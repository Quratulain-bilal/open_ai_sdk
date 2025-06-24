📘 Dynamic Instructions in OpenAI Agents SDK


🧠 Concept Introduction (Basic Idea)
🔹 What are Instructions?
Agent ko guide karne ke liye hum usay ek prompt dete hain — isay instructions kehte hain.

Ye instructions hoti hain:

Agent ka tone, role, aur behavior define karti hain.

LLM ka thinking pattern inhi pe depend karta hai.

🔹 Fixed vs Dynamic Instructions
✅ Fixed Instructions (Normal Tarika)
Aap direct prompt de dete ho Agent create karte waqt:

python
Copy
Edit
agent = Agent(
    name="Helper",
    instructions="You are a helpful assistant.",
    model=model
)
Har run mein yehi static prompt use hota hai.

Har user ke liye same behavior.

No context-awareness.

🔄 Dynamic Instructions (Context-Aware Prompt)
Kabhi aapko chahiye ke:

Prompt har baar context ke mutabiq change ho.

Har user ke liye alag instructions generate ho.

Prompt personalize ho based on:

User role (admin/guest)

User name

Location, language, settings etc.

🧬 How It Works Internally – Lifecycle Breakdown
Let’s break it down step by step:

✅ Step 1: Agent receives dynamic function instead of static string
python
Copy
Edit
def dynamic_instructions(agent, context):
    if context.get("user") == "admin":
        return "You are a professional assistant. Respond formally."
    elif context.get("user") == "guest":
        return "You are a friendly assistant. Be casual and polite."
    else:
        return "You are a helpful assistant."

agent = Agent(
    name="SmartAgent",
    instructions=dynamic_instructions,
    model=model
)
🧠 Behind the scenes:
instructions parameter is a callable (function) now.

SDK checks: Is it a str or a function?

If function → call it at runtime with agent & context.

✅ Step 2: You run the agent using Runner
python
Copy
Edit
Runner.run_sync(agent, input="Hello!", context={"user": "admin"})
✅ Step 3: Instructions Function Gets Called Dynamically
Under the hood:

agent.instructions(agent, context) is invoked.

Jo return aata hai, wo final prompt ban jata hai.

python
Copy
Edit
# Internally:
instructions_prompt = agent.instructions(agent, context)
This prompt is passed to the LLM along with input.

✅ Step 4: LLM Runs Based on Dynamic Prompt
Now the agent talks to LLM using this generated prompt.

So agar context mein user = "Ali" ho, the prompt might be:

“You are a friendly assistant. Call the user by name Ali.”

✅ Step 5: Output Generated → User gets context-aware answer
📊 Visual Flow (Mentally)
text
Copy
Edit
[Runner.run()] 
   ↓
[Agent receives input + context]
   ↓
[Instructions Function is called → Returns dynamic prompt]
   ↓
[LLM is called with final prompt + input]
   ↓
[LLM generates answer → Output shown]
✅ Use Cases (Kahan Useful Hai)
Scenario	Dynamic Behavior
🤖 Chatbot	Greet user by name, adjust tone
🔐 Role-based UI	Admins get strict response, users friendly
🧪 Testing	Inject instructions based on test case
🗣️ Multi-lingual	Prompt generated based on preferred language

⚙️ Advanced Version – Async Function as Instructions
Instructions function async bhi ho sakti hai:

python
Copy
Edit
async def dynamic_instructions(agent, context):
    user_type = await get_user_type_from_api(context["user_id"])
    return f"You are a bot for a {user_type} user."

agent = Agent(instructions=dynamic_instructions, model=model)
SDK handles this await under the hood.

It awaits the instructions function if it's async.

❓ FAQ Section
Q: Kya har bar instructions function run hoti hai?
✅ Haan, har Runner.run() ke time pe instructions regenerate hoti hain.

Q: Kya context required hai?
📦 Nahi — but recommended. You can pass custom context as dict.

Q: Kya ye tool_choice ke saath kaam karta hai?
🧠 Bilkul. Dono parallel features hain.

✅ Summary (In Short)
Feature	Explanation
instructions="..."	Static instructions (default)
instructions=function	Dynamic prompt generation
Accepts context?	✅ Yes
Async supported?	✅ Yes
Benefit	Personalized, context-aware behavior
Lifecycle?	Run-time evaluated for every Runner.run()