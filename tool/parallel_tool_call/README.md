📘  parallel_tool_calls = True


📌 What is it?
Normally jab LLM tools detect karta hai, to wo ek time pe sirf ek tool call karta hai per turn. Lekin agar aap parallel_tool_calls=True set kar dein, to multiple tools ek hi turn mein call ho sakte hain.

 "Agar user ne aik saath 2 tools ka kaam bola ho, to dono tools aik hi bar run kar jayein instead of one-by-one."

✅ Benefits:
⚡ Speed: Dono tools ek saath run honay se response jaldi milta hai.

📈 Efficiency: Kam turns mein kaam ho jata hai.

🔁 Less Looping: Har tool ke liye alag turn lene ki zarurat nahi padti.

❗ Limitations:
🔥 Gemini API does NOT support parallel tool calls as of now.
Aapko error mil sakta hai:


Error: Parallel tool calls are not supported.
✅ Ye feature mostly OpenAI's GPT-4 based tools ke sath achi tarah kaam karta hai.

⚠️ If You Use Gemini:
Agar aap Gemini model use kar rahe hain (gemini-1.5-flash, 2.0), to aapko parallel_tool_calls=False rakhna padega, warna 400 error aayega.


