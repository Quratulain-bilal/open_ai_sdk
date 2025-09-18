# 📄 **OpenAI Agents SDK – Exceptions & Error Handling (Complete README)**  


---


## 🧩 Overview

  
- Kya **user** ne galti ki? → `UserError`  
- Kya **model** ne galti ki? → `ModelBehaviorError`  
- Kya **safety rules** violate hui? → `Input/OutputGuardrailTripwireTriggered`  
- Kya **agent ne zyada baar baat ki**? → `MaxTurnsExceeded`

Sab exceptions ka **base class** hai: `AgentsException`

---

## 🚨 1. `AgentsException` — Base Class

### 📌 Purpose:
Sabhi agent-specific exceptions ka **common parent**.  
Agar aap `except AgentsException:` likh dein — to **sab agent errors** catch ho jayengi.

### 🧑‍💻 Example:
```python
try:
    result = agent.run("Hello")
except AgentsException as e:
    print(f"Agent-related error: {e}")
```

### 💡 Kyun Banaya Gaya?
- Taki aap **agent errors** aur **general Python errors** (`ValueError`, `KeyError`) alag se handle kar saken.
- Logging, monitoring, aur debugging ke liye useful.

---

## 🔄 2. `MaxTurnsExceeded`

### ❓ Kab Aati Hai?
Jab agent aur user ke darmiyan **maximum allowed turns** (baatein) exceed ho jayein.

### ⚠️ Kyun Aati Hai?
- Agent kisi masle mein phas kar **infinite loop** mein chala jata hai.
- User ka sawal **bohat complex** hai — solve karne ke liye zyada steps chahiye.
- Agent ka logic **galat hai** — har baar same cheez poochta rehta hai.

### 🧪 Simple Misal:
Aap ne agent ko kaha — *“Sirf 2 baar jawab de sakte ho.”*  
User ne 3 sawal puche → **3rd turn pe error!**

### 💻 Code Example:
```python
from openai import OpenAI
from agents import Agent, Runner
import agents.exceptions as exceptions

client = OpenAI(api_key="your-api-key")

# Agent with max 2 turns
agent = Agent(
    name="Helper",
    instructions="Answer in short.",
    model="gpt-4o",
    max_turns=2
)

try:
    result = Runner.run_sync(agent, "Hello, how are you?")  # Turn 1
    print(result.final_output)

    result = Runner.run_sync(agent, "What's your name?")    # Turn 2
    print(result.final_output)

    result = Runner.run_sync(agent, "What time is it?")     # Turn 3 → ERROR!
    print(result.final_output)

except exceptions.MaxTurnsExceeded:
    print("❌ Agent ne maximum allowed turns exceed kar liye!")
    print("Naya session shuru karein.")
```

### 🖨️ Output:
```
Hi! I'm good, thank you.
My name is Helper.
❌ Agent ne maximum allowed turns exceed kar liye!
Naya session shuru karein.
```

---

## 🤖 3. `ModelBehaviorError`

### ❓ Kab Aati Hai?
Jab **AI model** aisi cheez kare jo usse karne ko **nahi kaha gaya tha** — ya jo **invalid/unsafe** ho.

### ⚠️ Kyun Aati Hai?
- Model ne **aisa tool use kiya** jo agent ke paas hi nahi tha.
- Model ne **JSON format mein jawab nahi diya** — jise system parse nahi kar paya.
- Model ne **schema ke khilaf** output diya — jaise required key missing.

### 🧪 Simple Misal:
Aap ne agent ko sirf `get_weather` aur `set_reminder` tools diye.  
Lekin model ne `send_email` use karne ki koshish ki → **Error!**

### 💻 Code Example:
```python
from openai import OpenAI
from agents import Agent, Runner
import agents.exceptions as exceptions

client = OpenAI(api_key="your-api-key")

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
    result = Runner.run_sync(agent, "Please send email to john@example.com")
    print(result.final_output)

except exceptions.ModelBehaviorError as e:
    print("❌ Model ne unexpected behavior dikhayi!")
    print(f"Error: {e}")
    print("Model ne aisa tool use kiya jo available nahi hai.")
```

### 🖨️ Output:
```
❌ Model ne unexpected behavior dikhayi!
Error: Tool 'send_email' not found
Model ne aisa tool use kiya jo available nahi hai.
```

---

## 📐 ModelBehaviorError + AgentOutputSchema Cases

### ✅ Case 1: Valid Schema + Valid JSON
```python
from agents import AgentOutputSchema
import json

agent_output = AgentOutputSchema(
    model={"type": "object", "properties": {"response": {"type": "string"}}}
)

json_obj = {"response": "Hello, my name is Muhammad anna and I am 20 years old"}
json_str = json.dumps(json_obj)

final_obj = agent_output.validate_json(json_str)
print("✅ Valid Output:", final_obj)
```

**Output:**
```
✅ Valid Output: {'response': 'Hello, my name is anna and I am 20 years old'}
```

---

### ❌ Case 2: LLM ne JSON format mein answer nahi diya
```python
try:
    plain_string = "Hello, this is a plain string without JSON"
    final_obj = agent_output.validate_json(plain_string)
except ModelBehaviorError as e:
    print("❌ ModelBehaviorError: LLM ne JSON format mein answer nahi diya!")
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print("❌ JSONDecodeError: Invalid JSON format")
    print(f"Error: {e}")
```

**Output:**
```
❌ ModelBehaviorError: LLM ne JSON format mein answer nahi diya!
Error: Model must return valid JSON format
```

---

### ❌ Case 3: LLM ne JSON diya lekin 'response' key missing hai
```python
try:
    invalid_json = {"answer": "Hello world", "status": "success"}  # 'response' missing
    invalid_str = json.dumps(invalid_json)
    final_obj = agent_output.validate_json(invalid_str)
except ModelBehaviorError as e:
    print("❌ ModelBehaviorError: JSON mein 'response' key missing hai!")
    print(f"Error: {e}")
```

