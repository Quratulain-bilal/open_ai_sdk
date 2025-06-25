🧠 last_agent 

📌 What is last_agent?
last_agent ek property hoti hai jo aapko batati hai kaunsa agent last mein run hua — yaani, final output dene se pehle ka aakhri agent kaun tha.

Yeh tab important hota hai jab aapka agent multiple handoffs karta ho — ya multi-agent workflow bana rahe ho.

🔍 Simple Definition:
last_agent = woh agent instance jo sabse aakhri mein run hua aur jisne final_output diya.

🧬 Lifecycle Flow (Step-by-step)

1️⃣ Runner.run() start hota hai with starting_agent  
2️⃣ Starting agent input receive karta hai  
3️⃣ Agar handoff hota hai, next agent run hota hai  
4️⃣ Loop chalta rehta hai jab tak koi final output na mile  
5️⃣ Last agent jisne output diya — wo set ho jata hai as `last_agent`



🚀 Step 1: First Input
first_input = "Tell me what is a verb"

first_result = Runner.run_sync(
    starting_agent=TriageAgent,
    input=first_input
)

print("📍 Final output of first turn:", first_result.final_output)
print("✅ Last agent that responded:", first_result.last_agent.name)

💬 Output:

📍 Final output of first turn: A verb is a word that shows action like "run", "eat", or "write".
✅ Last agent that responded: LangAgent

🚀 Step 2: Follow-up Input using last_agent

second_input = "Give me more examples of verbs."

second_result = Runner.run_sync(
    starting_agent=first_result.last_agent,  # Using LangAgent
    input=second_input
)

print("📘 Second output (follow-up):", second_result.final_output)
💬 Output:

📘 Second output (follow-up): Sure! Examples of verbs include: jump, sleep, write, talk, and read.
✅ Summary (Lifecycle + Flow):
Step	Action
1️⃣	User sends "Tell me what is a verb"
2️⃣	TriageAgent sees "verb" → hands off to LangAgent
3️⃣	LangAgent replies with grammar answer
4️⃣	SDK tracks last_agent = LangAgent
5️⃣	User follow-up "More examples" → goes direct to LangAgent

C



















💬 Output: