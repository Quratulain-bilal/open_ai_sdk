📌 prompt_with_handoff_instructions() kya hai?
Yeh aik function hai jo aapke agent ko yeh batata hai ke:

Agar user ka sawaal is agent ke kaam se related nahi hai, to wo agent query ko kisi aur agent ko de (handoff) kar sakta hai.

Is function ka kaam hai agent ke instructions mein ek standard line add karna jise agent samajhta hai:

"Agar aap ye kaam nahi kar saktay, to aap isay kisi aur agent ko handoff kar saktay hain."

🔄 Kab prompt_with_handoff_instructions() use karna chahiye?
Situation / Halat	Use karna chahiye?
Aap ke paas 2 ya zyada agents hain (jaise billing, support)	✅ Haan
Aap chahte ho ke har agent apna kaam kare aur doosray ko handoff kare	✅ Haan
Sirf aik agent hai poore system mein	❌ Nahi zaroori
Aap handoff feature use hi nahi kar rahe	❌ Nahi zaroori

🧠 important 
Agar aap is function ko use nahi karte, to har agent yeh sochega ke wo har query ka jawab dena uska kaam hai — chahe wo uske kaam se related ho ya nahi.

Lekin agar aap yeh function use kar lein, to:

Agent keh sakta hai: "ye kaam mere liye nahi hai"

Aur query ko automatically sahi agent tak ponchaya jata hai (handoff)

Iska faida:

✅ System clean rehta hai

✅ Har agent sirf apna kaam karta hai

✅ User ko sahi jawab milta hai

📁 Kaise kaam karta hai (chhoti summary):
Aap yeh import karte ho:

from agents.extensions.handoff_prompt import prompt_with_handoff_instructions
Jab aap agent banate ho, to instructions mein yeh function lagate ho:

billing_agent = Agent(
    name="Billing Agent",
    instructions=prompt_with_handoff_instructions("Sirf billing ka jawab do.")
)
Is se agent samajhta hai ke agar query billing se related nahi, to wo support agent ko handoff kar sakta hai.

📦 Example:

from agents import Agent, Runner
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

billing_agent = Agent(
    name="Billing Agent",
    instructions=prompt_with_handoff_instructions("Sirf billing se related sawaalat ka jawab do.")
)

support_agent = Agent(
    name="Support Agent",
    instructions=prompt_with_handoff_instructions("Sirf support se related sawaalat ka jawab do.")
)

runner = Runner(agents=[billing_agent, support_agent])

response = runner.run("Mujhe internet support chahiye.")
print(response)
🔚 Summary 
prompt_with_handoff_instructions() agent ko yeh batata hai ke "agar query us ke kaam ki nahi, to wo usay kisi aur agent ko de sakta hai"

Agar aapke paas multiple agents hain, to yeh zaroor use karein

Agar sirf ek agent hai, to use karna zaroori nahi