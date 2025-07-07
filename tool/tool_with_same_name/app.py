from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash",
)

# ✅ Same name for both tools: "math_tool"

@function_tool(name_override="math_tool")
def add(a: int, b: int) -> int:
    print("🟢 Running ADD tool")
    return a + b

@function_tool(name_override="math_tool")
def subtract(a: int, b: int) -> int:
    print("🔵 Running SUBTRACT tool")
    return a - b

# 🔧 Agent config
agent = Agent(
    name="Math Agent",
    instructions="You are a math expert. Use the correct tool to solve the user's question.",
    model=model,
    tools=[add, subtract],  # Both registered
    tool_use_behavior="auto"
)

# 👤 Prompt: clearly wants subtraction
result = Runner.run_sync(agent, "What is 9 minus 3?")
print("\n✅ Final Output:", result.final_output)
