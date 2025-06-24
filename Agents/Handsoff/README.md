
📚 Handoffs in OpenAI Agents SDK 


🌐 Official Documentation 

Handoffs are sub-agents that the agent can delegate to. You provide a list of handoffs, and the agent can choose to delegate to them if relevant. This is a powerful pattern that allows orchestrating modular, specialized agents that excel at a single task. Read more in the handoffs documentation.




🌐 What are Handoffs?
“Handoff” ka matlab hota hai: ek agent se doosray agent ko zimmedari dena.




📌 Why Use Handoffs?
Alag alag agents ko unka expert kaam dena

Agents ko manageable aur clean banana

Complex workflows ko modular banana

AI ko guide karna ke kis agent ko kab trigger karna hai

🔍 Handoff Parameters (1-by-1 With Examples)
✅ 1. agent (required)
Ye batata hai kis agent ko handoff karna hai.

handoff(
    agent=refund_agent  # 🤖 Ye agent handle karega user ka refund query
)
✅ 2. tool_name_override
AI jab handoff tool call karta hai, uska naam hota hai like transfer_to_refund_agent.
Aap apni marzi se naam rakh sakte ho taake zyada clear ho.

handoff(
    agent=refund_agent,
    tool_name_override="ask_refund"
)
🔹 Is se LLM ko clearly samajh aata hai: “agar refund ka sawal ho toh ask_refund use karo.”

✅ 3. tool_description_override
LLM ko tool samjhanay ke liye short description dena helpful hota hai.


handoff(
    agent=refund_agent,
    tool_description_override="Use this tool when user asks refund-related questions"
)
📎 Tip: Description jitna natural hoga, utna behtar LLM samjhega.

✅ 4. on_handoff
Jab bhi handoff trigger ho, aapka custom function call hoga.
Useful for: logging, notifications, DB save, input validate, etc.


from agents import RunContextWrapper

async def on_handoff_log(ctx: RunContextWrapper[None]):
    print("📝 Handoff has been triggered!")

handoff(
    agent=refund_agent,
    on_handoff=on_handoff_log
)
✅ 5. input_type
Jab aap chahein ke LLM user input se structured data extract kare, to yeh parameter lagta hai.


from pydantic import BaseModel

class RefundInput(BaseModel):
    reason: str

handoff(
    agent=refund_agent,
    input_type=RefundInput
)
🧠 Ab LLM try karega user message se "reason" nikaalne ka, aur on_handoff() ya agent ko de dega.

✅ 6. input_filter
Agar aap nahi chahte ke next agent ko puri history ya tool calls milein — use this.


from agents.extensions import handoff_filters

handoff(
    agent=refund_agent,
    input_filter=handoff_filters.remove_all_tools
)