# 🚀 ULTIMATE PROMPT ENGINEERING GUIDE (Roman Urdu Mein) 

> _"Prompt Engineering sirf 'instructions dena' nahi  ye ek art hai, science hai, aur ek superpower hai!"

Agar aap ne socha hai ke Prompt Engineering sirf "Temperature aur Few-Shot" tak limited hai — to aap bilkul galat hain! Aaj ke zamane mein, **top companies aur AI researchers** ne itni advanced techniques develop kar li hain ke aap AI ko **detective, scientist, ya apna personal assistant** bana sakte hain!

Ye guide aap ko **zero se PRO** tak le jayega. Har technique ko hum **Roman Urdu** mein samjhain ge, har mushkil lafz ko **brackets mein explain** karen ge, aur har technique ke saath **real examples** den ge — taake aap seedha istemal kar saken!

Chaliye, shuru karte hain!

---

## 📚 1. Prompt Engineering Kya Hai? 

**Prompt = Hukum* jo aap AI ko dete hain.  
**Engineering = Is hukum ko itna achha banana** ke AI bilkul wohi kare jo aap chahte hain — na zyada, na kam!

- **LLM (Large Language Model)**: AI ka dimagh — jo internet ki sab cheezon ko padh kar seekha hai. *(Jaise koi bacha jo library ki sab kitabein parh kar sab kuch yaad kar leta hai!)*
- **Token**: AI ke liye har lafz, comma, ya space ek “token” hota hai. *(Jaise “Pakistan” = 1 token, “Pak-istan” = 2 tokens)*

> 💡 **Example**:  
> ❌ Ghalat Prompt: _"Mujhe code chahiye."_  
> ✅ Sahi Prompt: _"Write a Python function that takes a list of numbers and returns the average. Include comments in Urdu Roman."_

---

## ⚙️ 2. AI Ki Settings: Temperature, Top-K, Top-P (Output Control)

### 🌡️ A. Temperature (Rangin Soch Ka Button)
- **Low (0.1-0.3)**: AI boring aur safe jawab deta hai. *(Math, facts ke liye perfect!)*
- **High (0.7-1.0)**: AI creative, random, aur kabhi-kabhi bekaar jawab deta hai. *(Stories, ideas ke liye acha!)*
- **0 = Greedy**: Hamesha sab se zyada likely wala lafz choose karta hai.
- **1+ = Nonsense Mode**: AI bar-bar same lafz bolne lagta hai — is ko kehte hain **"Repetition Loop Bug"**.

### 🔝 B. Top-K & Top-P (Sochne Ka Filter)
- **Top-K (e.g., 20)**: Sirf top 20 most likely lafzon mein se choose karo.
- **Top-P (e.g., 0.9)**: Sirf un lafzon mein se choose karo jinki combined probability 90% ho.
- **Low Values = Focused & Factual**  
  **High Values = Creative & Varied**

> 🎯 **Pro Settings**:  
> - Facts / Code: `Temp: 0.0`, `Top-P: 0.9`, `Top-K: 20`  
> - Creative Writing: `Temp: 0.8`, `Top-P: 0.95`, `Top-K: 50`  
> - Brainstorming: `Temp: 1.0`, `Top-P: 1.0`, `Top-K: 100`

---

## 🛠️ 3. Prompting Techniques (AI Ko Kaise Samjhain? — FULL LIST!)

### 1. Zero-Shot 
Bina kisi example ke, direct sawal poocho.

> **Prompt**:  
> `Translate "Hello, how are you?" into Urdu Roman.`  
> **Output**: `Assalam-o-Alaikum, aap kaise hain?`

---

### 2. Few-Shot 
3-5 examples dikhao — AI pattern samajh jata hai.

> **Prompt**:  
> ```
> Turn English to Roman Urdu:
> Example 1: "I love pizza" → "Mujhe pizza pasand hai"
> Example 2: "Where is the market?" → "Market kahan hai?"
> Now do this: "Let's go to the park."
> ```

---

### 3. Chain of Thought (CoT) — "Step-by-Step Socho!"
Mushkil problems ke liye — AI ko kehna hai: _"Pehle soch, phir jawab do."_

> **Prompt**:  
> `Aap ke paas 500 rupaye hain. Ek pen 50 rupaye ka hai. Kitne pen aap khareed sakte hain? Let’s think step by step.`  
> **AI**:  
> 1. Ek pen = 50 rupaye.  
> 2. Total paisa = 500 rupaye.  
> 3. 500 / 50 = 10.  
> 4. Jawab: 10 pen.

