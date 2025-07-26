📘 README: OpenAI Agents SDK — Handoff Mechanism Explained
1. Introductions: kya hai "handoff"?
“Handoff” ek mechanism hai jisme Agent A apna task Agent B ko transfer (handoff) kar sakta hai. Yeh tab useful hai jab multiple specialized agents milkar kaam karte hain — jaise invoice, weather, translation etc. 



2. Core Components (Technical)
Agent aur Runner
Agent: Ek LLM-based model hota hai instructions aur tools ke saath defined.

Runner: Execution engine jo loop chalata hai—agent output, tool calls, aur hand-offs detect karta hai 
OpenAI GitHub
+6
OpenAI GitHub
+6
GitHub
+6
.

Handoff Configuration
handoff() function jo dynamic tool banata hai agent-to-agent delegation ke liye.

Params include:

agent: target agent object.

tool_name_override, tool_description_override

on_handoff: callback jab handoff trigger hota hai.

input_type: schema of data passed.

input_filter: sab se important — ye decide karta hai history ka kon sa hissa next agent ko milta hai 
Reddit
+6
OpenAI GitHub
+6
GitHub
+6
.

Input Filters
Yeh function HandoffInputData object leta hai (jis mein full conversation history hoti hai) aur return karta hai modified HandoffInputData.

Built-in filters include:

remove_all_tools

remove_system_messages

remove_agent_messages

Custom filters bhi define kiye ja sakte hain—for example sirf user messages pass karna 


7.  Important Points 

Handoff kyun?	Multiple agents specialization ke liye tasks divide karna.
input_filter kyun?	Sub-agent ko confusions se bachana. Sirf relevant user context pass karna.
Custom filter banana?	Python function HandoffInputData -> HandoffInputData. Example diya above.
Runner-level vs handoff-level?	Handoff-level filter ek specific transfer ke liye hota hai; Runner-level globally saare handoffs pe automatic lagta hai.
Built-in filters kya hain?	remove_all_tools, remove_system_messages, remove_agent_messages etc.



🌟 Scenario: Simple Agent Loop with Handoff
Humare paas:

MainAgent

MathAgent (sub-agent for math problems)

Ek Runner jo loop chalayega

User message: "2 + 2 kya hota hai?"

🔁 Agent Loop — Step-by-Step Turns
🔹 Turn 1: User → Main Agent
Input:
User ne input diya:

arduino
Copy
Edit
"2 + 2 kya hota hai?"
System Prompt:
Runner internally LLM ko prompt deta hai:

css
Copy
Edit
[System prompt] + [MainAgent instructions] + [User input]
Yani:

"Tum ek Triage Agent ho. User ne ye poocha hai: 2 + 2 kya hota hai? Agar ye math se related hai to MathAgent ko handoff karo."

LLM (OpenAI) ko ye context diya jata hai aur woh decision leta hai:

Agar wo khud jawab de sakta hai → final_output deta hai

Agar usay lagta hai math_agent behtar karega → tool call karega: "transfer_to_math_agent"

🔹 Turn 2: Main Agent ne Tool (handoff) Call kiya
Ab Runner dekh raha hai ke:

Ye tool call ek handoff tool hai (transfer_to_math_agent)

To ab:

input_filter lagta hai (agar defined ho)

Filtered conversation MathAgent ko bhej di jati hai

🔹 Turn 3: Sub-Agent (MathAgent) → LLM Call
Ab same process repeat hota hai, lekin ab MathAgent ke instructions ke sath:

System Prompt to LLM:

css
Copy
Edit
[System prompt] + [MathAgent instructions] + [Filtered User message]
Yani:

"Tum ek Math Expert ho. User ne poocha: 2 + 2 kya hota hai?"

LLM Output:

arduino
Copy
Edit
"2 + 2 = 4"
Ye output jab final_output ke form mein milta hai → to loop stop ho jata hai.

🔚 Final Step: Runner Return karta hai
Runner final_output ko return karta hai:

Final Answer:

arduino
Copy
Edit
"2 + 2 = 4"
🔁 Agar Multiple Handoff ho?
Same loop repeat hota hai:

AgentA → handoff → AgentB

AgentB → handoff → AgentC

AgentC → final_output deta hai

Jab tak kisi agent ka output "final_output" na ho, loop chalta rehta hai. Ye multi-layered recursive loop hai.

📌 Important Concepts Summary
Concept	Explanation
Turn?	Ek round jisme agent ka LLM call hota hai
System Prompt?	Agent ke rules + user message LLM ko diya jata hai
Tool Call?	LLM jab kisi tool ko call karta hai (including handoff)
Handoff Tool?	Ek tool jo doosre agent ko control deta hai
Input Filter?	Conversation ka woh hissa jo sub-agent ko diya jata hai
Final Output?	Jab agent direct answer de deta hai, aur loop ruk jata hai
Runner Loop	Ye sab steps manage karta hai jab tak final answer na milay

