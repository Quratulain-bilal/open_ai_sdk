from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, handoff, set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio


set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

# 🤖 Specialized Agents

refund_agent = Agent(
    name="Refund Agent",
    instructions="Answer refund-related questions like refund process, delay, and time to receive refund."
)

billing_agent = Agent(
    name="Billing Agent",
    instructions="Answer billing-related questions like incorrect charges, invoice requests, or due amounts."
)

faq_agent = Agent(
    name="FAQ Agent",
    instructions="Answer general FAQs like delivery time, working hours, or store location."
)

#  Triage Agent  Controller
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
You are a smart support agent. 
- If user asks about refunds, handoff to Refund Agent.
- If user asks about billing or charges, handoff to Billing Agent.
- If user asks general questions, handoff to FAQ Agent.
Otherwise, handle the message yourself.
""",
    handoffs=[
        handoff(refund_agent),
        handoff(billing_agent),
        handoff(faq_agent)
    ]
)

# 🚀 Runner
async def main():
    print(" Ask your question (billing, refund, or FAQ):")
    user_input = input(" You: ")

    result = await Runner.run(
        starting_agent=triage_agent,
        input=user_input,
    )

    print("\n🤖 Final Output:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
