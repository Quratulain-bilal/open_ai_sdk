📘 README: handoff with input_type 
🔹 1. Handoff kya hota hai?
Handoff aik method hai jisme aik agent doosray agent ko kaam transfer (pass) karta hai — bilkul tool call jaisa hi hota hai.

handoff(
    agent=another_agent,
    on_handoff=handler_function
)
🔹 2. Handoff ka pattern tool call jaisa hi hota hai
Handoff jab hota hai to LLM agent sirf 2 cheezen pass karta hai:

Cheez	Description
name	Jis agent ko call karna hai
arguments	Jo input dena hai us agent ko

Example tool-style JSON:

{
  "name": "MathAgent",
  "arguments": {
    "question": "What is x squared?"
  }
}
🔹 3. Normally arguments empty dict hoti hai
Agar aap handoff mein koi input structure define nahi karte to system by default empty dict {} bhejta hai:

{
  "name": "GreetingAgent",
  "arguments": {}
}
Iska matlab function sirf ctx le sakta hai:


def on_handoff(ctx: RunContextWrapper):  # ✅ Valid
    print("Hello from agent!")
🔹 4. Lekin agar input_type define karo...
To phir arguments ke andar structure aayega — jo aapne BaseModel se define kiya ho:


class MyInput(BaseModel):
    question: str
    topic: str

handoff(
    agent=some_agent,
    on_handoff=handle,
    input_type=MyInput  # ✅ Input type define kar diya
)
Tab arguments is tarah dikhenge:

{
  "name": "MathAgent",
  "arguments": {
    "question": "What is derivative?",
    "topic": "Calculus"
  }
}
Aur aapka handler function banega:

def handle(ctx: RunContextWrapper, input: MyInput):  # ✅ 2 parameter honge
    print(input.question)
🔥 5. Important Rule: Function aur input_type dono match hone chahiye
✅ Agar function mein 2 parameter hain:

def handle(ctx, input: MyInput)
➡️ To aapko input_type dena zaroori hai, warna UserError aayega.

❌ Agar function mein sirf ctx hai aur input_type diya hai:
def handle(ctx)  # Sirf ek param
handoff(..., input_type=MyInput)  # ❌ Galat pairing
➡️ Yeh bhi error dega.

✅ Agar sirf ctx hai to input_type nahi dena chahiye:

def handle(ctx)  # ✅
handoff(..., on_handoff=handle)  # ✅ input_type nahi diya
✅ Example Code – Simple & Correct

from agents import Agent, handoff, Runner, RunContextWrapper
from pydantic import BaseModel
import asyncio

# Step 1: Define structured input
class MyInput(BaseModel):
    name: str

# Step 2: Agent to receive handoff
greet_agent = Agent(
    name="GreetAgent",
    instructions="Greet users by name.",
    handoff_description="Says hello."
)

# Step 3: Handoff handler (2 parameters, so input_type required)
def greet(ctx: RunContextWrapper, input: MyInput):
    print(f"Hello, {input.name}! 👋")

# Step 4: Create handoff with input_type
greet_handoff = handoff(
    agent=greet_agent,
    on_handoff=greet,
    input_type=MyInput
)

# Step 5: Main agent to pass query
main_agent = Agent(
    name="MainAgent",
    instructions="Pass greeting queries.",
    handoffs=[greet_handoff]
)

# Step 6: Run the agent
async def run():
    await Runner.run(
        starting_agent=main_agent,
        input="Say hello to Ayesha"
    )

asyncio.run(run())
📌 Summary Table
Scenario	input_type chahiye?	Function
Sirf ctx parameter	❌ Nahi chahiye	def f(ctx)
ctx + input: MyModel	✅ Chahiye	def f(ctx, input: MyModel)
input_type diya ho lekin function mein input nahi ho	❌ ❗ Error	
Function mein input ho lekin input_type na diya ho	❌ ❗ Error	




📘 Handoff with input_type –


Handoff ka concept bilkul tool call ki tarah kaam karta hai, jismein aik agent doosray agent ko kaam handover karta hai. Jab handoff hota hai, to LLM sirf do cheezein agent ko pass karta hai: aik name (jo us agent ka naam hota hai jisko handoff kiya ja raha hai), aur doosra arguments, jismein input data hota hai. Normally agar aap koi input_type define nahi karte, to arguments empty {} hota hai, aur aapka on_handoff function sirf aik parameter ctx: RunContextWrapper leta hai. Lekin agar aap structured input dena chahte hain — jaise question, topic, name — to aapko ek BaseModel class banana hoti hai (jaise MyInput) aur handoff() function mein input_type=MyInput specify karna hota hai. Is surat mein aapka on_handoff function 2 parameters lega: pehla ctx, aur doosra input: MyInput. Lekin yahan aik important rule hai: agar aap function mein 2 parameters le rahe ho to input_type lazmi define karni hogi, warna UserError aayega. Isi tarah agar aap function mein sirf ctx le rahe ho to input_type nahi deni chahiye, warna phir se UserError aayega. Ye system is liye banaya gaya hai takay LLM se aane wala data type-safe ho, aur agents ko accurately samajh aaye ke unko kya data mila hai aur uss pe kya kaam karna hai. Is tarah handoff with input_type aapko predictable aur structured behavior deta hai jab multiple agents apas mein kaam transfer kar rahe hote hain.
