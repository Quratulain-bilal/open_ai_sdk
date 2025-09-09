# 🧠  PROMPT ENGINEERING MASTER GUIDE  


> _"Prompt Engineering sirf ‘instructions dena’ nahi — ye ek **science** hai, jismein aap AI ke dimagh ko **guide** karte hain taake woh aap ke liye **sahi aur accurate** kaam kare!"_

---

## 📚 SECTION 1: Prompt Engineering Kya Hai? 

### 💡 Simple Definition:
**Prompt = Hukum** jo aap AI ko dete hain.  
**Engineering = Is hukum ko itna achha banana** ke AI bilkul wohi kare jo aap chahte hain — na zyada, na kam!

- **LLM (Large Language Model)**: AI ka dimagh — jo internet ki sab cheezon ko padh kar seekha hai. *(Jaise koi bacha jo library ki sab kitabein parh kar sab kuch yaad kar leta hai!)*
- **Token**: AI ke liye har lafz, comma, ya space ek “token” hota hai. *(Jaise “Pakistan” = 1 token, “Pak-istan” = 2 tokens)*

> 💡 **Example**:  
> ❌ Ghalat Prompt: _"Mujhe code chahiye."_  
> ✅ Sahi Prompt: _"Write a Python function that takes a list of numbers and returns the average. Include comments in Urdu Roman."_



## ⚙️ SECTION 2: AI Ki Settings — “Dials” Jo Aap Ko Control Karni Chahiye

Ye settings AI ke output ko dramatically change karti hain. In ko ignore mat karo!



### 1. 🌡️ Temperature — The “Creativity Knob”

#### ❓ Kya Hai?
Ye setting batati hai ke AI kitna **random** ya **safe** jawab de.

#### 🧠 Kaise Kaam Karti Hai?
- **Low (0.0–0.3)**: AI boring aur safe jawab deta hai. *(Math, facts ke liye perfect!)*
- **High (0.7–1.0+)**: AI creative, random, aur kabhi-kabhi bekaar jawab deta hai. *(Stories, ideas ke liye acha!)*
- **0 = Greedy**: Hamesha sab se zyada likely wala lafz choose karta hai.
- **1+ = Nonsense Mode**: AI bar-bar same lafz bolne lagta hai — is ko kehte hain **"Repetition Loop Bug"**.

#### 🎯 Real-World Example:
> **Task**: 2 + 2 = ?  
> - Temp = 0 → Output: `4` (100% accurate)  
> - Temp = 1 → Output: `4... or maybe 5? Let’s explore the philosophy of numbers...` (Useless!)

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Math ya code ke liye high temperature use karna → Ghalat jawab aata hai.
- Creative task ke liye low temperature use karna → Boring, robotic jawab aata hai.

> 💡 **Pro Tip**: Agar task ka ek hi sahi jawab hai (math, classification, code) → **Hamesha Temperature = 0 rakho!**

---

### 2. 🔝 Top-K & Top-P — The “Idea Filters”

Ye settings AI ko kehti hain ke woh sirf apne "top choices" mein se hi agla lafz choose kare.

#### ➤ Top-K (e.g., K=20)
- Sirf top 20 most likely lafzon mein se choose karo.
- Low K (1–10) → Focused, factual.
- High K (50–100) → Creative, varied.
- K=1 → Same as greedy (Temp=0).

#### ➤ Top-P (a.k.a. Nucleus Sampling, e.g., P=0.9)
- Considers enough top words until their combined probability ≥ 90%.
- Low P (0.1–0.5) → Very focused.
- High P (0.9–1.0) → Very open-ended.

#### 🎯 Real-World Example:
> **Task**: “Mujhe ek funny joke sunao.”  
> - Top-K = 5 → AI sirf 5 most common jokes mein se choose karega → Boring.  
> - Top-K = 50 → AI zyada creative jokes try karega → Mazedaar!

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Top-K aur Top-P dono ko high rakhte hain → AI ka output bekaar ho jata hai.
- In settings ko ignore karte hain → AI unpredictable ho jata hai.

> 💡 **Pro Tip**: Use **Top-P = 0.95** and **Top-K = 30** as your default starting point. Adjust from there.

---

### 3. 📏 Max Tokens — The “Answer Length Limiter”

#### ❓ Kya Hai?
Ye setting batati hai ke AI ko kitne **words ya tokens** (chote chote lafz) tak ka jawab dena hai.

