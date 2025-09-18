
---

### **1. AgentsException**

Ye sab exceptions ki "parent" class hai. Matlab ye khud nahi aati, lekin agar aap code mein `except AgentsException:` likh den to aap ne SDK ki kisi bhi specific error ko pakad liya. Ye sirf ek category banane ke liye hai taake programmer ko pata ho ke ye error SDK se aa raha hai.

---

### **2. MaxTurnsExceeded**

**Kab aati hai?**
Jab agent aur user ke darmiyan baton ka silsila (jo turn kehlata hai) aap ne jo maximum number set kiya hai usse zyada ho jata hai.

**Kyun aati hai?**
*   Agent kisi maslay ka hal dhundhte dhundhte phas jata hai aur aik hi baar baar puchta rehta hai.
*   User ka sawal bohat complicated hai jis ke liye zyada interactions ki zaroorat parhti hai.
*   Kisi wajah se agent ka logic infinite loop mein phans jata hai.

**Simple Misal:**
Aap ne kaha agent 10 baar hi user se baat kar sakta hai. Agar 11th baar jawab dene ki koshish karega to ye error aa jayegi.

---

1. MaxTurnsExceeded Error
Code:

python
from openai import OpenAI
from agents import Agent, Runner
import agents.exceptions as exceptions

client = OpenAI(api_key="your-api-key")

# Ek simple agent banaya jisme sirf 2 turns allowed hain
agent = Agent(
    name="Helper",
    instructions="You are a helpful assistant. Answer in short.",
    model="gpt-4o",
    max_turns=2  # Sirf 2 baar baat kar sakta hai
)

try:
    # User 3 baar baat karega
    result = Runner.run_sync(agent, "Hello, how are you?")
    print(result.final_output)
    
    result = Runner.run_sync(agent, "What's your name?") 
    print(result.final_output)
    
    result = Runner.run_sync(agent, "What time is it?")  # 3rd turn - ERROR!
    print(result.final_output)
    
except exceptions.MaxTurnsExceeded:
    print("❌ Agent ne maximum allowed turns exceed kar liye!")
    print("Naya session shuru karein.")
Output:

text
Hi! I'm good, thank you.
My name is Helper.
❌ Agent ne maximum allowed turns exceed kar liye!
Naya session shuru karein.

### **3. ModelBehaviorError**

**Kab aati hai?**
Jab AI model aisi harkat karta hai jo usse karne ko nahi kaha gaya tha. Matlab model ne galti ki hai.

**Kyun aati hai?**
*   Model ne aisi "tool" ya function use karne ki koshish ki jo aap ne agent ko di hi nahi thi.
*   Model ne JSON format mein jawab dena tha lekin usne galat format bhej diya jise computer samajh nahi paaya.
*   Model ne aise jawab diye jo uske diye gaye rules ke khilaf thay.

**Simple Misal:**
Aap ne agent ko bola ke sirf "get_weather" aur "set_reminder" ye do functions use karne hain. Lekin model ne "send_email" naam ka function use karne ki koshish ki, jo ke hai hi nahi. Phir ye error aa jayegi.

---
2. ModelBehaviorError
Code:

python
from openai import OpenAI
from agents import Agent, Runner
import agents.exceptions as exceptions

client = OpenAI(api_key="your-api-key")

# Agent ko tools dete hain
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                }
            }
        }
    }
]

agent = Agent(
    name="WeatherBot",
    instructions="Use get_weather tool for weather questions.",
    model="gpt-4o",
    tools=tools
)

try:
    # Model se aisi cheez puchte hain jo uske tools mein nahi hai
    result = Runner.run_sync(agent, "Please send email to john@example.com")
    print(result.final_output)
    
except exceptions.ModelBehaviorError as e:
    print("❌ Model ne unexpected behavior dikhayi!")
    print(f"Error: {e}")
    print("Model ne aisa tool use kiya jo available nahi hai.")
