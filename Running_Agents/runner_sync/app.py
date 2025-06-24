from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

# 1. Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Setup Gemini client
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. Setup model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)

# 4. Create Agent
greeter_agent = Agent(
    name="Greeter",
    instructions="You are a friendly AI assistant that greets users politely and warmly.",
    model=model
)

# 5. Run the agent using Runner.run_sync
response = Runner.run_sync(
    greeter_agent,
    input="Say hello to Quratulain Shah."
)

# 6. Print the final output
print(" Agent Response:", response.final_output)
