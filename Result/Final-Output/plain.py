from agents import Agent, Runner

# Agent with plain text instructions, no output_type
plain_agent = Agent(
    name="SimpleWriter",
    instructions="Write a short motivational quote."
)

# Run 
result = Runner.run_sync(
    starting_agent=plain_agent,
    input="I feel tired today."
)

# Output is plain string
print("Final Output (No output_type):", result.final_output)