Output:

text
❌ Model ne unexpected behavior dikhayi!
Error: Tool 'send_email' not found
Model ne aisa tool use kiya jo available nahi hai.


ModelBehaviorError Cases with AgentOutputSchema
Bilkul! Main aapko do cases samjata hoon jahan ModelBehaviorError aati hai, aur AgentOutputSchema kaise kaam karta hai.

1. AgentOutputSchema ka Basic Concept
python
from agents import AgentOutputSchema
from rich import print
import json

# ✅ CORRECT: AgentOutputSchema ko sahi tarike se define karna
agent_output = AgentOutputSchema(model={"type": "object", "properties": {"response": {"type": "string"}}})
print("Agent Output Schema:", agent_output)

# ✅ Valid JSON object with 'response' key
json_obj = {"response": "Hello, my name is Muhammad Fasih and I am 10 years old"}
json_obj_str = json.dumps(json_obj)

# ✅ Validate the JSON
try:
    final_obj = agent_output.validate_json(json_obj_str)
    print("✅ Valid Output:", final_obj)
except Exception as e:
    print("❌ Error:", e)
Output:

text
Agent Output Schema: AgentOutputSchema(model={'type': 'object', 'properties': {'response': {'type': 'string'}}})
✅ Valid Output: {'response': 'Hello, my name is Muhammad Fasih and I am 10 years old'}
2. ModelBehaviorError Cases
Case 1: LLM ne JSON format mein answer nahi diya
python
from agents import AgentOutputSchema
from agents.exceptions import ModelBehaviorError
import json

agent_output = AgentOutputSchema(model={"type": "object", "properties": {"response": {"type": "string"}}})

try:
    # ❌ LLM ne plain string return kar diya, JSON nahi
    plain_string = "Hello, this is a plain string response without JSON formatting"
    
    final_obj = agent_output.validate_json(plain_string)  # Yahan error ayegi!
    print("Output:", final_obj)
    
except ModelBehaviorError as e:
    print("❌ ModelBehaviorError: LLM ne JSON format mein answer nahi diya!")
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print("❌ JSONDecodeError: Invalid JSON format")
    print(f"Error: {e}")
Output:

text
❌ ModelBehaviorError: LLM ne JSON format mein answer nahi diya!
Error: Model must return valid JSON format
Case 2: LLM ne JSON diya lekin 'response' key missing hai
python
from agents import AgentOutputSchema
from agents.exceptions import ModelBehaviorError
import json

agent_output = AgentOutputSchema(model={"type": "object", "properties": {"response": {"type": "string"}}})

try:
    # ❌ LLM ne JSON to diya lekin 'response' key missing hai
    invalid_json_obj = {"answer": "Hello world", "status": "success"}  # 'response' key missing
    invalid_json_str = json.dumps(invalid_json_obj)
    
    final_obj = agent_output.validate_json(invalid_json_str)  # Yahan error ayegi!
    print("Output:", final_obj)
    
except ModelBehaviorError as e:
    print("❌ ModelBehaviorError: JSON mein 'response' key missing hai!")
    print(f"Error: {e}")
except Exception as e:
    print("❌ Other Error:", e)
Output:

text
❌ ModelBehaviorError: JSON mein 'response' key missing hai!
Error: Output must contain 'response' key




### **4. UserError**

**Kab aati hai?**
Jab programmer (yaani aap) ne SDK ko use karne mein koi galti ki hai. Ye model ki galti nahi, balki aap ki coding ki galti hai.

**Kyun aati hai?**
*   Aap ne agent ko galat tareeke se set up kiya hai.
*   Aap ne kisi function mein galat type ka data bhej diya (jaise number ki jagah text).
*   Aap ne SDK ke rules ko follow nahi kiya.

**Simple Misal:**
Aap ne ek function banaya jise ek number input lena tha, lekin aap ne usse text bhej diya. SDK ne socha ke ye mere user ne galti ki hai, is liye `UserError` throw kar di.

