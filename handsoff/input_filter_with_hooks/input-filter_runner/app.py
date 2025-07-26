from agents.handoffs import HandoffInputData
from dotenv import load_dotenv
from typing import TypeVar
from rich import print
import os
from agents import Agent, Runner, handoff, HandoffInputData, RunConfig,OpenAIChatCompletionsModel,set_tracing_disabled,AsyncOpenAI

set_tracing_disabled(disabled=True)
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
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# Yeh function tab chalta hai jab kisi agent ko handoff hone wala ho.
# Agar user ka input "weather" shamil karta ho tabhi handoff allow karo, warna data wapas bhej do without handoff.

def handoff_filter(data: HandoffInputData) -> HandoffInputData:
    input_text = str(data.input_history).lower()  # Input history string bana ke lowercase mein
    if "weather" in input_text:
        print("[green]Input contains 'weather', allowing handoff...[/green]")
        return data  # Allow handoff
    else:
        print("[red] Input doesn't contain 'weather', blocking handoff...[/red]")
        return HandoffInputData(  # Empty handoff data return kar rahe
            input_history=data.input_history,
            pre_handoff_items=(),
            new_items=()
        )
#sub agent

weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a weather expert. Answer only if the user asks about weather-related queries.",
    model=model,
    handoff_description="Handles weather-related questions like temperature, forecast, rain etc."
)

#main agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="If the query is about weather, hand it off to the Weather Agent. Otherwise, try to answer it.",
    handoffs=[weather_agent],
    model=model
)



result = Runner.run_sync(
    starting_agent=triage_agent,
    input="what is physics.",
    run_config=RunConfig(handoff_input_filter=handoff_filter)
)

#* Final Output Print
print("[bold blue]\nFinal Output:[/bold blue]", result.final_output)