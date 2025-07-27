import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os
import requests

from agents import function_tool, Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel


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



@function_tool
def get_time() -> str:
    """Return current time in HH:MM:SS format."""
    return datetime.now().strftime("%H:%M:%S")

@function_tool
def get_date() -> str:
    """Return current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")



@function_tool
def get_weather(country: str) -> str:
    """Returns hardcoded weather info for a given country."""
    return f"🌤️ The weather in {country} is sunny, 30°C with light breeze."


@function_tool
def get_crypto() -> str:
    """Return hardcoded crypto prices of 6 coins."""
    return (
        "💰 Crypto Prices:\n"
        "- Bitcoin (BTC): $67,000\n"
        "- Ethereum (ETH): $3,500\n"
        "- Binance Coin (BNB): $550\n"
        "- Solana (SOL): $145\n"
        "- Cardano (ADA): $0.45\n"
        "- Dogecoin (DOGE): $0.15"
    )

# -----------------------------
# Main Agent with tools
# -----------------------------

main_agent = Agent(
    name="MainAssistant",
    instructions="You are an assistant who can answer using tools: get_time, get_date, get_weather, get_crypto."
    
    ,
    model=model,
    tools=[get_time, get_date, get_weather, get_crypto]
)


config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



async def chat():
 

        # Run main agent using Runner
        result = await Runner.run(main_agent,"tell me the current date,and ,and current time,also give me the current rates of coin,and weather of italy ", run_config=config)

        print(result.final_output)
    




if __name__ == "__main__":
    asyncio.run(chat())
