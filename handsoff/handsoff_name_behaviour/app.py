from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, handoff, RunConfig, AgentHooks
from openai import AsyncOpenAI
from dotenv import load_dotenv
from rich import print
import os
import asyncio

load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY=os.environ.get("GEMINI_API_KEY")

config = RunConfig(
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=AsyncOpenAI(
            api_key=API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai"
        )
    )
)

class CustomMathAgentHooks(AgentHooks):
    async def on_start(self, context, agent):
        print("Math Agent is started.")

    async def on_end(self, context, agent, output):
        print("Math Agent is ended.")

#! Mene Agent ka name galat dia ha Physicist dia ha jabky agent Mathematician ha
math_expert_agent = Agent(
    name="Physicist", 
    instructions="You are an expert in mathematics. Solve problems accurately and explain your reasoning when needed.",
    handoff_description="Handles all mathematical questions and calculations.",
    hooks=CustomMathAgentHooks()
)

class CustomPhysicsAgentHooks(AgentHooks):
    async def on_start(self, context, agent):
        print("Physics Agent is started.")

    async def on_end(self, context, agent, output):
        print("Physics Agent is ended.")

#! Mene Agent ka name galat dia ha Mathematician dia ha jab ky agent jo ha wo Physicist ha
physics_expert_agent = Agent(
    name="Mathematician", 
    instructions="You are an expert in physics. Provide clear and precise answers to physics-related problems and concepts.",
    handoff_description="Handles all physics-related queries and theoretical explanations.",
    hooks=CustomPhysicsAgentHooks()
)

triage_agent = Agent(
    name="Traige Agent",
    instructions=(
        "You are a triage agent"
    ),
    handoffs=[physics_expert_agent, math_expert_agent]
)

physics_related_question="Tell me the basics concepts of Quantum Theory"
maths_related_question="Tell me the basics concepts of Integration in maths."

async def main():
    physics_result = await Runner.run(
        starting_agent=triage_agent,
        input=physics_related_question,
        run_config=config
    )
  
    print(physics_result)


asyncio.run(main())
