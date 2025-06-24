from agents import Agent, Runner, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import asyncio
import os


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


model = OpenAIChatCompletionsModel(
    model="models/gemini-pro",  # Gemini model name
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta"  # Gemini base URL
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
    result_stream = await Runner.run_stream(
        starting_agent=agent,
        input="Can you write me a poem about the moon?",
        max_turns=3
    )

    print("📝 Poem (Streaming):\n")

    async for event in result_stream.events():
        if event["type"] == "delta":
            print(event["delta"], end="", flush=True)

    print("\n\n✅ Done!")

# ✅ Run it
if __name__ == "__main__":
    asyncio.run(run_poem_stream())
