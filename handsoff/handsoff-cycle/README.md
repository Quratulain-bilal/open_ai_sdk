🔁 Project Scenario Overview: Handoff Cycle Using Filters
Tumhara goal yeh hai:

❓ Jab koi input HistoryAgent ko diya jaye, agar woh question history ka nahi hai, to woh ScienceAgent ko handoff kare. Uske baad agar woh science ka nahi hai to MathAgent ko. Aur agar woh math ka nahi hai to HistoryAgent ko dobara.

Yeh ek cycle create karta hai: History → Science → Math → History → ...

⚙️ Key Concepts Samajhne Wale
✅ 1. Agent
Agent aik AI logic ya expert hai, jaise: HistoryAgent, ScienceAgent, MathAgent.

Har agent ka role hota hai specific domain ke questions solve karna.

Agar kisi question ka jawab us ke paas nahi hai to woh kisi aur agent ko forward karta hai.

✅ 2. Handoff
Jab ek agent kisi aur agent ko kaam de, isay handoff kehtay hain.

handoff() mein do cheezen zaroori hoti hain:

agent: jisko handoff dena hai

input_filter: aik function jo handoff se pehle input ko modify karay

✅ 3. Input Filter
Yeh chhoti functions hain jo har handoff se pehle input text ko change karte hain.

Example:

def history_input_filter(input):
    input.input_history = "What is gravity?"
    return input
🧠 Code Behavior Summary
Start hota hai HistoryAgent se — input: "Who discovered Newton's Laws?"

HistoryAgent ka input filter usko "What is gravity?" bana deta hai

Phir ScienceAgent aata hai, woh input ko "What is 9 + 10?" bana deta hai

Phir MathAgent aata hai, woh input ko "Who was Napoleon?" bana deta hai

Phir MathAgent fir se HistoryAgent ko handoff karta hai

Cycle shuru ho jaata hai, dubara History → Science → Math → History...

❗ Error Ki Wajah
Infinite Loop (Recursion) Error

🔄 Infinite Loop Explanation:
Tumhara filter-based handoff ka logic input change karke agents ko confuse kar raha hai.

Har agent samajhta hai:

"Yeh meri domain ka nahi hai, main handoff karta hoon"

Aur yeh cycle kabhi rukti hi nahi.

Result: Python ka error RecursionError: maximum recursion depth exceeded.

💡 Kaise Fix Karein (Understanding Point of View)
Har agent mein ek condition lagao:

Agar input relevant hai, toh handle karo

Warna handoff karo

Handoff cycle ko break karne ka mechanism banao, jaise:

Max depth count

Or ek marker: "forwarded": True input ke saath bhejna

Better input filters banao:

Realistic and intelligent filters

Har filter input ko itna relevant bana de ke next agent usay handle kar le

📋 Yeh Scenario Kab Useful Hai?
Yeh advanced AI logic tab useful hota hai jab:

Tumhare paas multi-specialist agents hon

Har agent decision le sakay ke kaun best suited hai kaam ke liye

Filters help karain context samajhne mein aur sahi direction dene mein

🎯 Final Lesson:
Handoff system powerful hai lekin dangerous bhi, agar tum cycle break na karo to system crash kar sakta hai.

Yeh concept production-level AI routing systems mein use hota hai, jaise customer support bots ya multi-agent reasoning systems mein.