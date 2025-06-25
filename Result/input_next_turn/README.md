🧠 input-next-tern() 
📌 Kya hota hai?
to_input_list() ek utility method hai jo RunResult ke upar call hota hai. Iska kaam hai:
“Current run ke sab outputs ko, original input ke sath combine karke ek naya input list banana.”

🔁 Life Cycle Samjho Step-by-Step
Start Input
Jab aap Runner.run() ya Runner.run_sync() call karte ho, ek input string ya list jati hai agent ko.

Agent Processing
Agent input le kar:

Message generate karta hai (LLM reply)

Tool call karta hai

Handoff karta hai

Reasoning deta hai

In sabko SDK internally RunItems ke form mein track karta hai.

Result Formation
Jab run complete hota hai, ye sab RunItems result.new_items mein hotay hain:

MessageOutputItem

ToolCallItem

ToolCallOutputItem

HandoffCallItem

HandoffOutputItem

ReasoningItem

to_input_list() Call
Jab aap result.to_input_list() call karte ho:

Ye original input ko leta hai

new_items se relevant messages ko extract karta hai

Sab ko combine karke ek clean structured input list banata hai

Next Agent Run Ready
Ab aap ye input list directly agle Runner.run() mein use kar sakte ho.
Multi-turn chat ke liye perfect hota hai.



🧪  Example 

result = Runner.run_sync(agent, input="Hello!")
next_input = result.to_input_list()
next_input.append({"role": "user", "content": "Continue..."})
Runner.run_sync(agent, input=next_input)
Yahan:

First turn ka agent output to_input_list() se carry hua

New user message append hua

Second run ke liye complete context ready ho gaya