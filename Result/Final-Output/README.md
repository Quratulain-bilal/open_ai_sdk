🧠 final_output 

final_output is the last value jo aapke agent ne generate kiya after completing all loops, tool calls, and possible handoffs.


🔷  Case 1: ❌ output_type NOT Defined
🔹 Meaning:
Agar aap Agent(...) mein output_type define nahi karte, to:

Agent ke instructions normal language generation hoti hain (free text)

AI model kuch bhi plain string return karega (not structured)

🔹 Lifecycle Flow:

Agent run karta hai ⟶ AI se plain string response aata hai ⟶ 
SDK parse nahi karta ⟶ `final_output` as string return hota hai
✅ Example:

agent = Agent(
    name="SimpleAgent",
    instructions="Write a small joke"
    # ❌ No output_type
)

result = Runner.run_sync(agent, input="Tell a joke")

print(result.final_output)  # ➤ This will be a `str`
Output Example:


"Why don’t scientists trust atoms? Because they make up everything!"
🔷  Case 2: ✅ output_type IS Defined
🔹 Meaning:
Agar aap Agent(...) mein output_type=MyModel define karte hain, to:

Agent se aane wala response structured (JSON-like) expected hota hai

SDK AI ke output ko Pydantic model mein parse karne ki koshish karta hai

🔹 Lifecycle Flow:

Agent run karta hai ⟶ AI JSON structure return karta hai ⟶
SDK tries: Pydantic model se validate kare ⟶ 
Agar match hua ⟶ return parsed model object as final_output
✅ Example:

from pydantic import BaseModel

class JokeOutput(BaseModel):
    setup: str
    punchline: str

agent = Agent(
    name="JokeAgent",
    instructions="Give a joke as JSON with setup and punchline",
    output_type=JokeOutput
)

result = Runner.run_sync(agent, input="Tell a joke in JSON")

# Now final_output is a JokeOutput object
print(result.final_output.setup)       # ➤ str
print(result.final_output.punchline)   # ➤ str
Output Example (Structured):


{
  "setup": "Why don't skeletons fight each other?",
  "punchline": "They don't have the guts."
}
🔷 Why final_output is typed as Any?

@property
def final_output(self) -> Any:
    ...
🔹 Reason:
Because of Handoffs (agent A gives control to agent B)

SDK doesn’t know beforehand which agent will finish last

So type can't be fixed (could be str, JokeOutput, EssayOutput, etc.)

🔷 5. Summary Table:
output_type Defined?	Output Format	final_output Type	Access
❌ No	Free text	str	print(result.final_output)
✅ Yes	Structured	Pydantic model	result.final_output.fieldname

