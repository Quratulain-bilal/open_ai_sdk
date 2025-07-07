from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool, RunConfig, enable_verbose_stdout_logging
import datetime
import os
from dotenv import load_dotenv


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


enable_verbose_stdout_logging()


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


@function_tool()
def get_time() -> str:
    return str(datetime.date.today())

@function_tool()
def weather_agent(city: str) -> str:
    return f"Today's weather is sunny in {city}"


trigger_agent = Agent(
    name="Trigger Agent",
    instructions="You are a helpful agent that provides time and weather updates.",
    model=model,
    tools=[get_time, weather_agent]
)


user_input = "Tell me the time and date and weather in Karachi"


result = Runner.run_sync(trigger_agent, user_input)


print(result.final_output)
