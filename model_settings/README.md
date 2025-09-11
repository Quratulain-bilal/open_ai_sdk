✅ 1️⃣ temperature: float | None
🔍 Kya karta hai?

Yeh decide karta hai ke model kitna boring ya kitna creative jawab dega.

 Kaise kaam karta hai?

Agar temperature = 0.0 → model har bar same jawab dega.

Agar temperature = 1.0 → model har bar thoda alag creative jawab dega.

 Example:

Aap poochte ho:
 "2 + 2 kya hota hai?"

Agar temperature = 0.0 → model bolega: "4" (hamesha same).

Agar temperature = 0.9 → model bolega:

"4"

"Four is the result"

"Of course it's 4"
(matlab har bar thoda style change karega).

 Kab use karein?
Situation	temperature
Maths / History / Facts	0.0 (boring but correct)
Poem / Story / Creative kaam	0.7 - 1.0 (zinda dil answer)
 2️⃣ top_p: float | None
 Kya karta hai?

Yeh decide karta hai ke model kitne options me se choose kare. Isko nucleus sampling kehte hain.

 Kaise kaam karta hai?

Model ke paas bahut saare possible words hote hain choose karne ke liye.
top_p batata hai:

"Sirf top X% zyada possible words me se choose karo."

 Simple Example with Colors:

Socho aap model se kehte ho:
 "Ek color ka naam batao."

Model ke paas list hai:

Word	Probability (chance)
Red	40%
Blue	30%
Green	15%
Yellow	10%
Purple	5%
 Agar top_p = 1.0:

→ Sabhi colors consider karega (Red, Blue, Green, Yellow, Purple).
Matlab full freedom.
 Agar top_p = 0.5:

→ Sirf top 50% probability wale words lega.
Matlab: Red (40%) + Blue (30%) = 70% → bas Red aur Blue me se choose karega.

📌 Iska matlab: top_p jitna kam hoga, utna focused aur predictable answer milega.

 Kab use karein?
Situation	top_p value
Creative answer (zyada options)	1.0
Focused aur safe answer	0.3 - 0.5
 Important:

temperature = randomness kitni ho.

top_p = kitne options me se choose karna hai.

✅ Dono ek saath kaam karte hain. Agar ek kaafi hai, dusra adjust karna zaroori nai hota.

✅ 3️⃣ frequency_penalty: float | None
🔍 Kya karta hai?

Model agar same word baar baar repeat kare, to yeh penalty lagata hai.

🧪 Example:

👉 Prompt: "Describe love"

Agar frequency_penalty = 0.0
Output: "Love is love is love is love..." (repeat karta ja raha hai).

Agar frequency_penalty = 1.0
Output: "Love is a strong emotion that connects people." (repeat avoid karta hai).

🎯 Kab use karein?

Jab model boring repeat kar raha ho.

Jab essay / poetry / paragraph me repetition avoid karna ho.

✅ 4️⃣ presence_penalty: float | None
🔍 Kya karta hai?

Model ko naye naye topics explore karne ke liye push karta hai.

🧪 Example:

Aap model se kehte ho: "Write about something."

Agar presence_penalty = 0.0
Model baar baar “Technology” ke bare me likhega.

Agar presence_penalty = 1.0
Model bolega: “Technology, Nature, Art, History” etc.

🎯 Kab use karein?

Jab aap brainstorming kar rahe ho.

Jab aap chahte ho ke har bar naya idea aaye.

✅ 5️⃣ tool_choice: "auto" | "required" | "none"
🔍 Kya karta hai?

Agar model ke paas tools (like calculator, weather API) ho, to yeh decide karta hai:

Tool use kare ya na kare.

🎯 Options:
Value	Meaning
"auto"	Model khud decide kare
"required"	Tool zaroor use kare
"none"	Bilkul tool use na kare
🧪 Example:

Prompt: "What's the weather in Karachi?"

"auto" → Model bole: “Let me check” and use weather tool.

"required" → Must use tool.

"none" → Tool use nahi karega, sirf guess karega.

✅ 6️⃣ parallel_tool_calls: bool | None
🔍 Kya karta hai?

Model ek hi time pe multiple tools use kar sakta hai ya nahi, ye decide karta hai.

🧪 Example:

Model ke paas 3 tools hain:

WeatherTool

CalendarTool

FlightTool

parallel_tool_calls = True
→ Teeno tools ek saath call ho sakte hain.

False
→ Ek time pe sirf ek tool chalega.

🎯 Kab use karein?

Jab speed important ho (e.g. voice assistant apps).

✅ 7️⃣ truncation: "auto" | "disabled"
🔍 Kya karta hai?

Agar aapka prompt aur history bahut lamba ho jaye, to purani messages cut karni chahiye ya nahi?

🎯 Options:
Value	Meaning
"auto"	Purani baatein cut ho jaati hain (auto)
"disabled"	Kuch bhi cut nahi hota (ho sakta hai fail ho)
🧪 Example:

Long conversation me model context chhota kare ya purana delete kare — ye handle karta hai.

✅ 8️⃣ max_tokens: int | None
🔍 Kya karta hai?

Model kitne tokens ka answer de — uski limit.

🧪 Example:

max_tokens = 10 → sirf 10 token ka reply (short).

max_tokens = 500 → long answer.

🎯 Kab use karein?
Use case	max_tokens
Short summary	30–50
Essay / blog	300–1000
✅ 9️⃣ reasoning: Reasoning | None
🔍 Kya karta hai?

Yeh special config hai reasoning models ke liye.
Jahan step-by-step logic use karni padti hai (maths, puzzles, logic).

🎯 Use case:

Maths problems

Logic puzzles

Chain-of-thought models

🚫 🔟 metadata, store, include_usage, extra_query, etc.

Yeh sab advanced ya internal features hote hain:

Name	Use
metadata	User ID / tracking info attach karna (for analytics)
store	Response save karna future audit ke liye
include_usage	Token count include karna (cost check ke liye)
extra_query	Extra query parameters API call me bhejna
extra_body	Extra POST body fields
extra_headers	Extra HTTP headers

👉 Ye mostly backend developers ya logging/debugging ke liye useful hain.

🏁 Conclusion:
Parameter	Kaam kya hai?
temperature	Randomness / Creativity control
top_p	Top % tokens me se choose kare
frequency_penalty	Repeat words avoid karna
presence_penalty	Naye topics explore karna
tool_choice	Tool use kare ya nahi
parallel_tool_calls	Multiple tools ek saath call ho
truncation	Purani messages truncate karni ya nahi
max_tokens	Output ki length limit

reasoning	Logic-based reasoning config

