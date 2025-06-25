from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
from pydantic import BaseModel

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    ),
)

# Output format
class Diagnosis(BaseModel):
    topic: str
    forward_to: str

#  triage agent
triage_agent = Agent(
    name="TriageAgent",
    instructions="Decide if this is about math or language. Return forward_to: 'MathAgent' or 'LangAgent'.",
    output_type=Diagnosis,
    model=model
)

# Specialist agents
math_agent = Agent(
    name="MathAgent",
    instructions="You are a math expert. Answer all math-related questions.",
    model=model
)

lang_agent = Agent(
    name="LangAgent",
    instructions="You are a language expert. Answer all language-related questions.",
    model=model
)

# User input goes to triage agent
first_result = Runner.run_sync(
    starting_agent=triage_agent,
    input="Tell me about verbs."
)

print("Final output:", first_result.final_output)
print(" Last agent was:", first_result.last_agent.name)  # This will print LangAgent

#  Next turn: re-use last agent directly
next_input = "What is a verb phrase?"

second_result = Runner.run_sync(
    starting_agent=first_result.last_agent,  # using LangAgent directly
    input=next_input
)

print("Next output:", second_result.final_output)
