🔁 Runner.run() 
 method aik intelligent looped workflow chalata hai jahan ek AI Agent apne tools, context, aur instructions ke sath response generate karta hai — jab tak final output nahi milta. Har parameter is loop ke kisi important gear ki tarah hota hai.

🧩 1. starting_agent — The Brain That Begins the Workflow
Kya hai?
Yeh agent woh function hai jo sabse pehle trigger hota hai. Ismein instructions hoti hain jo model ko batati hain ke is input ka kya karna hai.

Internally:
Jab Runner.run() start hota hai, sabse pehle starting_agent.__call__() hota hai — jisme input + context pass hota hai.

Lifecycle:

Agent initializes

Instructions bind hoti hain

Input milta hai

Model call hota hai (based on run_config)

Output ya tool ya handoff decide hota hai

📌 Agar handoff call aata hai, to loop dubara chalta hai naye agent ke sath.

🧩 2. input — The Trigger
Kya hai?
User ka original prompt ya structured message list.

Lifecycle:

Pehle input agent ko diya jata hai

Agent isey LLM ko deta hai

Response ya reasoning ya toolCall wapas milta hai

Result RunResult mein save hota hai

📌 Ye input baad mein result.input property se bhi access ho sakta hai.

🧩 3. context — The Memory Bank
Kya hai?
Aapka custom Python object ya dataclass — jisme user state, app settings, ID, etc. ho sakta hai.

Lifecycle:

Start mein Runner.run() ko diya jata hai

Har tool/agent ke ctx: RunContextWrapper[YourContextType] mein yeh wrap ho kar jata hai

Tool ya agent is context se shared values access karta hai

📌 Data safely pass hota hai har step mein bina global variable ke.

🧩 4. max_turns — Infinite Loop Se Protection
Kya hai?
Maximum baar agent-tool-agent loop chal sakta hai. Default: 20

Lifecycle:

Har AI + Tool combination ek turn count hota hai

Har iteration pe count increase hota hai

Agar exceed ho jaye → MaxTurnsExceeded exception throw hoti hai

📌 Agent stuck na ho, isliye yeh cap zaroori hai.

🧩 5. hooks — Live Telemetry (Debug, Logs, Events)
Kya hai?
Aapka custom event handler object (RunHooks subclass) jo lifecycle pe trigger hota hai.

Lifecycle:

on_agent_start, on_tool_start, on_agent_end, on_error, etc.

Har lifecycle phase mein aap custom logging, tracking, alerts set kar sakte ho

📌 Production apps mein yeh observability aur control ke liye important hota hai.

🧩 6. run_config — The Engine Settings
Kya hai?
Model config, base_url, temperature, tool_behavior etc. ka centralized package.

Lifecycle:

Jab model call hota hai (LLM ya tool), to config apply hota hai

RunConfig.model, RunConfig.model_provider, RunConfig.tracing_disabled etc.

📌 Aap model=model_obj dekar Gemini ya OpenAI easily switch kar sakte ho.

🧩 7. previous_response_id — Conversation Continuity
Kya hai?
Agar aap thread-based LLM (like OpenAI Chat API) use kar rahe ho, yeh thread continuation ke liye hota hai.

Lifecycle:

Agar pehle se koi conversation chal rahi ho

LLM ko yeh ID dene par woh pichla context automatically load kar leta hai

📌 Ye advanced use cases mein helpful hai, jaise chat agents with memory.

🔚 Final Output: RunResult
Jab agent run ka loop complete hota hai, aapko milta hai:

Property	Kya deta hai
final_output	Last agent ka result (str ya object)
input	Original user input
last_agent	Last executed agent (useful for follow-up)
new_items	Sab events: messages, tool calls, reasoning
raw_responses	Raw LLM API response
to_input_list()	Ye output ko next run ke input mein convert karta hai

🧠 Summary of Internal Flow
mermaid
Copy
Edit
graph TD
A[User Input] --> B[starting_agent invoked]
B --> C[Model called with input]
C --> D[Tool Call or Output or Handoff]
D -->|Tool| E[Run tool & return result]
D -->|Handoff| F[Next agent runs]
D -->|Output| G[Return Final Output]
E --> B
F --> B
