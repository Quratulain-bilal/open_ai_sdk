
from agents.handoffs import Handoff
from pydantic import BaseModel
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, handoff, RunConfig,RunContextWrapper
from openai import AsyncOpenAI
from dotenv import load_dotenv
from rich import print
import os
import asyncio



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

# ✅ Step 1: Define input type
class MyInput(BaseModel):
    name: str

# ✅ Step 2: Agent jo kaam karega jab handoff hoga
my_agent = Agent(
    name="GreetingAgent",
    instructions="Say hello using the user's name.",
    handoff_description="Greets the user."
)

# ✅ Step 3: Handoff function (input receive karega)
def handle(ctx: RunContextWrapper, input: MyInput):
    print(f"Hello, {input.name}! 👋")

# ✅ Step 4: Handoff create karo (sirf class name dena hai, instance nahi)
my_handoff = handoff(
    agent=my_agent,
    on_handoff=handle,
    input_type=MyInput
)

# ✅ Step 5: Triage agent jo handoff karega
main_agent = Agent(
    name="MainAgent",
    instructions="If someone says hello, hand off to GreetingAgent.",
    handoffs=[my_handoff]
)

# ✅ Step 6: Run the agent
async def run():
    await Runner.run(
        starting_agent=main_agent,
        input="Hello, my name is Ayesha.",
        run_config=config
    )

asyncio.run(run())
