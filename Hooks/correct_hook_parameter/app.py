from agents import Agent, AgentHooks, RunContextWrapper
from dataclasses import dataclass
from pydantic import BaseModel

class MyContext(BaseModel):
    name: str

# Dummy agent
agent_a = Agent(name="Agent A", instructions="Test", model=None)
agent_b = Agent(name="Agent B", instructions="Test", model=None)

@dataclass
class MyHooks(AgentHooks[MyContext]):
    async def on_handoff(self, context: RunContextWrapper[MyContext], from_agent: Agent[MyContext], to_agent: Agent[MyContext]) -> None:
        print("✅ Correct order — no error")

# Simulate calling it
import asyncio

context = RunContextWrapper(context=MyContext(name="Quratulain"))
hooks = MyHooks()

# Call it manually to test
asyncio.run(hooks.on_handoff(context, agent_a, agent_b))  # ✅ Works
