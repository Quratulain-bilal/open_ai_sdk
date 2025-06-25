import asyncio
from agents import Agent, Runner, trace

async def main():
    agent = Agent(
        name="TravelAssistant",
        instructions="You are a concise and knowledgeable travel guide."
    )

    with trace(workflow_name="TravelConversation"):
        # First user input
        result = await Runner.run(agent, "What's the best time to visit Japan?")
        print(result.final_output)

        # Second input with conversation context
        next_input = result.to_input_list() + [{"role": "user", "content": "What cities are best in spring?"}]
        result = await Runner.run(agent, next_input)
        print(result.final_output)

        # Third input with continued context
        next_input = result.to_input_list() + [{"role": "user", "content": "Any festivals in Kyoto?"}]
        result = await Runner.run(agent, next_input)
        print(result.final_output)

asyncio.run(main())
