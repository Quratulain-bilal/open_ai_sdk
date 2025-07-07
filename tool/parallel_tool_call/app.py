from agents import Agent, function_tool, Runner, ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client,
)

@function_tool()
def get_date(city: str, format: str) -> str:
    return f"Date in {city} is: {datetime.date.today()}"

@function_tool()
def get_time(city: str, timezone: str) -> str:
    return f"Time in {city} is: {datetime.datetime.now().strftime('%H:%M:%S')}"

agent = Agent(
    name="Parallel Agent",
    instructions="Give both time and date together if asked.",
    model=model,
    tools=[get_date, get_time],
    model_settings=ModelSettings(
        tool_choice="auto",
        parallel_tool_calls=True,
        max_turns=3
    )
)

result = Runner.run_sync(agent, "Tell me the time and date in Lahore")
print(result.final_output)
