 Lifecycle Hooks
🧠 Official_Documentation 
Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, or pre-fetch data when certain events occur. You can hook into the agent lifecycle with the hooks property. Subclass the AgentHooks class, and override the methods you're interested in.



🔁 Lifecycle Events (Hooks) – Explained
Kabhi kabhi aap chahte hain ke jab agent kuch important step perform kare (jaise start hona, koi tool chalana, ya kaam finish karna), to aap ko uss event ka record ya notification mil jaye — isi liye "hooks" ka use hota hai.

Hooks allow you to monitor and control what happens before, during, and after the agent runs. Think of hooks as event listeners.

🧠 What are Agent Hooks?
Hooks are custom Python classes where you can define async methods like:

on_start() – jab agent start hota hai

on_tool_start() – jab koi tool start hota hai

on_tool_end() – jab tool apna kaam complete karta hai

on_end() – jab agent apna final output return karta hai

Ye sab functions automatically call ho jate hain agar aap ne hooks=YourHookClass() agent mein diya ho.