> 📌 **Pro Tip**: CoT ke liye hamesha `Temperature = 0` rakho!

---

### 4. Step-Back Prompting 
Pehle general sawal poocho, phir us ka jawab use kar ke specific task karo.

> **Step 1**: `What are the key features of a good smartphone?`  
> **Step 2**: `Based on those features, recommend a phone under 50,000 rupees.`

---

### 5. Self-Consistency (Ek Hi Sawal, Kayi Baar Poocho!)
Ek hi sawal ko 5-10 baar poocho (high temperature ke sath), phir sab se zyada aane wale jawab ko final jawab maan lo.

> **Use Case**: Email classification — Kya ye email "IMPORTANT" hai ya "NOT IMPORTANT"?

---

### 6. ReAct Prompting (Reason + Act — AI Tools Istemal Kare!)
AI sochta hai, phir Google search karta hai, phir phir sochta hai.

> **Task**: `How many kids do all Metallica band members have combined?`  
> **AI**:  
> 1. *Sochta hai*: “Pehle band members ke names nikalne hain.”  
> 2. *Action*: Google search — “Metallica band members”.  
> 3. Har member ke liye search karta hai — “James Hetfield kids”.  
> 4. Sab ko add kar deta hai!

---

### 7. Tree of Thoughts (ToT) 
AI sirf ek raasta nahi, balki **kai different raaston** par sochta hai — phir best choose karta hai.

> **Example**: _"Best way to learn Python?"_  
> AI sochega:  
> - Online courses  
> - Books  
> - YouTube  
> - Bootcamps  
> Phir compare kar ke best suggest karega.

---

### 8. Automatic Prompt Engineering (APE) — "AI Se AI Ko Prompt Likhwao!"
AI se poocho: _"Mujhe 10 different prompts likh do jo pizza orders ko JSON mein convert karein!"_

> **Steps**:  
> 1. 10 prompts generate karwao.  
> 2. Test karo — dekho konsa behtar kaam karta hai.  
> 3. Best prompt choose karo — ya us mein improve karo!

---

### 9. Generated Knowledge Prompting — "Pehle Facts Nikalo, Phir Jawab Do!"

Pehle AI se facts generate karwao, phir un facts ko use kar ke final task karo.

> **Prompt**:  
> ```
> Step 1: List 5 key facts about climate change in Pakistan.
> Step 2: Using those facts, write a 3-paragraph article for school students.
> ```

> 💡 **Fayda**: AI ke hallucinations (jhoot bolna) kam hote hain — kyunki woh pehle facts check karta hai.

---

### 10. Directional Stimulus Prompting — "Hints Do, Pura Jawab Mat Do!"

AI ko pura jawab nahi, balki **hints** do — taake woh khud soch kar jawab de.

> **Prompt**:  
> `Instead of giving the full answer, give me 3 hints to solve this math problem: 2x + 5 = 15.`  
> **AI**:  
> 1. Pehle 5 ko right side le jao.  
> 2. Phir dono sides ko 2 se divide karo.  
> 3. x ka value 5 aye ga.

> 💡 **Use Case**: Students ke liye — taake woh khud seekh sakein.

---

### 11. Skeleton-of-Thought (SoT) — "Pehle Outline Banao, Phir Bharo!"

Pehle AI se outline (skeleton) banwao, phir us outline ko fill karwao.

> **Prompt**:  
> ```
> Step 1: Create an outline for a blog post about "How to Save Money in Pakistan".
> Step 2: Now, write the full blog post using that outline.
> ```

> 💡 **Fayda**: Structure accha hota hai — aur AI zyada organized jawab deta hai.

---

### 12. Least-to-Most Prompting — "Chote Sawal, Phir Bade Sawal!"

Pehle chote, aasan sawal poocho — phir un ke jawab use kar ke bade, mushkil sawal poocho.

> **Example**:  
> 1. `What is photosynthesis?`  
> 2. `How does photosynthesis help plants grow?`  
> 3. `Explain the role of photosynthesis in the ecosystem.`

> 💡 **Fayda**: AI ko step-by-step build-up milta hai — is se final jawab zyada accurate hota hai.

---

### 13. Multimodal Prompting — "Sirf Text Nahi, Image, Audio Bhi!"

