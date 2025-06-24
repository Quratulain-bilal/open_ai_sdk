#  Required Imports
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from pydantic import BaseModel, EmailStr
import os
from dotenv import load_dotenv
import asyncio

#  Load API Key
load_dotenv()
set_tracing_disabled(True)

API_KEY = os.getenv("GEMINI_API_KEY")
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

#  Pydantic Model (Structured Output)
class UserInfo(BaseModel):
    name: str
    age: int
    email: EmailStr

#  Create Agent with Pydantic Output
agent = Agent(
    name="UserInfoAgent",
    model=model,
    output_type=UserInfo  #  agent se expected output type
)

#  Run Agent with Input
async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="My name is Quratulain Shah, I'm 24 years old and my email is qurat@example.com.",
    )

    user: UserInfo = result.final_output

    print(" Structured Output:")
    print(f"Name: {user.name}")
    print(f"Age: {user.age}")
    print(f"Email: {user.email}")

if __name__ == "__main__":
    asyncio.run(main())