#### 🧠 Kaise Kaam Karti Hai?
- Zyada tokens = zyada time aur zyada cost (agar aap pay kar rahe hain).
- Ye setting sirf jawab ko **kat deta hai** — AI ko short jawab dene ke liye aap ko apne prompt mein bhi kehna hoga!

#### 🎯 Real-World Example:
> **Prompt**: `Explain quantum physics in 10 words.`  
> **Output**: `Tiny particles behave weirdly; reality is probabilistic.`  
> Agar Max Tokens = 5 hota → Output: `Tiny particles behave weirdly...` (Incomplete!)

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Max Tokens ko bahut chota rakhna → AI ka jawab incomplete ho jata hai.
- Max Tokens ko bahut bada rakhna → AI rambling shuru kar deta hai.

> 💡 **Pro Tip**: Hamesha apne prompt mein bhi length specify karo — jaise: `Answer in 1 sentence.`

---

## 🛠️ SECTION 3: Prompting Techniques — Har Ek Ko Depth Mein Samjho!

---

### 1. Zero-Shot Prompting — Just Ask!

#### ❓ Kya Hai?
Bina kisi example ke, direct sawal poocho.

#### 🧠 Kaise Kaam Karti Hai?
AI apne training data se pattern dhundh kar jawab deta hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> `Translate "Hello, how are you?" into Urdu Roman.`  
> **Output**: `Assalam-o-Alaikum, aap kaise hain?`

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Vague prompts dete hain → AI confuse ho jata hai.
- Complex tasks ke liye zero-shot use karte hain → Ghalat jawab aata hai.

> 💡 **Pro Tip**: Simple tasks ke liye use karo — jaise translate, summarize, classify.

---

### 2. Few-Shot Prompting — Show, Don’t Just Tell!

#### ❓ Kya Hai?
AI ko 3-5 examples dikhao — taake woh pattern samajh sake.

#### 🧠 Kaise Kaam Karti Hai?
AI examples se “template” banata hai — phir us template ko apne input par apply karta hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> ```
> Turn English to Roman Urdu:
> Example 1: "I love pizza" → "Mujhe pizza pasand hai"
> Example 2: "Where is the market?" → "Market kahan hai?"
> Now do this: "Let's go to the park."
> ```
> **Output**: `Chalo park chalte hain.`

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Examples mein galtiyan karte hain → AI ghalat pattern seekh leta hai.
- Edge cases (ajeeb inputs) nahi dikhate — jaise “no cheese” wala pizza order.

> 💡 **Pro Tip**: Include “weird” examples — jaise “no cheese”, “half-half”, “extra spicy”.

---

### 3. Chain of Thought (CoT) — “Think Step by Step”

#### ❓ Kya Hai?
AI ko kehna hai: _"Pehle soch, phir jawab do."_

#### 🧠 Kaise Kaam Karti Hai?
AI problem ko chote chote steps mein todta hai — har step ka logic clear hota hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> `Aap ke paas 500 rupaye hain. Ek pen 50 rupaye ka hai. Kitne pen aap khareed sakte hain? Let’s think step by step.`  
> **AI**:  
> 1. Ek pen = 50 rupaye.  
> 2. Total paisa = 500 rupaye.  
> 3. 500 / 50 = 10.  
> 4. Jawab: 10 pen.

#### ⚠️ Galtiyan Jo Log Karte Hain:
- CoT ke saath high temperature use karna → Steps random ho jate hain.
- “Let’s think step by step” nahi likhna → AI direct ghalat jawab de deta hai.

> 💡 **Pro Tip**: CoT ke liye hamesha `Temperature = 0` rakho!

---

### 4. Step-Back Prompting — “Pehle Bada Sawal Poocho!”

#### ❓ Kya Hai?
Pehle general sawal poocho — phir us ka jawab use kar ke specific task karo.

#### 🧠 Kaise Kaam Karti Hai?
AI ko pehle background knowledge activate hoti hai — is se final jawab zyada accurate hota hai.

#### 🎯 Real-World Example:
> **Step 1**: `What are the key features of a good smartphone?`  
> **Step 2**: `Based on those features, recommend a phone under 50,000 rupees.`

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Direct specific task pooch lete hain → AI shallow jawab deta hai.
- Step-Back ka concept nahi samajhte — sochte hain ye time waste hai.

> 💡 **Pro Tip**: Creative tasks, brainstorming, complex problem-solving ke liye perfect hai.

---

### 5. Self-Consistency — “Ek Hi Sawal, Kayi Baar Poocho!”

