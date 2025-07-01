
✅ OpenAI Agents SDK – Hooks Lifecycle 
🔁 What Are Hooks?
Hooks wo special functions hote hain jo agent ya runner ke lifecycle ke specific points par automatically trigger hote hain. Unmein aap custom logging, validation, monitoring, ya delegation logic inject kar sakte ho.

🧠 Core Types of Hooks
1. RunHooks (System-Level)
Yeh har agent, tool, ya step ke upar chalta hai.

Agar aap custom run hook nahi dete to SDK khud default RunHooks() inject karta hai.


if hooks is None:
    hooks = RunHooks()
✅ Always active, even if not specified.

2. AgentHooks (Agent-Specific)
Sirf us agent ke liye chalta hai jisko aapne explicitly hooks= diya ho.

Default behavior: koi hook nahi chalta unless explicitly diya jaye.

🔒 Must be assigned manually to each agent:
agent = Agent(..., hooks=CustomAgentHook())

⚙️ Common Lifecycle Hook Functions
Hook Function	Triggered When...	Parameters Injected by SDK
on_start	Agent starts running	context, agent
on_tool_start	Tool is about to run	context, agent, tool
on_tool_end	Tool execution finishes	context, agent, tool, result
on_end	Agent gives final output	context, agent, output
on_handoff	Agent hands off to another agent	context, from_agent, to_agent (in AgentHooks)
on_agent_start	Runner begins running an agent	context, agent
on_agent_end	Runner finishes an agent	context, agent, output

🧩 Parameter Injection: Who Gives What?
Jab aap ye define karte ho:


async def on_tool_end(self, context, agent, tool, result):
Aap sirf function banate ho — values nahi bhejte.
✅ OpenAI SDK khud deta hai:
context: RunContextWrapper — user ka state, memory, inputs

agent: jis agent ke andar hook run ho raha hai

tool: function_tool ya class-based tool jo agent use kar raha hai

result: tool ka output ya agent ka final response

from_agent, to_agent: handoff ke waqt 2 agents

❗ Agar aap parameters na likho ya galat likho, SDK inject nahi kar paayega → TypeError


1️⃣ Base Classes: Abstraction vs Default Class
❓ Are RunHooks and AgentHooks Abstract Base Classes (ABCs)?
❌ Nahi! Yeh abstract class nahi hain — yeh simple base classes hain jinke methods ke andar default empty definitions hain (pass).

📌 Meaning:
Aap override karo toh aapka logic chalega

Aap kuch bhi override na karo toh SDK error nahi karega

SDK safely on_start(), on_tool_start() waghera call kar sakta hai bina check kiye ke method present hai ya nahi


✅ Hook functions ke parameters positional hote hain kyunki:

SDK aapke defined function ko directly positional arguments ke through call karta hai

Isliye agar aap unka order galat likhen, ya kisi ko skip karen, toh Python TypeError de deta hai

SDK koi kwargs ya ** spread use nahi karta
(Jaise: func(context=context, agent=agent) nahi karta)



