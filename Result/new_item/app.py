from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from dotenv import load_dotenv
import os


set_tracing_disabled(True)
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")


model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    ),
)

#  Math tool: multiply 2 numbers
@function_tool
def multiply_two_numbers(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b

#  Math Agent
math_agent = Agent(
    name="Math Genius",
    instructions="You're an expert at solving math problems.",
    model=model,
    tools=[multiply_two_numbers],
)

# History Agent
history_agent = Agent(
    name="Historian",
    instructions="You answer historical questions like dates, events, and timelines.",
    model=model,
)

#  Triage Agent
triage_agent = Agent(
    name="Triage",
    instructions=(
        "If the user asks about history, hand off to the Historian. "
        "If the user asks about math, hand off to the Math Genius."
    ),
    handoffs=[math_agent, history_agent],
    model=model,
)

#  Run the system
result = Runner.run_sync(
    starting_agent=triage_agent,
    input="What is 7 times 8?"
)

#  Final Output
print(" Final Answer:", result.final_output)

# 🧾 new_items breakdown
print(" Breakdown of Steps (new_items):")
for idx, item in enumerate(result.new_items):
    print(f"\n🔹 Step {idx+1}: Type = {item.type}")
    print(item)
