
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
import os
from dotenv import load_dotenv
import asyncio
from dataclasses import dataclass

load_dotenv()
set_tracing_disabled(True)

API_KEY = "AIzaSyCSDFxp7bE4rgUwdMK4t4bTQg7R7xqnAxA"
if not API_KEY:
    raise ValueError("API key not found!")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)


@dataclass
class UserContext:
    name: str
    role: str


def generate_instructions(ctx, agent):
    user = ctx.context  

    if user.role == "admin":
        return (
            f"You are assisting Admin {ctx.context.name}. "
            "Provide detailed, technical responses with formal tone."
        )
    else:
        return (
            f"You are assisting Guest {ctx.context.name}. "
            "Provide short and simple answers."
        )

#  Agent with dynamic instructions function
agent = Agent[UserContext](
    name="RoleBasedHelper",
    model=model,
    instructions=generate_instructions  # 👈 Yeh function har run par instructions return karega
)

#  Main runner function
async def main():
    #  Change role to test "admin" vs "guest"
    context = UserContext(name="Quratulain", role="admin")
    # context = UserContext(name="Ali", role="guest")

    result = await Runner.run(
        starting_agent=agent,
        input="How do I create a secure login system?",
        context=context  #  Yeh context agent ko milega aur dynamic prompt me use hoga
    )

    print(" Final Output:")
    print(result.final_output)

# ⏯ Run the program
if __name__ == "__main__":
    asyncio.run(main())














