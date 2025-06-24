🧾 Instructions 

syntax
instructions = "Behavior guidelines as a string"
Details:

Agent ka behavior, response tone, aur style control karta hai.

Har response mein agent ko kis tarah jawab dena chahiye, woh yahan define hota hai.


Is se agent ki responses consistent rehti hain — har input pe woh same pattern follow karega.

Aap kisi bhi purpose ke liye agent ko customize kar sakte ho:

"Answer like a helpful doctor"

"Speak like a pirate"

"Always be short and friendly"

📌 Sochiye agent aik role play kar raha hota hai — instructions uska script hota hai. Aap actor ko jaise dialogue dete ho, waisa agent ko yahan direction dete ho.

🧠 Model
Syntax:
model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="model_name",
    temperature=0.7,
    top_p=0.9,
    max_tokens=100
)
Details:

Yeh agent ka processing engine hota hai — kaunsa Large Language Model (LLM) use hoga, woh yahan define hota hai.

Aap OpenAI ya Gemini dono ke models use kar sakte ho (agar compatible ho).

Additional tuning settings:

temperature: Creativity control — 0.0 for facts, 1.0 for creative writing.

top_p: Focused vs. diverse word selection.

max_tokens: Response kitna lamba ho sakta hai (in tokens, ~1 token ≈ ¾ word).

Code mein: Gemini model "gemini-1.5-flash" use ho raha hai, jo fast aur lightweight haisuitable for quick answers.

Yeh model OpenAIChatCompletionsModel wrapper mein diya gaya hai takay woh SDK ke sath compatible ho.

📌 Model agent ka dimaag hai  aap bata rahe ho ke uska sochne ka andaaz kaisa ho. Factual? Creative? Short ya long? Sab settings yahan decide hoti hain.

🛠️ Tools (Aalaat)
Syntax:

@function_tool
def tool_name(parameter: type) -> return_type:
    return result

tools = [tool_name]
Details:

Tools Python functions hote hain jo agent ko external actions karne ki power dete hain.

Example: API call karna, database se fetch karna, ya koi calculation karna.

@function_tool decorator SDK ko batata hai ke ye function ek usable tool hai.

