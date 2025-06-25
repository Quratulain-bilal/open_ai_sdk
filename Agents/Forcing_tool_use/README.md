🔷  Tools in Agents SDK
Agents SDK mein tools woh functions hain jinhein aap LLM ko use karne dete ho — for real-world data fetching, calculations, etc.

Lekin... by default, jab aap tool dete ho, LLM ka choice hota hai ke wo tool ko call kare ya nahi. Iska matlab:

Sirf tool provide karna ≠ tool zaroor call hoga ❌

🧩 Problem: Why Force Tool Use?
Kahi dafa aap chahte ho:

LLM hamesha tool se kaam le

bina tool ke jawab accept nahi ho

Ya sirf ek specific tool use ho, koi aur nahi

Is wajah se SDK ne introduce kiya:

🔧 ModelSettings.tool_choice
Option	Meaning	Urdu Explanation
"auto" (default)	LLM decide karega tool use ho ya nahi	Apne aap decide kare
"required"	Tool use zaroor hoga, but kaunsa – LLM decide karega	Lazmi tool call kare
"none"	Tool use bilkul allowed nahi	Tool completely disable
"tool_name"	Sirf wohi tool use ho jo aap ne specify kiya	Kisi ek khas tool ko allow karna

🔁 Internal Lifecycle When You Use tool_choice
Let’s break it step-by-step like an inner agent + LLM chat cycle:

✅ Step 1: Agent Setup with Tool
python
Copy
Edit
agent = Agent(tools=[weather_lookup], model_settings={"tool_choice": "required"})
Yahan agent ko tool diya gaya.

Aur model_settings.tool_choice = required lagaya gaya → force karega LLM ko tool zaroor use karna hai.

✅ Step 2: Runner Starts Loop
Aap Runner.run() ya Runner.run_sync() lagate ho.

Agent gets invoked.

LLM ko input bhejta hai — What’s the weather today?

✅ Step 3: LLM Decision
Agar tool_choice = "required" hai:

LLM ke paas koi option nahi.

Usse zaroor tool call karna padta hai.

LLM constructs a function_call.

✅ Step 4: Tool Call Execution
SDK identifies tool name (e.g. weather_lookup)

Tool function run hota hai.

Result return hota hai: “Today is sunny”

✅ Step 5: LLM Re-Call? OR Stop?
Yahan pe do possibilities:

🔁 Default:
Tool ka result wapas LLM ko jata hai.

LLM kuch aur add karega (e.g. "Based on the weather lookup, here's what I found...")

🛑 Forced Stop:
Aap ne tool_use_behavior = "stop_on_first_tool" lagaya:

python
Copy
Edit
agent.tool_use_behavior = "stop_on_first_tool"
Iska matlab: Tool ka output direct user ko show karo, LLM se aur kuch mat lo.

Bohat helpful jab aap chahte ho predictable output, jaise calculator, translation, data lookup etc.

⚠️ Tool Loop Risk: Infinite Loop Bug
Jab tool call hota hai, aur LLM fir us result pe naya tool call kar deta hai → infinite loop ban sakta hai 😱

Is liye by default:

python
Copy
Edit
agent.reset_tool_choice = True
Yani har tool call ke baad tool_choice = auto ho jata hai taake loop na chale.

Agar aap loop chahte ho intentionally, to:

python
Copy
Edit
agent.reset_tool_choice = False
Use with extreme care.

📦 Behind the Scenes (Inner Mechanics)
1. tool_choice inject hota hai model_settings mein:
json
Copy
Edit
{
  "tool_choice": "required"
}
2. LLM ko yeh instruction milta hai ke tool zaroor call karo.
3. Tool call ka JSON response aata hai:
json
Copy
Edit
{
  "function_call": {
    "name": "weather_lookup",
    "arguments": {}
  }
}
4. SDK tool ko resolve karta hai → execute karta hai.
5. Response goes to:
LLM (if behavior = default)

Or Direct to user (if stop_on_first_tool)

💡 Pro Tip: Use tool_choice = "tool_name" for Precision

model_settings = ModelSettings(tool_choice="weather_lookup")
Yani sirf ye tool allowed hai, aur LLM kisi aur ka naam bhi le to error.

🧠 Summary: Tool Forcing Logic
Concept	Explanation
tool_choice="required"	Tool ka use zaroori hai
tool_choice="none"	Tool use completely disabled
reset_tool_choice=True	Tool ke baad auto reset kare behavior
tool_use_behavior="stop_on_first_tool"	Tool ka output = final output
tool_choice="tool_name"	Sirf ek tool allow kare
