from agents import Agent, AgentHooks, RunContextWrapper
from dataclasses import dataclass
from pydantic import BaseModel
import asyncio

# Context
class MyContext(BaseModel):
    name: str

# Dummy Agents
agent_a = Agent(name="Agent A", instructions="Test A", model=None)
agent_b = Agent(name="Agent B", instructions="Test B", model=None)

# ❌ Wrong order: to_agent, context, from_agent (This will break)
@dataclass
class BrokenHook(AgentHooks[MyContext]):
    async def on_handoff(
        self,
        to_agent: Agent[MyContext],                       # ❌ Wrong position
        context: RunContextWrapper[MyContext],            # ❌ Wrong position
        from_agent: Agent[MyContext]                      # ❌ Wrong position
    ) -> None:
        print("❌ This should not run")

# Simulate context
context = RunContextWrapper(context=MyContext(name="Quratulain"))
hook = BrokenHook()

asyncio.run(hook.on_handoff(agent_b, context, agent_a))

# ❌ This will give TypeError due to positional mismatch
# Uncomment below to test the error

