from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")


client = AsyncOpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai")
model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-1.5-flash")

#  Base agent
base_agent = Agent(
    name="BasePizzaAgent",
    instructions="You are a pizza ordering assistant. Help users with their pizza order.",
    model=model
)

#  Regular Pizza agent
regular_pizza_agent = base_agent.clone(
    name="RegularPizzaAgent"
)

#   Party Pizza agent (bulk orders)
party_pizza_agent = base_agent.clone(
    name="PartyPizzaAgent",
    instructions="You are a pizza assistant specialized in large/bulk orders for events. Suggest combos and discounts."
)

#  Run both agents
async def main():
    print(" Regular Order:")
    result1 = await Runner.run(starting_agent=regular_pizza_agent, input="I want a small pepperoni pizza.")
    print(result1.final_output)

    print("\n Party Order:")
    result2 = await Runner.run(starting_agent=party_pizza_agent, input="I need 10 large pizzas for a birthday.")
    print(result2.final_output)

if __name__ == "__main__":
    asyncio.run(main())
