from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, RunContextWrapper, function_tool, ModelSettings
from dotenv import load_dotenv
import asyncio, os


# Load your API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini Client Setup
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Choose the model
model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)


# Real-life Example: Currency Tool


@function_tool
def convert_dollar_to_pkr(ctx: RunContextWrapper[None]) -> str:
    conversion_rate = 278  # Mock static rate
    dollars = 10
    return f"{dollars} USD = {dollars * conversion_rate} PKR"

@function_tool
def convert_celsius_to_fahrenheit(ctx: RunContextWrapper[None]) -> str:
    celsius = 30
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C = {fahrenheit}°F"

#  Agent with Forced Tool Use


agent = Agent(
    name="ConverterAgent",
    instructions="Use the tool to convert currencies or temperature. Don’t answer manually.",
    model=model,
    tools=[convert_dollar_to_pkr, convert_celsius_to_fahrenheit],
    model_settings=ModelSettings(tool_choice="required")  # Force tool use
)

# Run


async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Can you convert 10 dollars to rupees please?"
    )
    print("\n🔁 Final Output:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
