Runner.run() Method Overview
Ye method ek AI workflow start karta hai using agent. Har parameter is journey ka ek important role play karta hai.

🧩 1. starting_agent
➤ Kya hai?
Ye wo main Agent object hai jo pehla kaam start karega.

➤ Kab use hota hai?
Sabse pehle.

Agent ke andar instructions hoti hain jaise:
"Tum ek poet ho", "Tum ek email writer ho" etc.

➤ Kyu zaroori hai?
Ye define karta hai ke pehla step kis AI brain se start hoga.

📌 Real-World Example:
“Writer Agent se kaam shuru karo.”

🧩 2. input
➤ Kya hai?
User ka pehla input.

Type: str ya list[TResponseInputItem]

➤ Kab use hota hai?
starting_agent ko input dene se sabse pehle use hota hai.

➤ Kyu zaroori hai?
Ye input agent ke brain ko trigger karta hai response generate karne ke liye.

📌 Example:
'Write an essay on AI'

🧩 3. context
➤ Kya hai?
Ek dataclass ya koi shared data object.

Memory jesa kaam karta hai.

➤ Kab use hota hai?
Har turn pe jab agent ya tool run hota hai, tab ye context unhe diya jata hai.

➤ Kyu zaroori hai?
Agar aapko shared values rakhni ho (like: user ID, previous messages), toh context kaam aata hai.

📌 Real-World Example:
“User is premium + prefers short answers.”

🧩 4. max_turns
➤ Kya hai?
Maximum allowed agent-tool turns.

➤ Kab use hota hai?
Loop start hota hai aur turn count hota hai:

agent → tool → agent = 1 turn

Repeat until output or turn limit

➤ Kyu zaroori hai?
Loop ko infinite chalte se bachane ke liye. Agar exceed kare to error: MaxTurnsExceeded

📌 Default: 20
🧩 5. hooks
➤ Kya hai?
Callbacks jo aapko lifecycle events ka live access dete hain.

➤ Kab use hota hai?
Jab agent/tool start ya end hota hai.

Errors aaye, input/output aaye — sab pe triggers.

➤ Kyu zaroori hai?
Logging, debugging, analytics, metrics sab ke liye perfect.

📌 Example:
class MyHooks(RunHooks):
    async def on_agent_start(...): pass
    async def on_tool_start(...): pass
🧩 6. run_config
➤ Kya hai?
Complete global settings ka package:

Model

Temperature

Tool provider

Tracing, etc.

➤ Kab use hota hai?
Jab model call hota hai, ya tool activate hota hai — ye config apply hota hai.

➤ Kyu zaroori hai?
API settings central rakhne ke liye taake har jagah se control mile.

📌 Example:
python
Copy
Edit
RunConfig(model=my_model, tracing_disabled=True)
🧩 7. previous_response_id
➤ Kya hai?
Agar aap Responses API use kar rahe ho (e.g. OpenAI official endpoint), ye parameter pichle response se thread ko continue karta hai.

➤ Kab use hota hai?
Jab OpenAI response thread based ho aur aap thread continuation karna chahein.

➤ Kyu zaroori hai?
Continuity maintain karne ke liye, jaise WhatsApp ya Gmail threads.

🔚 Output: RunResult
Jab loop finish hota hai (final output mil jata hai), toh RunResult return hota hai jisme:

final_output

inputs

tool_calls

handoff_history

guardrail_violations (if any)

