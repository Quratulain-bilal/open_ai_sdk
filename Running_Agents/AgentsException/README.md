💥 AgentsException (Base Class)
🔹 Kab aata hai?
Generic base class hai. Aap isay sab exceptions ke liye use kar sakte ho, agar specific exception catch na karni ho.

✅ Code Example:

from agents.exceptions import AgentsException

try:
    result = Runner.run_sync(my_agent, input="Hello")
except AgentsException as e:
    print("Kuch problem hui:", e)
🔁 MaxTurnsExceeded
🔹 Kab aata hai?
Jab agent too many turns (loops) chalata hai, aur max_turns limit exceed kar deta hai.

✅ Code Example:

from agents.exceptions import MaxTurnsExceeded

try:
    result = Runner.run_sync(my_agent, input="Hello", max_turns=1)  # Limit set
except MaxTurnsExceeded:
    print("Agent ne allowed turns se zyada bar run kiya!")
🧠 Tip: Har AI response ya tool-call ek "turn" hoti hai.

🧠 ModelBehaviorError
🔹 Kab aata hai?
Model ne invalid output diya, e.g. galat JSON ya tool ka naam jo exist hi nahi karta.

✅ Code Example:

from agents.exceptions import ModelBehaviorError

try:
    result = Runner.run_sync(my_agent, input="Use tool XYZ please.")  # Tool XYZ defined nahi
except ModelBehaviorError as e:
    print("Model ne kuch galat behavior dikhaya:", e)
👨‍💻 UserError
🔹 Kab aata hai?
Jab developer (aap) SDK ka galat use kare.

✅ Code Example:

from agents.exceptions import UserError

try:
    result = Runner.run_sync(my_agent, input={"msg": "Hello"})  # Galat type
except UserError as e:
    print("UserError: Shayad input ka type ya config galat hai:", e)
🧠 input should always be str or list[TResponseInputItem], na ke dict.

🚧 InputGuardrailTripwireTriggered
🔹 Kab aata hai?
Jab input violate karta hai guardrail rule.

✅ Code Example:

from agents.guardrails import InputGuardrail
from agents.exceptions import InputGuardrailTripwireTriggered

class BadWordsGuardrail(InputGuardrail):
    def check(self, input, context=None):
        if "badword" in input.lower():
            return self.fail("No abusive language allowed.")
        return self.ok()

my_agent.input_guardrails = [BadWordsGuardrail()]

try:
    result = Runner.run_sync(my_agent, input="This is a badword")
except InputGuardrailTripwireTriggered as e:
    print("Input ne rule break kiya:", e)
🛡 OutputGuardrailTripwireTriggered
🔹 Kab aata hai?
Jab model ka output violate karta hai guardrail rule (e.g. private info).

✅ Code Example:

from agents.guardrails import OutputGuardrail
from agents.exceptions import OutputGuardrailTripwireTriggered

class NoPhoneNumberGuardrail(OutputGuardrail):
    def check(self, output, context=None):
        if "123-456" in output:
            return self.fail("Phone numbers not allowed.")
        return self.ok()

my_agent.output_guardrails = [NoPhoneNumberGuardrail()]

try:
    result = Runner.run_sync(my_agent, input="Give me your number.")
except OutputGuardrailTripwireTriggered as e:
    print("Output ne guardrail tor diya:", e)
📚 Summary Table with Code Mapping
Exception	Trigger Condition	Code Highlight
AgentsException	Generic SDK error	except AgentsException
MaxTurnsExceeded	Loop exceeded max_turns	max_turns=1
ModelBehaviorError	Model returns invalid output/tool	Tool not defined
UserError	Developer uses SDK wrong	input={"msg": "Hello"}
InputGuardrailTripwireTriggered	Guardrail trip on user input	BadWordsGuardrail()
OutputGuardrailTripwireTriggered	Guardrail trip on model output	NoPhoneNumberGuardrail()

🔚 Final Thought
In sab exceptions ka purpose:

SDK ko safe aur predictable banana

Developer ko controlled flow dena

Production AI apps mein trustworthy systems build kar
