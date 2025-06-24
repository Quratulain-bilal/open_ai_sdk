from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    RunContextWrapper,
    function_tool
)
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
set_tracing_disabled(disabled=True)


API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise KeyError("Error 405: API key not found")


client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

#  Custom Context Class with More Info
@dataclass
class UserInfo:
    name: str
    age: int
    email: str
    city: str
    country: str
    job_title: str
    experience_years: int

# 🛠️ Tool to Display Full User Info
@function_tool
async def fetch_user_details(ctx: RunContextWrapper[UserInfo]) -> str:
    '''
    Returns detailed user information.
    '''
    user = ctx.context  # UserInfo object
    return (
        f" Name: {user.name}\n"
        f" Age: {user.age} years\n"
        f" Email: {user.email}\n"
        f" City: {user.city}, {user.country}\n"
        f" Job Title: {user.job_title}\n"
        f" Experience: {user.experience_years} years"
    )

# 🚀 Main Function
async def main():
    # Context Data with More Fields
    user_info = UserInfo(
        name="Quratulain",
        age=24,
        email="anna@example.com",
        city="Karachi",
        country="Pakistan",
        job_title="AI Engineer",
        experience_years=2
    )

    # Agent Creation
    agent = Agent[UserInfo](
        name="Assistant",
        tools=[fetch_user_details],
        model=model,
    )

    # Run the Agent
    result = await Runner.run(
        starting_agent=agent,
        input="Tell me all the user information.",
        context=user_info,
    )

    # Print the Result
    print(result.final_output)

# ⏳ Entry Point
if __name__ == "__main__":
    asyncio.run(main())
