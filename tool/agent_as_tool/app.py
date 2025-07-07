from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, enable_verbose_stdout_logging
from dotenv import load_dotenv
from rich import print
import os

# enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY=os.environ.get("GEMINI_API_KEY")

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
)

english_agent = Agent(
    name="English Linguistic",
    instructions="You are expert in English language",
    model=model
)

urdu_agent = Agent(
    name="Urdu Linguistic",
    instructions="You are expert in Urdu language",
    model=model
)

orchestrator_agent=Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        english_agent.as_tool(
            tool_name="translate_to_english",
            tool_description="Translate the user's message to English"
        ),
        urdu_agent.as_tool(
            tool_name="translate_to_urdu",
            tool_description="Translate the user's message to Urdu",
        )
    ],
    model=model
)

result = Runner.run_sync(
    starting_agent=orchestrator_agent,
    input="'tum kia kar rahy ho', translate it to english"
)

print(result.final_output)