AI ko text ke sath **image, audio, ya video** bhi de sakte hain!

> **Example**:  
> - Photo upload kar ke poocho: _"Is photo mein kya cheez hai?"_  
> - Audio suna kar kehna: _"Is audio ka summary likho."_

> 💡 **Note**: Is ke liye special models chahiye hote hain — jaise Gemini 1.5 ya GPT-4V.

---

## 🎯 4. Best Practices — Prompting Pro Kis Tarah Banein? (ULTIMATE LIST!)

### ✅ 1. Hamesha Examples Do (Few-Shot Best Hai!)
AI ko examples dikhao — ye sab se zyada effective tareeqa hai.

### ✅ 2. Clear & Specific Bano
> ❌ `Write about games.`  
> ✅ `Write a 3-paragraph blog post about the history of Nintendo in the 1990s, in a fun tone.`

### ✅ 3. Strong Verbs Istemal Karo
Shuru mein ye verbs use karo:  
`Write`, `Explain`, `List`, `Classify`, `Translate`, `Act as`, `Summarize`.

### ✅ 4. Output Ki Length Control Karo
`Answer in 1 sentence.` ya `Explain in 100 words or less.`

### ✅ 5. Variables Use Karo (Dynamic Prompts Ke Liye)
> **Prompt**: `Tell me a fun fact about the city: {city_name}.`  
> `{city_name} = "Lahore"`

### ✅ 6. JSON Format Mein Output Mangain
> **Prompt**: `Extract product name, price, and release date. Return as JSON.`

### ✅ 7. Document Karo Apne Prompts Ko!
Har prompt, us ki settings, aur output ko note karo.

> **Template**:  
> | Prompt Name | Goal | Model | Temp | Prompt | Output | Result (OK/Not OK) |

### ✅ 8. Experiment Karo — Har Cheez Try Karo!
- Different wordings try karo.
- Different temperatures try karo.
- Different models try karo (Gemini, GPT, Claude).

### ✅ 9. Use Constraints Wisely (Positive Instructions Diyein!)
> ❌ `Don’t mention the price.`  
> ✅ `Only describe the product’s features and color.`

### ✅ 10. Test on Edge Cases (Ajeeb Inputs Try Karo!)
Agar aap ka prompt pizza orders handle karta hai — to test karo:  
- "No cheese" wala order  
- "Half-half" wala order  
- "Extra extra spicy" wala order

### ✅ 11. Use JSON Schema for Complex Data
AI ko ek **blueprint** do ke data kaisa hona chahiye.

> **Example Schema**:  
> ```json
> {
>   "name": "string",
>   "price": "number",
>   "release_date": "date"
> }
> ```

### ✅ 12. Use “Let’s Think Step by Step” for EVERY Complex Task
Ye magic phrase hai — is se AI ka accuracy 50%+ badh jata hai!

### ✅ 13. Combine Techniques (Hybrid Prompts)
Ek hi prompt mein **CoT + Few-Shot + Role Prompting** combine karo!

> **Example**:  
> ```
> Act as a strict math teacher. Explain step by step.
> Example: 2 + 2 = 4 (Because we add two numbers).
> Now solve: 5 + 7 = ?
> ```

---

## 📝 5. Summary — Cheat Sheet (Sab Kuch Ek Jagah!)

| Technique          | Kab Use Karein?                          | Magic Phrase                     |
|--------------------|------------------------------------------|----------------------------------|
| Zero-Shot          | Simple, direct tasks                     | `Translate`, `Summarize`         |
| Few-Shot           | Complex patterns, data formatting        | `Example: ...`                   |
| Chain of Thought   | Math, logic, reasoning                   | `Let’s think step by step.`      |
| Step-Back          | Creative brainstorming                   | `First, list 5 ideas...`         |
| Self-Consistency   | High-stakes classification               | Ask 5 times, pick most common    |
| ReAct              | When you need web search / tools         | `Search for...`                  |
| Tree of Thoughts   | Complex problems with multiple solutions | `Explore all possible ways...`   |
| Generated Knowledge| Reduce hallucinations                    | `First, list facts about...`     |
| Directional Stimulus| Teach students / give hints             | `Give me 3 hints to solve...`    |
| Skeleton-of-Thought| Long-form content                        | `First, create an outline...`    |
| Least-to-Most      | Build up complexity                      | `First, explain X. Then, Y...`   |




**Happy Prompting!** 😊🤖
