Jab bhi aap Runner.run() ya Runner.run_sync() use karte hain, to LLM (like GPT or Gemini) se jo original raw model response aata hai — woh raw_responses mein store hota hai.

Ye woh response hota hai jo SDK bina processing ke, direct LLM se receive karta hai.

Step 1: User Input
Aap koi message ya task bhejtay ho agent ko — for example: "Summarize this paragraph."

Step 2: Agent → LLM Call
Agent backend pe LLM ko query karta hai. LLM kuch raw JSON response return karta hai. Ye response contain karta hai:

Raw generated message

Tool call structure (agar koi ho)

Token usage

Finish reason, etc.

Step 3: SDK Parsing & Wrapping
SDK is raw JSON ko:

Internally parse karta hai

Clean format mein RunItems banata hai

Lekin original response ko bhi ModelResponse ke roop mein preserve karta hai

Step 4: Store in raw_responses
Ye original ModelResponse object list ke form mein RunResult.raw_responses mein store hoti hai.