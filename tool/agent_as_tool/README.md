🌐 Translation System using Agents as Tools 
 ek chhota sa translation system banaya hai jisme  AI agents ko tool ki tarah use kiya hai. Har agent ek khaas kaam karta hai — koi English translation karta hai, koi Urdu translation karta hai. Phir ek main agent hota hai jo decide karta hai ke kaunsa kaam kis se karwana hai. Yeh hi system ka orchestrator agent hota hai.

🧠 Step-by-Step Explanation
✅ 1. Zaroori Libraries Import Ki ja rahi hain:

from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
from rich import print
import os
Ye sab packages aur tools chahiye taake aapka agent sahi tarah se kaam kare.

dotenv se aap apni API key chhupake use karte hain (security ke liye).

rich.print() colorful aur clean output dikhata hai terminal mein.

🔑 2. Environment Setup aur Model Banaya Gaya:
set_tracing_disabled(disabled=True)
load_dotenv()
API_KEY=os.environ.get("GEMINI_API_KEY")
Tracing off kiya gaya hai (yeh internal tracking hoti hai).

.env file se GEMINI ka API key liya gaya hai.

Is API key se hum Google Gemini language model ko connect kar rahe hain.


model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
)
Yeh model Google Gemini AI ka ek version hai jisko humne OpenAI SDK ke zariye connect kiya.

🌍 3. Do Agents Banaye Gaye (Ek English, Ek Urdu):

english_agent = Agent(
    name="English Linguistic",
    instructions="You are expert in English language",
    model=model
)
Yeh agent sirf English translation karta hai. Isko bataya gaya ke “tum English ke expert ho.”


urdu_agent = Agent(
    name="Urdu Linguistic",
    instructions="You are expert in Urdu language",
    model=model
)
Yeh agent Urdu ka specialist hai.

🔁 4. Main Agent (Orchestrator) Banaya Gaya:

orchestrator_agent=Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
Yeh main controller agent hai.

Yeh decide karega ke kis agent/tool ko kaam dena hai.

Agar koi input English mein translate karne ka kahay, toh English agent ko kaam milega.

Agar Urdu mein, toh Urdu agent ko.

🛠️ 5. Agents ko Tools Banaya gaya (as_tool)

tools=[
    english_agent.as_tool(
        tool_name="translate_to_english",
        tool_description="Translate the user's message to English"
    ),
    urdu_agent.as_tool(
        tool_name="translate_to_urdu",
        tool_description="Translate the user's message to Urdu",
    )
]
Ab English aur Urdu agents ko tool ki shakl di gayi.

Matlab ab orchestrator_agent in dono ko ek machine ke tool ki tarah use kar sakta hai.

tool_name aur tool_description se yeh decide hota hai ke kis tool se kya kaam lena hai.

▶️ 6. Runner se Input Diya aur Translation Karwaya:

result = Runner.run_sync(
    starting_agent=orchestrator_agent,
    input="'tum kia kar rahy ho', translate it to english"
)
Yahaan pe user ne bola: 'tum kia kar rahy ho' ko English mein translate karo.

Yeh input orchestrator_agent ko diya gaya.

Orchestrator ne analyze kiya, samjha ke English chahiye — toh usne translate_to_english tool ko activate kar diya.

Translation ho gayi.

📤 7. Final Output Print Kiya Gaya:

print(result.final_output)
Jo translation hui, wo final output ke taur pe print ki gayi.

🧩 Summary (Point-wise)

1️⃣	Agents aur model ko setup kiya gaya
2️⃣	Do experts banaye: English aur Urdu
3️⃣	In agents ko tools banaya using .as_tool()
4️⃣	Ek master agent banaya (orchestrator) jo decide karega kaunsa tool use hoga
5️⃣	User input diya gaya
6️⃣	Orchestrator ne relevant agent tool ko call kiya
7️⃣	Final translated result print kiya gaya

💡 Aap Isse Kya Seekh Sakte Hain?
Modular thinking: Har agent ek part (tool) hai jo alag kaam karta hai.

Smart orchestration: Aik master agent logic decide karta hai.

Agent as Tool: Kisi bhi agent ko as_tool() se doosre agent ka helper bana sakte ho.