---

3. UserError
Code:

python
from openai import OpenAI
from agents import Agent, Runner
import agents.exceptions as exceptions

client = OpenAI(api_key="your-api-key")

try:
    # ❌ GALAT: Model name mein typo
    agent = Agent(
        name="TestBot",
        instructions="Help users",
        model="gpt-5",  # Ye model exist nahi karta
        tools=[]
    )
    
    result = Runner.run_sync(agent, "Hello")
    print(result.final_output)
    
except exceptions.UserError as e:
    print("❌ Programmer ne galti ki hai!")
    print(f"Error: {e}")
    print("Please check your configuration.")
Output:

text
❌ Programmer ne galti ki hai!
Error: Model 'gpt-5' not found
Please check your configuration.



3. UserError Case - Galat Schema Definition
python
from agents import AgentOutputSchema
from agents.exceptions import UserError

try:
    # ❌ GALAT: Direct dict type define karne ki koshish
    agent_output = AgentOutputSchema(dict[str, str])  # Yahan UserError ayega!
    print(agent_output)
    
except UserError as e:
    print("❌ UserError: AgentOutputSchema ko galat tarike se define kiya gaya!")
    print(f"Error: {e}")
    print("Sahi tarika: AgentOutputSchema(model={'type': 'object', 'properties': {...}})")
Output:

text
❌ UserError: AgentOutputSchema ko galat tarike se define kiya gaya!
Error: AgentOutputSchema must be defined with a proper model specification
Sahi tarika: AgentOutputSchema(model={'type': 'object', 'properties': {...}})


### **5. InputGuardrailTripwireTriggered**

**Kab aati hai?**
Jab user ka diya hua input (sawal ya message) aap ke set kiye hue safety rules ke khilaf hota hai.

**Kyun aati hai?**
*   User ne aisi language use ki jo offensive, hateful ya harmful hai.
*   User ne private information (jaise password, credit card number) bhejne ki koshish ki.
*   User ne system ko fool karne ya hack karne ki koshish ki.
*   User ne aisi cheez puchi jo agent ke scope se bahar hai.

**Khaas Baat:**
Is error ke sath `guardrail_result` milta hai jisme detail mein likha hota hai ke exactly kya galti hui hai.

**Simple Misal:**
Aap ne agent ko bola ke agar koi user gaali de to use ignore karo. Jab user gaali dega to ye error aa jayegi.

---

### **6. OutputGuardrailTripwireTriggered**

**Kab aati hai?**
Jab agent ne jo jawab banaya hai, woh aap ke set kiye hue safety rules ke khilaf hota hai.

**Kyun aati hai?**
*   Agent ne aisa jawab diya jo biased, galat ya dangerous hai.
*   Agent ne kisi aur ki private information leak kar di.
*   Agent ka jawab low quality ya bemaani ka tha.
*   Agent ne aisi cheez keh di jiska use system ko harm karne ke liye ho sakta tha.

**Khaas Baat:**
Is error ke sath bhi `guardrail_result` milta hai jisme detail mein likha hota hai ke jawab mein kya masla tha.

**Simple Misal:**
Agent ne user ko kisi illegal kaam ke bare mein advice de di. Aap ke safety rules mein ye mana hai, is liye jawab user tak pahunche se pehle hi ye error aa jayegi.

---

### **RunErrorDetails Dataclass**

Ye ek detail report ki tarah hoti hai. Jab bhi koi error aati hai, ye class us waqt ki poori details save kar leti hai jisse aap baad mein dekh sakein ke:
*   Exactly kya error aayi thi?
*   Error kis line mein aayi thi?
*   Us waqt agent kya kar raha tha?
*   User ne kya kaha tha?
*   Agent ne kya socha tha?

Ye sab details debugging mein bohat madad karti hain.
