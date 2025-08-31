

import os, asyncio
from dataclasses import dataclass
from typing import Any, TypeVar
from dotenv import load_dotenv
from pydantic import BaseModel

from agents import(
    Agent,
    AgentHooks,
    FunctionTool,
    RunConfig,
    RunContextWrapper,
    RunHooks,
    Runner,
    AsyncOpenAI, 
    OpenAIChatCompletionsModel,
    function_tool,  
    set_tracing_disabled,
    )



load_dotenv()
# enable_verbose_stdout_logging()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
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
    tracing_disabled=set_tracing_disabled(True)  
)


# Agent
agent = Agent(
    name="PoemAgent",
    instructions="You are a poetic assistant. Always respond in the form of a beautiful short poem.",
    model=model,
    tools=[]  # No tools needed
)

# Streaming runner (Only delta handling)
async def run_poem_stream():
    print("👧 User: Can you write me a poem about the moon?\n")

    result_stream = Runner.run_streamed(
        starting_agent=agent,
        input="Can you write me a poem about the moon?",
        max_turns=3
    )

    print("📝 Poem (Streaming):\n")
    
    async for event in result_stream.stream_events():
        if event.type == "raw_response_event":
            if hasattr(event.data, "delta") and event.data.delta:
                print(event.data.delta, end="", flush=True)


    print("\n\n✅ Done!")

asyncio.run(run_poem_stream())
