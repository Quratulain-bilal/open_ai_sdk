from agents import (
    Agent, Runner, handoff,
    OpenAIChatCompletionsModel, AsyncOpenAI,
    set_tracing_disabled
)
from agents.extensions import handoff_filters  #  Yeh zaruri hai input_filter ke liye
from dotenv import load_dotenv
import os
import asyncio

#  Setup
set_tracing_disabled(True)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

#  Refund Agent
refund_agent = Agent(
    name="Refund Agent",
    instructions="You help users with refund issues. Just respond to what user asked, based on clean history."
)

#  Main Agent
main_agent = Agent(
    name="Main Agent",
    instructions="""
You're a support assistant. If user talks about refunds, hand off to Refund Agent.
""",
    model=model,
    handoffs=[
        handoff(
            agent=refund_agent,

            #  Yeh line filter karegi history se tools ya extra data
            input_filter=handoff_filters.remove_all_tools
        )
    ]
)

#  Runner
async def main():
    print("💬 Ask something:")
    user_input = input("You: ")

    result = await Runner.run(
        starting_agent=main_agent,
        input=user_input,
    )

    print("\n✅ Final Output:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
