from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

# 🛠️ Define one tool using @function_tool with all possible parameters
@function_tool(
    name_override="simple_addition",  # tool ka naam hum khud define kar rahe hain
    description_override="This tool adds two numbers and returns the sum.",  # apna description de rahe hain
    docstring_style="google",  # docstring format (sphinx, google, numpy)
    use_docstring_info=True,  # docstring se hi parameter info li jaayegi
    hidden=False,  # tool hidden nahi hoga
    manual_schema=None  # khud ka schema nahi de rahe, auto banega
)
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The sum of the numbers
    """
    return a + b


agent = Agent(
    name="Math Helper",
    instructions="You help with basic math problems.",
    model=model,
    tools=[add_numbers]
)


result = Runner.run_sync(agent, input="What is 5 plus 3?")
print("🟢 Final Output:", result.final_output)
