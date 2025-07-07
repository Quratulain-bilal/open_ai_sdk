from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, enable_verbose_stdout_logging, ToolsToFinalOutputResult, RunContextWrapper, FunctionToolResult
from typing import List
from dotenv import load_dotenv
from rich import print
import os

enable_verbose_stdout_logging()
load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash",
)

@function_tool(docstring_style="sphinx", name_override="add", use_docstring_info=False)
def add_in_sphinx_style(a: int, b: int) -> int:
    """Add two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :returns: The sum of the two numbers.
    :rtype: int
    """
    return a + b

@function_tool(docstring_style="google", name_override="add")
def add_in_google_style(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

@function_tool(docstring_style="numpy", name_override="add")
def add_in_numpy_style(a: int, b: int) -> int:
    """Add two numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The sum of the two numbers.
    """
    return a + b

agent = Agent(
    name="Mathematician", 
    instructions="You are math expert", 
    model=model, 
    tools=[add_in_sphinx_style],
)
result = Runner.run_sync(starting_agent=agent, input="What is 2+2")
print(result.final_output)