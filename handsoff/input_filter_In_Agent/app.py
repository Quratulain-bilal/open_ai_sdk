
from agents.handoffs import HandoffInputData
from dotenv import load_dotenv
from typing import TypeVar
from rich import print
import os
from agents import Agent, Runner, handoff, HandoffInputData, RunConfig,OpenAIChatCompletionsModel,set_tracing_disabled,AsyncOpenAI

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"


external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# --- Model setup ---
model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


#  Input filter function
def handoff_function(data: HandoffInputData) -> HandoffInputData:
    print("🔍 Agent level handoff filter triggered")
    return data  # Yahan aap modify bhi kar sakte hain input ko

#  Sub agent: addition ke liye
addition_agent = Agent(
    name="Addition Agent",
    instructions="Add karna ata hai.",
    model=model,
)

#  Main agent: jo handoff karega addition agent ko
math_agent = Agent(
    name="Math Agent",
    instructions="Agar input addition ka ho to addition agent ko handoff karo.",
    model=model,
    handoffs=[
        handoff(
            agent=addition_agent,
            input_filter=handoff_function  # ✅ Yahan lagta hai input filter agent-level par
        )
    ]
)

#  Run the agent
result = Runner.run_sync(
    starting_agent=math_agent,
    input="Add 4 + 4"
)
print(result.final_output)
