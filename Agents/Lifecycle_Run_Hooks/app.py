from agents import Agent, AgentHooks, Runner, RunContextWrapper, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import asyncio

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

@dataclass
class CustomerContext:
    name: str
    address: str


@function_tool
def confirm_address(ctx: RunContextWrapper[CustomerContext]) -> str:
    return f"Confirming your order to be delivered at: {ctx.context.address}"

#Step 3: AgentHooks to log activity
class PizzaHooks(AgentHooks[CustomerContext]):

    async def on_start(self, ctx, agent):
        print(f"\n🍕 Agent started for {ctx.context.name}")

    async def on_tool_start(self, ctx, agent, tool):
        print(f"\n🛠️ Tool starting: {tool.name}")

    async def on_tool_end(self, ctx, agent, tool, result):
        print(f"\n✅ Tool completed. Result: {result}")

    async def on_end(self, ctx, agent, output):
        print(f"\n📦 Agent done. Final answer: {output}")

#  Pizza Agent
pizza_agent = Agent[CustomerContext](
    name="PizzaBot",
    instructions="Take pizza order. Confirm size, toppings, and address politely.",
    model=model,
    tools=[confirm_address],
    hooks=PizzaHooks()
)

# Runner
async def main():
    customer = CustomerContext(name="Zainab", address="123 Main Street, Karachi")

    result = await Runner.run(
        starting_agent=pizza_agent,
        input="I want a large pizza with extra cheese and olives.",
        context=customer
    )

    print("\nFinal Response:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
