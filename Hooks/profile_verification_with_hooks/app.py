from agents import (
    Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,
    RunHooks, RunContextWrapper, function_tool, AgentHooks
)
from dotenv import load_dotenv
from dataclasses import dataclass
from pydantic import BaseModel
from typing import TypeVar, Any
import os

# Generic type for context-based hooks
T = TypeVar("T")

# Load environment variables
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise KeyError("API key not found. Please set GEMINI_API_KEY in .env file")

# Initialize Gemini client and model
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# Define context model for user information
class MyContext(BaseModel):
    name: str
    age: str

# Tool function to return user info
@function_tool
def get_user_info(ctx: RunContextWrapper[MyContext]) -> str:
    return f"User name: {ctx.context.name}, Age: {ctx.context.age}"

# Runner-level hooks for start and end logging
@dataclass
class CustomRunHook(RunHooks[T]):
    async def on_agent_start(self, context: RunContextWrapper[T], agent: Agent[T]) -> None:
        print("[Runner] Agent execution started.")

    async def on_agent_end(self, context: RunContextWrapper[T], agent: Agent[T], output: Any) -> None:
        print("[Runner] Agent execution completed.")

# Agent-level hooks for tracking execution
@dataclass
class CustomAgentHook(AgentHooks[T]):
    async def on_start(self, context: RunContextWrapper[T], agent: Agent[T]) -> None:
        print(f"[Agent] Starting process for user: {context.context.name}")

    async def on_end(self, context: RunContextWrapper[T], agent: Agent[T], output: Any) -> None:
        print(f"[Agent] Process completed. Output: {output}")

# Create the agent instance
agent = Agent[MyContext](
    name="Assistant",
    instructions="Provide the user's name and age using the get_user_info tool.",
    model=model,
    tools=[get_user_info],
    hooks=CustomAgentHook[MyContext]()
)

# Prepare user context data
context = MyContext(name="Muhammad Fasih", age="10")

# Run the agent synchronously with runner hooks
result = Runner.run_sync(
    agent=agent,
    input="Please tell me my name and age.",
    context=context,
    hooks=CustomRunHook[MyContext]()
)

# Print final output from the agent
print("Final Output:", result.final_output)
