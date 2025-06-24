🔍 What is Context? (Context kya hota hai?)
Context ek "intelligent data bag" hota hai — jismein woh har wo information hoti hai jo agent, tools ya handoff ko chahiye hoti hai during execution.

📦 Think of context like a "global state object" jo:

Har agent ko diya jata hai

Har tool function access kar sakta hai

Workflow ke dauran share hota hai — bina duplicate coding ke

🧠 Official Definition:
“Context is a dependency-injection tool: it's an object you create and pass to Runner.run(), that is passed to every agent, tool, handoff etc. It serves as a grab bag of dependencies and state.”

Matlab:

Aap koi bhi custom object (like dict, class) create karke context ke tor pe de sakte ho.

Ye shared hota hai across agents & tools.

🏗️ Real Life Analogy:
Imagine aik restaurant:

Chef (agent) ko pata hona chahiye:

customer ka naam

dietary preferences

table number

Waiter ye info deta hai = context 🎯

Agar context nahi mila → chef confuse hoga → result: ghalat khana

⚙️ Context Lifecycle Breakdown (Step-by-Step)
✅ Step 1: Create a context object
Yeh custom class, dictionary, ya kisi bhi Python object ka instance ho sakta hai.

python
Copy
Edit
context = {
  "user_name": "Ali",
  "role": "admin",
  "language": "ur"
}
✅ Step 2: Pass context to Runner.run()
python
Copy
Edit
Runner.run_sync(
  starting_agent=my_agent,
  input="Start session",
  context=context  # 💡 yahan context pass hota hai
)
📌 Ab yeh context har tool aur agent tak propagate ho jata hai.

✅ Step 3: Agent accesses context
Agar aap agent ke andar dynamic_instructions ya tools mein ho, to aapko context milta hai via:

python
Copy
Edit
def dynamic_instructions(agent, context):
    if context["role"] == "admin":
        return "Speak formally."
✅ Step 4: Tool function gets context via RunContextWrapper
python
Copy
Edit
@function_tool()
def get_user_name(ctx: RunContextWrapper[dict]) -> str:
    return f"Hello, {ctx.context['user_name']}!"
RunContextWrapper → yeh ek safe wrapper hai jo tool ko context access karne deta hai.

✅ Step 5: Context flows through handoffs and all internal logic
Agar aap multiple agents ya tools handoff kar rahe ho:

context unchanged rehta hai

Har new agent ko wahi context milta hai

Is tarah data duplication nahi hoti

🔁 Use Case Scenarios
Situation	Context Example
Multi-language app	"language": "en" or "ur"
Role-based behavior	"role": "admin" or "guest"
Dynamic greetings	"user_name": "Ali"
Personalization	"theme": "dark", "timezone": "PKT"
Live app state	"session_id": "abc123"

🧬 Inner Mechanism: How Context Internally Flows
text
Copy
Edit
[You call Runner.run(..., context=your_context)]
        ↓
[Context is passed to agent.invoke(...)]
        ↓
[Agent passes it to tools, instructions, and sub-agents]
        ↓
[Each tool wraps it via RunContextWrapper]
        ↓
[Final output generated → still includes context]
🧪 Agent Generic Context Type
Agents can be generic like:

python
Copy
Edit
Agent[dict]  # if using dictionary
Agent[MyAppContext]  # if using custom class
This makes SDK:

Strongly typed

Context-aware

Easily testable

✅ Benefits of Using Context
Feature	Benefit
🧠 Smart AI	Agent acts according to role, user, etc.
🧼 Clean Design	No need to pass every value again and again
🔀 Modular	Different agents, same context
🚀 Scalable	Supports large apps with consistent data
🔐 Secure	Controlled injection of critical info

📌 Summary: Context in One Glance
Topic	Details
What?	Shared data object
Why?	Pass info like user, role, settings
Where?	Passed to Runner.run()
Accessed via	Direct in agent, RunContextWrapper in tools
Types	dict, class, any Python object
Flow	One-time inject → accessible everywhere in run
Benefit	Clean code, dynamic behavior, testability