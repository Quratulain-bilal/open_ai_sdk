 What Is Agent Cloning?


OFFICIAL_DOCUMENTATION

By using the clone() method on an agent, you can duplicate an Agent, and optionally change any properties you like.


Details
Sometimes aap ko ek base agent banana hota hai with common instructions, tools, and model. Aur usi agent ki multiple versions chahiyein with thoda different behavior.

Is case mein aap Agent.clone() method use kar sakte hain to duplicate the original agent without writing everything again.

✅ Why Use clone()?

Ek base agent banao, then customize jitne versions chaaho

Performance efficient hai, maintain karna easy hota hai

Large multi-tasking bots ke liye perfect (jaise: sales bot, refund bot, info bot from same template)