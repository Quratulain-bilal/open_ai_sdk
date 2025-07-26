# handoff_example.py

from agents import Agent, Runner
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

# ✅ Billing Agent - will only handle billing-related queries
billing_agent = Agent(
    name="Billing Agent",
    instructions=prompt_with_handoff_instructions(
        "Aap ek billing expert ho. Aap sirf billing se related queries ka jawab do."
    )
)

# ✅ Support Agent - will only handle support-related queries
support_agent = Agent(
    name="Support Agent",
    instructions=prompt_with_handoff_instructions(
        "Aap ek support expert ho. Aap sirf support issues ka jawab do."
    )
)

# ✅ Runner - combines multiple agents
runner = Runner(agents=[billing_agent, support_agent])

# 🔍 User sends a support-related question
query = "Mujhe internet ka masla hai. Kya aap meri madad kar sakte hain?"

# 🧠 Run the query through the agents
response = runner.run(query)

# 📤 Show the result
print("🧾 Final Response:")
print(response)
