from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool, RunConfig, enable_verbose_stdout_logging
import datetime
import os
from dotenv import load_dotenv

# 🌍 1. Load environment variable for API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 🔊 Enable logs to trace steps
enable_verbose_stdout_logging()

# 📡 2. External OpenAI client using Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 🤖 3. Gemini model config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ⚙️ 4. Global config for agent run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# 🔧 5. Tool 1: Get current date
@function_tool()
def get_time() -> str:
    return str(datetime.date.today())

# 🔧 6. Tool 2: Get weather in a city
@function_tool()
def weather_agent(city: str) -> str:
    return f"Today's weather is sunny in {city}"

# 🧠 7. Agent definition with both tools
trigger_agent = Agent(
    name="Trigger Agent",
    instructions="You are a helpful agent that provides time and weather updates.",
    model=model,
    tools=[get_time, weather_agent]
)

# 🧪 8. User sends input asking both tools
user_input = "Tell me the time and date and weather in Karachi"

# 🚀 9. Run the agent
result = Runner.run_sync(trigger_agent, user_input)

# 📤 10. Final natural language response from agent
print(result.final_output)
