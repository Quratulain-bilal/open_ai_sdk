from pydantic import BaseModel
from agents import Agent, Runner

# Define structured output format
class MotivationOutput(BaseModel):
    quote: str
    author: str

# Agent with structured output
structured_agent = Agent(
    name="StructuredWriter",
    instructions="Return a motivational quote as JSON with quote and author fields.",
    output_type=MotivationOutput
)

# Run the agent
result = Runner.run_sync(
    starting_agent=structured_agent,
    input="Give me a motivational quote."
)

# Output is a Pydantic object
print(" Quote:", result.final_output.quote)
print("Author:", result.final_output.author)
