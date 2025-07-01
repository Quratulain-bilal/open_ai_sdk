# app.py

from agents import Agent, RunContextWrapper, Runner, AgentHooks
from openai import AsyncOpenAI, OpenAIChatCompletionsModel
from dataclasses import dataclass
from pydantic import BaseModel
from typing import Any
from rich import print
from rich.panel import Panel
from rich.console import Console
from dotenv import load_dotenv
import asyncio
import os

# 🔹 Load environment variables from .env
load_dotenv()

# 🔹 Setup Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise KeyError("Error 405: API key not found in environment.")

# 🔹 Gemini-compatible OpenAI Client
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 🔹 Gemini model wrapper
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# 🔹 Custom Context for Agent
class MyContext(BaseModel):
    user: str

# 🔹 Tool 1 - Greet
def greet(ctx: RunContextWrapper[MyContext]) -> str:
    return f"👋 Hello [bold blue]{ctx.context.user}[/bold blue] from [green]Agent A[/green]!"

# 🔹 Tool 2 - Farewell
def farewell(ctx: RunContextWrapper[MyContext]) -> str:
    return f"👋 Goodbye [bold magenta]{ctx.context.user}[/bold magenta] from [red]Agent B[/red]!"

# 🔹 Agent A Hooks
@dataclass
class AgentAHooks(AgentHooks[MyContext]):
    async def on_start(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext]) -> None:
        print(f"[green]🚀 Agent A Started for {context.context.user}[/green]")

    async def on_end(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext], output: Any) -> None:
        print(f"[green]✅ Agent A Ended[/green]")

    async def on_handoff(self, context: RunContextWrapper[MyContext], from_agent: Agent[MyContext], to_agent: Agent[MyContext]) -> None:
        print(f"[yellow]🤝 Handoff from Agent A to Agent B[/yellow]")

# 🔹 Agent B Hooks
@dataclass
class AgentBHooks(AgentHooks[MyContext]):
    async def on_start(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext]) -> None:
        print(f"[red]🚀 Agent B Started[/red]")

    async def on_end(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext], output: Any) -> None:
        print(f"[red]✅ Agent B Ended[/red]")

# 🔹 Define Agents using Gemini model
agent_a = Agent(
    name="Agent A",
    instructions="Greet the user and hand off to Agent B.",
    model=model,
    tools=[greet],
    hooks=AgentAHooks()
)

agent_b = Agent(
    name="Agent B",
    instructions="Say goodbye to the user.",
    model=model,
    tools=[farewell],
    hooks=AgentBHooks()
)

# 🔹 Runner setup
runner = Runner(
    agents=[agent_a, agent_b],
    max_steps=5
)

# 🔹 Main function to run the flow
async def main():
    ctx = MyContext(user="Quratulain")
    result = await runner.run(
        input="Start conversation",
        context=ctx
    )
    print(Panel.fit(str(result), title="🏁 Final Result"))

# 🔹 Run the app
if __name__ == "__main__":
    asyncio.run(main())
