from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool, ModelSettings
import os
from dotenv import load_dotenv

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Tool with decorator
@function_tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny today."

# Agent with tool_choice = "auto", temperature = 0.6
weather_agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful weather assistant.",
    model=model,
    tools=[get_weather],
    model_settings=ModelSettings(
        tool_choice="auto",         # LLM will decide when to use tool
        temperature=0.6,            # Slight creativity/randomness
        max_tokens=500              # Optional limit on model response
    )
)

# User input
user_prompt = "What's the weather in Lahore?"

# Run agent with max_turns = 3
result = Runner.run_sync(
    starting_agent=weather_agent,
    input=user_prompt,
    max_turns=3  # <- Agent can only run up to 3 turns max
)

print(result.final_output)