#### ❓ Kya Hai?
Ek hi sawal ko 5-10 baar poocho (high temperature ke sath) — phir sab se zyada aane wale jawab ko final jawab maan lo.

#### 🧠 Kaise Kaam Karti Hai?
AI kabhi-kabhi galti kar sakta hai — multiple tries se accuracy badhti hai.

#### 🎯 Real-World Example:
> **Task**: Email classification — Kya ye email "IMPORTANT" hai ya "NOT IMPORTANT"?  
> Agar 5 baar poochne par 4 baar "IMPORTANT" aya, to final jawab "IMPORTANT" maan lo.

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Low temperature use karte hain → Sab answers same aate hain → Benefit nahi milta.
- Sirf 2-3 baar try karte hain — 5-10 baar try karna chahiye.

> 💡 **Pro Tip**: High-stakes decisions (medical, legal, security) ke liye perfect hai.

---

### 6. ReAct Prompting — “Reason + Act” (AI Tools Istemal Kare!)

#### ❓ Kya Hai?
AI sochta hai, phir Google search karta hai, phir phir sochta hai.

#### 🧠 Kaise Kaam Karti Hai?
AI apne aap ko “agent” ki tarah behave karta hai — jo tools (search, calculator) use kar sakta hai.

#### 🎯 Real-World Example:
> **Task**: `How many kids do all Metallica band members have combined?`  
> **AI**:  
> 1. *Sochta hai*: “Pehle band members ke names nikalne hain.”  
> 2. *Action*: Google search — “Metallica band members”.  
> 3. Har member ke liye search karta hai — “James Hetfield kids”.  
> 4. Sab ko add kar deta hai!

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Code nahi likhna aata — is ke liye Python + LangChain chahiye.
- Real-time data ki zaroorat nahi hoti — phir bhi ReAct use kar lete hain → Overkill.

> 💡 **Pro Tip**: Jab aap ko REAL-TIME data chahiye (stock prices, news, sports scores).

---

### 7. Tree of Thoughts (ToT) — “Sab Raaste Socho!”

#### ❓ Kya Hai?
AI sirf ek raasta nahi, balki **kai different raaston** par sochta hai — phir best choose karta hai.

#### 🧠 Kaise Kaam Karti Hai?
Jaise koi insaan jo kisi problem ko solve karne ke liye kai tareeqon par gaur kare.

#### 🎯 Real-World Example:
> **Task**: _"Best way to learn Python?"_  
> AI sochega:  
> - Online courses  
> - Books  
> - YouTube  
> - Bootcamps  
> Phir compare kar ke best suggest karega.

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Simple tasks ke liye use karna — ToT expensive aur slow hai.
- Is ka concept nahi samajhte — sochte hain ye CoT ka hi dusra naam hai.

> 💡 **Pro Tip**: Complex problems with multiple solutions ke liye perfect hai.

---

### 8. Automatic Prompt Engineering (APE) — “AI Se AI Ko Prompt Likhwao!”

#### ❓ Kya Hai?
AI se poocho: _"Mujhe 10 different prompts likh do jo pizza orders ko JSON mein convert karein!"_

#### 🧠 Kaise Kaam Karti Hai?
AI apne aap ko “prompt engineer” ki tarah behave karta hai — jo aap ke liye best prompt generate karta hai.

#### 🎯 Real-World Example:
> **Steps**:  
> 1. 10 prompts generate karwao.  
> 2. Test karo — dekho konsa behtar kaam karta hai.  
> 3. Best prompt choose karo — ya us mein improve karo!

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Generated prompts ko blindly use kar lete hain — test nahi karte.
- APE ko magic samajh lete hain — har task ke liye perfect nahi hota.

> 💡 **Pro Tip**: Jab aap ko bohat sare similar prompts chahiye hote hain — jaise ek chatbot ke liye 50 alag tareeqon se "order place karna".

---

### 9. Generated Knowledge Prompting — “Pehle Facts Nikalo, Phir Jawab Do!”

#### ❓ Kya Hai?
Pehle AI se facts generate karwao — phir un facts ko use kar ke final task karo.

#### 🧠 Kaise Kaam Karti Hai?
AI ke hallucinations (jhoot bolna) kam hote hain — kyunki woh pehle facts check karta hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> ```
> Step 1: List 5 key facts about climate change in Pakistan.
> Step 2: Using those facts, write a 3-paragraph article for school students.
> ```

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Step 1 ko skip kar dete hain — direct article likhwate hain → Hallucinations zyada hote hain.
- Facts ko verify nahi karte — AI ghalat facts bhi de sakta hai.

