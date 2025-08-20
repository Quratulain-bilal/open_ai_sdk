from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, ModelSettings  
from agents.run import RunConfig  
from dotenv import load_dotenv  
from rich import print  
import os, asyncio

load_dotenv()  
set_tracing_disabled(disabled=True)  

API_KEY = os.environ.get("GEMINI_API_KEY")  
if not API_KEY:
    raise KeyError("Error 405: Does not found an api key")  

model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    )
)

model_settings_1 = ModelSettings(
    temperature=0.95,
    top_p=1.0,
    max_tokens=600,
    presence_penalty=0.6,
    tool_choice="none",
    parallel_tool_calls=False,
    truncation="auto",
    include_usage=True
)

model_settings_2 = ModelSettings(
    temperature=0.3,
    top_p=0.8,
    max_tokens=400,
    presence_penalty=0.0,
    tool_choice="auto",
    parallel_tool_calls=True,
    truncation="disabled",
    include_usage=True
)

model_settings_3 = ModelSettings(
    temperature=0.5,
    top_p=1.0,
    max_tokens=250,
    presence_penalty=0.1,
    tool_choice="required",
    parallel_tool_calls=True,
    truncation="auto",
    include_usage=True
)

config_1 = RunConfig(model=model, model_settings=model_settings_1)
config_2 = RunConfig(model=model, model_settings=model_settings_2)
config_3 = RunConfig(model=model, model_settings=model_settings_3)


agent_1 = Agent(
    name="StoryWriter",
    instructions="You are a creative story writer who writes engaging fantasy stories for kids.",
    model=model
)

agent_2 = Agent(
    name="TechTeacher",
    instructions="You are a calm technical assistant that explains programming concepts to beginners in very simple language.",
    model=model
)

agent_3 = Agent(
    name="LogicBot",
    instructions="You are a reasoning expert. Solve logic puzzles step-by-step with explanations.",
    model=model
)


async def main():
    result_1, result_2, result_3 = await asyncio.gather (
        Runner.run(
            starting_agent=agent_1, 
            input="Write a magical story about a rabbit who can fly", 
            run_config=config_1
        ),
        Runner.run(
            starting_agent=agent_2, 
            input="Explain what a Python decorator is with code example", 
            run_config=config_2
        ),
        Runner.run(
            starting_agent=agent_3, 
            input="If all humans are mammals and all mammals are animals, are all humans animals?", run_config=config_3
        )
    )

   
    print("SCENARIO 1 OUTPUT:")
    print(result_1.final_output)
    
    print("SCENARIO 2 OUTPUT:")
    print(result_2.final_output)

    print("SCENARIO 3 OUTPUT:")
    print(result_3.final_output)

asyncio.run(main())
