🔍 Runner mein handoff_input_filter pass karne ka faida (Compared to Agent ke andar dena)
Jab aap handoff_input_filter ko directly Agent ke andar pass karte hain, to wo filter sirf usi agent ke handoff process par apply hota hai. Iska matlab hai ke agar aap ke paas multi-level agents ka structure ho — jaise ke ek Triage Agent jo kisi query ko kisi aur Sub-Agent ko handoff karta hai — to us case mein filter only uss agent tak restricted hota hai jahan pe aapne use assign kiya hai. Iske baraks, agar aap handoff_input_filter ko Runner ke RunConfig object ke zariye pass karte hain, to yeh global level pe kaam karta hai — yani yeh filter har us handoff pe apply hoga jo kisi bhi level pe ho raha ho, chahe wo Triage agent se ho ya kisi nested agent se. Is tarah aap centralized control rakhte hain ke kaunsi input query handoff hone se pehle filter ho — aur aapko har agent ke andar separately filter lagani ki zarurat nahi padti. Yeh scalability aur debugging dono ke liye bohat hi powerful technique hai, especially jab aapka system complex aur layered ho jaata hai.


✅ 🔁 Complete Example with Handoff Input Filter — Passed via Runner.run_sync
python
Copy
Edit
from openai import Agent, Runner, RunConfig, FunctionTool

# Tool: Answer science-related questions
def science_answer_tool(question: str) -> str:
    return f"This is a science answer to: {question}"

# Tool wrap in FunctionTool
science_tool = FunctionTool.from_function(
    function=science_answer_tool,
    name="science_answer_tool",
    description="Answers science-related questions."
)

# Sub-Agent: Handles science questions
science_agent = Agent(
    name="ScienceAgent",
    instructions="Answer only science-related questions.",
    tools=[science_tool]
)

# Main Agent: Decides when to handoff
triage_agent = Agent(
    name="TriageAgent",
    instructions="Triage and handoff science questions to ScienceAgent.",
    tools=[],
    handoff_agents=[science_agent]
)

# ✅ Filter: Replace "physics" with "science"
def handoff_filter(input_text):
    return input_text.replace("physics", "science")

# ✅ RUNNER: Pass filter directly via RunConfig
result = Runner.run_sync(
    starting_agent=triage_agent,
    input="What is physics?",
    run_config=RunConfig(handoff_input_filter=handoff_filter)
)

# Print final output
print(result.final_output)
📌 What’s Happening?
Input: "What is physics?"

Filter: "physics" → "science"
(ab input ban gaya "What is science?")

Triage Agent decides to handoff

Science Agent handles it using science_answer_tool

✅ Final output is printed

🧠 Why pass the filter in Runner, not Agent?
Agar aap filter ko agent mein dete hain, to wo sirf usi agent ke liye hota hai. Lekin agar aap Runner.run_sync() ke andar RunConfig mein dete ho:

To aap global level pe modify kar rahe ho input ko

Ye ensure karta hai ke handoff hone se pehle input ko preprocess kiya jaye

























✅ 🔁 Complete Example with Handoff Input Filter — Passed via Runner.run_sync
p
from openai import Agent, Runner, RunConfig, FunctionTool

# Tool: Answer science-related questions
def science_answer_tool(question: str) -> str:
    return f"This is a science answer to: {question}"

# Tool wrap in FunctionTool
science_tool = FunctionTool.from_function(
    function=science_answer_tool,
    name="science_answer_tool",
    description="Answers science-related questions."
)

# Sub-Agent: Handles science questions
science_agent = Agent(
    name="ScienceAgent",
    instructions="Answer only science-related questions.",
    tools=[science_tool]
)

# Main Agent: Decides when to handoff
triage_agent = Agent(
    name="TriageAgent",
    instructions="Triage and handoff science questions to ScienceAgent.",
    tools=[],
    handoff_agents=[science_agent]
)

# ✅ Filter: Replace "physics" with "science"
def handoff_filter(input_text):
    return input_text.replace("physics", "science")

# ✅ RUNNER: Pass filter directly via RunConfig
result = Runner.run_sync(
    starting_agent=triage_agent,
    input="What is physics?",
    run_config=RunConfig(handoff_input_filter=handoff_filter)
)

# Print final output
print(result.final_output)
📌 What’s Happening?
Input: "What is physics?"

Filter: "physics" → "science"
(ab input ban gaya "What is science?")

Triage Agent decides to handoff

Science Agent handles it using science_answer_tool

✅ Final output is printed