**Output:**
```
❌ ModelBehaviorError: JSON mein 'response' key missing hai!
Error: Output must contain 'response' key
```

---

## 👨‍💻 4. `UserError`

### ❓ Kab Aati Hai?
Jab **programmer (aap)** ne SDK ko galat istemal kiya ho — model ki galti nahi, **aapki galti**.

### ⚠️ Kyun Aati Hai?
- Galat model name diya (jaise `gpt-5` jo exist nahi karta).
- Galat type ka data bheja — number ki jagah string.
- SDK ke rules ko follow nahi kiya — jaise `AgentOutputSchema` galat define kiya.

### 🧪 Simple Misal:
Aap ne `AgentOutputSchema` ko `dict[str, str]` se define karne ki koshish ki — lekin SDK ne bola:  
> “Nahi bhai — `model={...}` object pass karo!”

### 💻 Code Example:
```python
try:
    # ❌ GALAT: Model name mein typo
    agent = Agent(
        name="TestBot",
        instructions="Help users",
        model="gpt-5",  # Ye model exist nahi karta
        tools=[]
    )
    result = Runner.run_sync(agent, "Hello")
except exceptions.UserError as e:
    print("❌ Programmer ne galti ki hai!")
    print(f"Error: {e}")
    print("Please check your configuration.")
```

**Output:**
```
❌ Programmer ne galti ki hai!
Error: Model 'gpt-5' not found
Please check your configuration.
```

---

### ❌ UserError Case — Galat Schema Definition
```python
try:
    # ❌ GALAT: Direct type pass karne ki koshish
    agent_output = AgentOutputSchema(dict[str, str])
except UserError as e:
    print("❌ UserError: AgentOutputSchema ko galat tarike se define kiya gaya!")
    print(f"Error: {e}")
    print("Sahi tarika: AgentOutputSchema(model={'type': 'object', 'properties': {...}})")
```

**Output:**
```
❌ UserError: AgentOutputSchema ko galat tarike se define kiya gaya!
Error: AgentOutputSchema must be defined with a proper model specification
Sahi tarika: AgentOutputSchema(model={'type': 'object', 'properties': {...}})
```

---

## 🛡️ 5. `InputGuardrailTripwireTriggered`

### ❓ Kab Aati Hai?
Jab **user ka input** (sawal/message) aap ke **safety rules** ke khilaf ho.

### ⚠️ Kyun Aati Hai?
- User ne **gaali**, **hateful speech**, ya **violent content** likha.
- User ne **PII** (password, credit card, SSN) bhejne ki koshish ki.
- User ne system ko **hack/fool** karne ki koshish ki.

### 🧩 Khaas Baat:
Is error ke sath **`guardrail_result: InputGuardrailResult`** milta hai — jisme detail hoti hai:
- Kis category mein aaya? (`violence`, `hate`, `pii`)
- Confidence score?
- Sanitized input?

### 🧪 Simple Misal:
Aap ne agent ko bola — *“Agar koi gaali de to ignore karo.”*  
User ne gaali di → **Error!**

---

## 🛡️ 6. `OutputGuardrailTripwireTriggered`

### ❓ Kab Aati Hai?
Jab **agent ka output** aap ke **safety rules** ke khilaf ho.

### ⚠️ Kyun Aati Hai?
- Agent ne **biased/dangerous** jawab diya.
- Agent ne **private info leak** kar di.
- Agent ka jawab **low quality** ya **bemaani** tha.
- Agent ne **illegal advice** di.

### 🧩 Khaas Baat:
Is error ke sath **`guardrail_result: OutputGuardrailResult`** milta hai — jisme detail hoti hai:
- Output kis cheez ke liye block hua?
- Kya suggested action hai?

### 🧪 Simple Misal:
Agent ne user ko *“How to hack a bank?”* ka jawab de diya → **Error!**

---

## 📊 `RunErrorDetails` Dataclass

### 📌 Purpose:
Jab bhi koi error aaye — ye class **us waqt ki poori details** save kar leti hai — debugging ke liye bohat useful.

### 🧾 Kya Save Karta Hai?
- `error_type`: `MaxTurnsExceeded`, `ModelBehaviorError`, etc.
- `message`: Error ka full message
- `timestamp`: Kab hua tha
- `context`: Agent kya kar raha tha? User ne kya kaha tha?
- `input_used`: User ka input
- `step_number`: Kis turn/step pe error aaya





## 🎯 Exception Hierarchy (Visual)

```
Exception
└── AgentsException
    ├── MaxTurnsExceeded
    ├── ModelBehaviorError
    ├── UserError
    ├── InputGuardrailTripwireTriggered
    └── OutputGuardrailTripwireTriggered
```

---

## 🧭 Quick Reference Table

| Exception                        | Triggered When…                                      | Responsibility       | Example Cause                          |
|----------------------------------|------------------------------------------------------|----------------------|----------------------------------------|
| `MaxTurnsExceeded`               | Agent ne allowed steps/turns exceed kar diye          | System / Config      | Infinite loop, bad planning            |
| `ModelBehaviorError`             | LLM ne invalid JSON/tool call diya                   | Model / Prompt       | Hallucinated tool, bad schema          |
| `UserError`                      | Developer ne SDK galat use kiya                      | User (Developer)     | Missing arg, wrong type                |
| `InputGuardrailTripwireTriggered`| User input ne safety filter trigger kiya             | User Input           | Toxic query, PII, banned topic         |
| `OutputGuardrailTripwireTriggered`| Agent output ne safety filter trigger kiya          | Model Output         | Violent reply, leaked data, NSFW       |


