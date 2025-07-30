🔐 Input Filter in Handoff 
🧠 1. Input Filter kya hota hai?
➤ Handoff:
Jab ek agent kisi task ko khud perform nahi karta aur doosray agent ko deta hai, to isay handoff kehte hain.

Example:
MainAgent user ka sawal dekhta hai aur decide karta hai ke ye sawal BillingAgent ya TechAgent ko forward karna chahiye.

➤ HandoffInputFilter:
Ye ek function hota hai jo decide karta hai ke aglay agent ko handoff ke waqt kya kya input diya jaye.

By default:
Agent ko puri conversation history milti hai.
Lekin input_filter ke zariye sirf relevant part dikhaya ja sakta hai (jaise sirf aakhri message).

📦 2. HandoffInputData: Yeh kya hota hai?
Jab filter function chalaya jata hai, to usay ek object milta hai jiska naam hota hai HandoffInputData.

Yeh object aik box jaisa hota hai, jisme teen cheezein hoti hain:

Part	Matlab
input_history	Pura user-agent conversation history
pre_handoff_items	Jo items handoff se pehle aaye
new_items	Naye items (jaise handoff trigger hone wala message ya tool response)

✅ Filter function isi box ko leta hai aur decide karta hai:
"Agla agent ko in mein se kya kya dikhana hai?"

🤖 3. Kya har bar filter function ka syntax fix hota hai?
✅ Haan, bilkul fix hota hai.
Aapko filter function hamesha is form mein likhna hota hai:

python
Copy
Edit
def mera_filter(data: HandoffInputData) -> HandoffInputData:
Part	Kya karta hai
data	Input box jo SDK se milta hai (HandoffInputData)
return	Filtered box (jisme sirf woh data hai jo aap bhejna chahte ho)

📌 Note: Function ka naam mera_filter kuch bhi ho sakta hai, lekin structure same rahega.

⚙️ 4. Agar aap Runner mein filter pass karein to?
✅ Haan, tab bhi wahi function lagega.
python
Copy
Edit
config = RunConfig(
    handoff_input_filter=mera_filter  # 👈 Yeh wahi filter function hai
)
Yeh global filter hoga. Agar agent-level pe filter define nahi kiya gaya, to yeh use hoga.

📋 5. Summary Table – Roman Urdu mein
Situation	Kya Lagay Ga?	Syntax
Agent-specific filter	handoff(...) mein	input_filter=mera_filter
Global filter	RunConfig mein	handoff_input_filter=mera_filter
Function ka syntax	Fix hoga	def mera_filter(data: HandoffInputData)

💡 6. Real-Life Example: Restaurant Waiter aur Chef
Scene:
Ek Waiter (Agent A) ne 10 logon ke orders sun liye hain.
Ab usay sirf aakhri order Chef (Agent B) ko dena hai.

Sawal	Jawaab
👤 Waiter sab kuch chef ko bataye?	❌ Nahi
📦 Kya bataye?	✅ Sirf aakhri customer ka message
🧠 Code mein isko kya kehte hain?	input_filter function
📥 Waiter ke paas kya hota hai?	HandoffInputData
📤 Chef ko kya deta hai?	Filtered HandoffInputData (sirf ek message)

🧪 7. Code Example: Sirf Aakhri Message Forward Karna
python
Copy
Edit
def mera_filter(data: HandoffInputData) -> HandoffInputData:
    last_user_msg = [item for item in data.all_items if item.role == "user"][-1:]
    return HandoffInputData(
        input_history=data.input_history,
        pre_handoff_items=data.pre_handoff_items,
        new_items=last_user_msg
    )
🔍 Line-by-Line Roman Urdu Explanation:
python
Copy
Edit
def mera_filter(data: HandoffInputData) -> HandoffInputData:
Ye function banaya jo filter ka kaam karega.

data mein puri baatein hain — SDK isay deta hai.

Function wapas bhi wohi object return karega — lekin filtered form mein.

python
Copy
Edit
    last_user_msg = [item for item in data.all_items if item.role == "user"][-1:]
data.all_items: Saari messages aur tool responses.

item.role == "user": Sirf user ke messages nikaalo.

[-1:]: Sirf aakhri message rakho.

python
Copy
Edit
    return HandoffInputData(
        input_history=data.input_history,
        pre_handoff_items=data.pre_handoff_items,
        new_items=last_user_msg
    )
Ye function sirf filtered data wapas kar raha hai.

Sirf woh cheez aglay agent ko milti hai jo relevant hai.

🎯 Final Reminder:
Hamesha HandoffInputData ka structure yaad rakho.

Filter function ka signature fix hai.

Aap logic andar change kar sakte ho, lekin structure change nahi hoga
