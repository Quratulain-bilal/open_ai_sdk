import asyncio
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from agents.hooks import RunHooks
from agents.types import Step
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Client setup
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# RunConfig
config = RunConfig(model=model, model_provider=client)

#  Hook Class
class MySimpleHook(RunHooks[dict]):
    async def on_step_end(self, step: Step, context: dict):
        print("🔔 Agent ne kuch likha:")
        print(step.response)

# Agent
agent = Agent(
    name="EasyWriter",
    instructions="Tum aik simple likhne wale agent ho. Short texts likho.",
    model=model
)

# Main
async def main():
    await Runner.run(
        starting_agent=agent,
        input="Ek short message likho kisi dost ko.",
        context={"user": "Ain"},
        max_turns=2,
        hooks=MySimpleHook(),  # ✅ Easy hook used here
        run_config=config
    )

if __name__ == "__main__":
    asyncio.run(main())
