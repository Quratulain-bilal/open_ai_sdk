import asyncio
from dotenv import load_dotenv
import os
import math
import datetime

from agents import function_tool, Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel,handoff

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"



external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

from datetime import datetime

@function_tool
def get_datetime(format: str = "default"):
    """
    Returns current date/time in different formats.
    Options for 'format': 
    - 'date' (YYYY-MM-DD)
    - 'time' (HH:MM:SS)
    - 'full' (YYYY-MM-DD HH:MM:SS)
    - 'default' (Day, DD Month YYYY, HH:MM:SS)
    """
    now = datetime.now()
    
    if format == "date":
        return f"Current Date: {now.strftime('%Y-%m-%d')}"
    elif format == "time":
        return f"Current Time: {now.strftime('%H:%M:%S')}"
    elif format == "full":
        return f"Current DateTime: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    else:
        return f"Today is: {now.strftime('%A, %d %B %Y, %H:%M:%S')}"

@function_tool
def reverse_text(text: str):
    """Reverses any text. Example: 'hello' -> 'olleh'"""
    print("Annie the best coder")
    return text[::-1]



@function_tool
def get_weather(country: str) -> str:
    """Returns hardcoded weather info for a given country."""
    print("Annie the best coder again")
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



python_expert = Agent(
    name="PythonExpert",
    instructions="""You are a **Senior Python Developer**. Your task is to:
    1. **Explain Python concepts** clearly with examples.
    3. **Write efficient code** for any problem (e.g., password generator, reverse sentence).
    5. **Give real-world analogies** for complex topics.
    - MUST provide executable code snippets for all Python-related tasks.
    - Use tools (get_crypto, get_datetime, reverse_text, get_weather) when query requires them and include their results directly.
    - Do not skip any task mentioned in the query.
    **Example Format:**
    ```python
    # Code Example
    def greet(name):
        return f"Hello, {name}!"
    """,
     tools=[get_crypto, get_datetime, reverse_text, get_weather],
   model=model
)

translator_agent = Agent(
    name="SimpleTranslator",
    instructions="""You are a bilingual translator. Follow these rules:
1. **Translate**: Hindi ↔ English (Roman/Unicode)
2. **Detection**: Auto-detect input language
3. **Short Texts**: Handle 1-2 sentences max
4. **Style**: Use friendly tone with emojis 😊

**Examples of Good Translations:**
- "नमस्ते" → "Hello 👋"
- "How are you?" → "आप कैसे हैं? 🤗"
- "मैं ठीक हूँ" → "I'm fine 👍"

**Avoid:**
- Long paragraphs
- Slang/Profanity""",
    model=model  
)

def translator_on_handoff(wrapper):
    print("Translator agent runs")

def python_expert_on_handoff(wrapper):
    print("Python expert agent runs")

main_agent = Agent(
    name="MainAssistant",
    instructions=("You are the main assistant. You have two specialist sub-agents:\n"
               "1. python_expert"
               "2. translator agent"
               "Your responsibilities:\n"
               "- Identify if query is python or translation related\n"
               "- Delegate to the appropriate sub-agent\n"
              " Delegate to the appropriate sub-agent\n'"
               "- Present final answers clearly\n"
               "**IMPORTANT**: You MUST call tool PARALLERLY if user query is asking for MULTIPLE of them"
              ),
     tools=[get_crypto, get_datetime, reverse_text, get_weather],
    model=model,
    handoffs=[
        handoff(
            agent=translator_agent,
            on_handoff=translator_on_handoff,
        ),
        handoff(
            agent=python_expert,
            on_handoff=python_expert_on_handoff
        ),
    ]
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

result = Runner.run_sync(main_agent,"give me the coin rates, and translate this into hindhi i am from mansehra , and reverse this sentense she is a girl, and tell me the time and current date,translate this in hindi i am frontened develope,define list and tupples",
                run_config=config)

print(result.final_output)
