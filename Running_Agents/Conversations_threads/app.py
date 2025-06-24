import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


model = OpenAIChatCompletionsModel(
    model="models/gemini-pro",
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

#  Translator Agent
translator_agent = Agent(
    name="TranslatorAgent",
    instructions="Translate English sentences into Urdu.",
    model=model,
)

# Summary Agent
summary_agent = Agent(
    name="SummaryAgent",
    instructions="Summarize the user's previous message.",
    model=model,
)

#  Master Agent to handle both (not doing handoff here to keep it clean)
async def run_conversation_thread():
    print("🔁 Conversation Thread Starts\n")

    # 🔹 Turn 1: Translation
    turn1 = await Runner.run(
        starting_agent=translator_agent,
        input="Translate this: I love learning."
    )

    print(" Turn 1 Input: Translate this: I love learning.")
    print(" Turn 1 Output:", turn1.final_output, "\n")

    # 🔹 Turn 2: Now summarize the translation
    new_inputs = turn1.to_input_list() + ["Now summarize it."]
    turn2 = await Runner.run(
        starting_agent=summary_agent,
        input=new_inputs
    )

    print(" Turn 2 Input: Now summarize it.")
    print(" Turn 2 Output:", turn2.final_output)

#  Run
if __name__ == "__main__":
    asyncio.run(run_conversation_thread())