> 💡 **Pro Tip**: Accuracy critical ho — jaise education, journalism, research.

---

### 10. Directional Stimulus Prompting — “Hints Do, Pura Jawab Mat Do!”

#### ❓ Kya Hai?
AI ko pura jawab nahi, balki **hints** do — taake woh khud soch kar jawab de.

#### 🧠 Kaise Kaam Karti Hai?
Students ko encourage karta hai ke woh khud seekhein — AI un ka teacher ban jata hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> `Instead of giving the full answer, give me 3 hints to solve this math problem: 2x + 5 = 15.`  
> **AI**:  
> 1. Pehle 5 ko right side le jao.  
> 2. Phir dono sides ko 2 se divide karo.  
> 3. x ka value 5 aye ga.

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Hints ki jagah direct answer de dete hain — learning nahi hoti.
- Hints bohat vague hote hain — students confuse ho jate hain.

> 💡 **Pro Tip**: Teaching, tutoring, interviews ke liye perfect hai.

---

### 11. Skeleton-of-Thought (SoT) — “Pehle Outline Banao, Phir Bharo!”

#### ❓ Kya Hai?
Pehle AI se outline (skeleton) banwao — phir us outline ko fill karwao.

#### 🧠 Kaise Kaam Karti Hai?
Structure accha hota hai — aur AI zyada organized jawab deta hai.

#### 🎯 Real-World Example:
> **Prompt**:  
> ```
> Step 1: Create an outline for a blog post about "How to Save Money in Pakistan".
> Step 2: Now, write the full blog post using that outline.
> ```

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Direct long article likhwate hain — AI rambling shuru kar deta hai.
- Outline ko ignore kar dete hain — structure nahi hota.

> 💡 **Pro Tip**: Long-form content (blogs, reports, scripts) ke liye perfect hai.

---

### 12. Least-to-Most Prompting — “Chote Sawal, Phir Bade Sawal!”

#### ❓ Kya Hai?
Pehle chote, aasan sawal poocho — phir un ke jawab use kar ke bade, mushkil sawal poocho.

#### 🧠 Kaise Kaam Karti Hai?
AI ko step-by-step build-up milta hai — is se final jawab zyada accurate hota hai.

#### 🎯 Real-World Example:
> **Example**:  
> 1. `What is photosynthesis?`  
> 2. `How does photosynthesis help plants grow?`  
> 3. `Explain the role of photosynthesis in the ecosystem.`

#### ⚠️ Galtiyan Jo Log Karte Hain:
- Direct complex sawal pooch lete hain — AI overwhelm ho jata hai.
- Steps ko skip kar dete hain — learning curve steep ho jati hai.

> 💡 **Pro Tip**: Complex topics, onboarding new users, teaching ke liye perfect hai.

---

## 🎯 SECTION 4: Best Practices — Prompting Pro Kis Tarah Banein? (ULTIMATE LIST!)

### ✅ 1. Hamesha Examples Do (Few-Shot Best Hai!)
### ✅ 2. Clear & Specific Bano
### ✅ 3. Strong Verbs Istemal Karo
### ✅ 4. Output Ki Length Control Karo
### ✅ 5. Variables Use Karo
### ✅ 6. JSON Format Mein Output Mangain
### ✅ 7. Document Karo Apne Prompts Ko!
### ✅ 8. Experiment Karo — Har Cheez Try Karo!
### ✅ 9. Use Constraints Wisely (Positive Instructions Diyein!)
### ✅ 10. Test on Edge Cases
### ✅ 11. Use JSON Schema for Complex Data
### ✅ 12. Use “Let’s Think Step by Step” for EVERY Complex Task
### ✅ 13. Combine Techniques (Hybrid Prompts)
### ✅ 14. CoT ke liye Temperature = 0
### ✅ 15. Prompting Iterative Process Hai — Kabhi Perfect Nahi Hota!

---

## 🚀 FINAL TIP: Experiment Karo, Document Karo, Repeat Karo!

Prompt Engineering ek **iterative process** hai — matlab aap ko bar-bar try karna hoga, thoda badalna hoga, test karna hoga, aur phir dobara try karna hoga. Lekin jab aap ko sahi formula mil jaye ga — to AI aap ka sab se behtar assistant ban jaye ga!

**Happy Prompting!** 😊🤖

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


