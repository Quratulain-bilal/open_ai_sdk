🔹 1. tool_choice = "auto" – LLM Automatically Decides Tool Call
Jab hum tool_choice ko "auto" par set karte hain ModelSettings ke andar, to iska matlab hota hai ke LLM (Large Language Model) khud decide karega ke user ke prompt ka jawab dene ke liye koi registered tool call karna hai ya sirf apni understanding se jawab generate karna hai.

🧠 Example Use Case:
Agar aapka prompt ho: "What's the weather in Lahore?"
Aur aap ne ek get_weather(city) tool register kiya hai, to LLM decide karega:
"Kya mujhe tool se data lena chahiye ya khud se reply banana chahiye?"

💡 Note:

Ye dynamic hota hai, har baar LLM ka response change bhi ho sakta hai based on temperature.

Agar tool clearly required nahi lagta, to LLM sirf apni knowledge se bhi reply de sakta hai.






🔹 2. temperature = 0.6 – Model Creativity Level
temperature ek hyperparameter hota hai jo model ki creativity ya randomness control karta hai.

Low temperature (e.g. 0.0) → model hamesha predictable aur boring jawab dega.

High temperature (e.g. 1.0) → model zyada creative ho sakta hai, kabhi kabhi irrelevant bhi.

Mid value like 0.6 → Balanced creativity — helpful, natural-sounding, aur useful answers.


"Agar aap chahte ho model har baar thoda alag lekin sahi jawab de to temperature 0.6 best choice hai."






🔹 3. max_turns = 3 – Limit Interaction Rounds
max_turns define karta hai ke ek agent kitne baar interaction (LLM ↔ tools ↔ LLM) kar sakta hai.
Har turn mein:
User msg → LLM response → tool call (if needed) → LLM final reply

✅ Example:

Turn 1: User ka prompt jata hai.

Turn 2: Tools se data aata hai.

Turn 3: Final response generate hota hai.

Agar max_turns=3, to agent is point par ruk jaata hai — infinite loop ya excessive processing se bachata hai.


"Agar aap chahte ho ke agent ka response zyada lamba na ho ya loop na banaye, to max_turns lagana zaroori hota hai."