

from agents import Agent, Runner, HandoffInputData, handoff, RunHooks,set_tracing_disabled,RunConfig,OpenAIChatCompletionsModel,AsyncOpenAI
from rich import print
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY=os.environ.get("GEMINI_API_KEY")

config = RunConfig(
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=AsyncOpenAI(
            api_key=API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai"
        )
    )
)
import asyncio
from agents import Agent, Runner, RunHooks, handoff, HandoffInputData

# ------------------- Filter Functions ------------------- #

def history_input_filter(input: HandoffInputData) -> HandoffInputData:
    print("📘 [bold yellow]History Input Filter Triggered")
    input.input_history = "What is gravity?"
    return input

def science_input_filter(input: HandoffInputData) -> HandoffInputData:
    print("🔬 [bold green]Science Input Filter Triggered")
    input.input_history = "What is 9 + 10?"
    return input

def math_input_filter(input: HandoffInputData) -> HandoffInputData:
    print("➗ [bold blue]Math Input Filter Triggered")
    input.input_history = "Who was Napoleon?"
    return input

# ------------------- Agents ------------------- #

# Step 1: First define agents without handoffs
history_agent = Agent(
    name="HistoryAgent",
    instructions="You are an expert in History. If question is about science, handoff to ScienceAgent.",
)

science_agent = Agent(
    name="ScienceAgent",
    instructions="You are a Science expert. Handoff to MathAgent if it's a math question.",
)

math_agent = Agent(
    name="MathAgent",
    instructions="You are a Math genius. If it's a history question, handoff to HistoryAgent.",
)

# Step 2: Now assign handoffs with actual Agent objects
history_agent.handoffs = [
    handoff(agent=science_agent, input_filter=history_input_filter)
]

science_agent.handoffs = [
    handoff(agent=math_agent, input_filter=science_input_filter)
]

math_agent.handoffs = [
    handoff(agent=history_agent, input_filter=math_input_filter)
]

# ------------------- Hooks ------------------- #

class MyHooks(RunHooks):
    async def on_handoff(self, context, from_agent, to_agent):
        print(f"[bold cyan]👋 {from_agent.name} handed off to {to_agent.name}")

# ------------------- Main ------------------- #

async def main():
    result = await Runner.run(
        starting_agent=history_agent,
        input="Who discovered Newton's Laws?",
        run_config=config,
        hooks=MyHooks()
    )
    print("\n🏁 [bold magenta]Final Output:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())  # ✅ Correct async execution
