✅ Coding + Theoretical Questions on OpenAI Agents SDK (Hooks Focused)

1. What design principle allows RunHooks to work even if not explicitly defined?
2. Why are hook method parameters strictly positional, not keyword-based?
3. Why must you manually assign AgentHooks but not RunHooks?
4. What happens if your on_tool_start hook is defined with the wrong number of parameters?
5. Why are RunHooks called a "global observer" while AgentHooks are called "local decorators"?
6. What is the lifecycle flow of hooks during a successful tool execution?
7. How do RunHooks and AgentHooks interact in a multi-agent system?
8. What’s the implication of having default pass implementations in RunHooks base class?
9. Can RunHooks be used to manipulate the tool output directly? Why or why not?
10. What hook(s) will be triggered if a tool raises an exception inside an agent?
11. In on_handoff, what lifecycle event is it connected to and what parameters does it receive?
12. Why doesn’t the SDK auto-inject AgentHooks like it does with RunHooks?
13. What is the execution order of the following hooks when a tool is called:
RunHooks.on_tool_start

AgentHooks.on_tool_start

Tool Execution

AgentHooks.on_tool_end

RunHooks.on_tool_end

14. Why can hooks mutate context.context, and why might that be dangerous?
15. How would you use hooks to trace and audit user flow across agents?
⚙️ SECTION 2: Advanced Coding and Debug Questions (15)
16. Given a hook that logs every tool execution, how would you implement a timeout tracker?
Hint: Use time.time() in on_tool_start and on_tool_end.

17. You want to skip on_tool_start for tools named "internal_logger". Write the condition.
18. Create a custom AgentHooks class that logs the agent name at the beginning and end.
19. Write a RunHooks implementation that stops the agent from running if the user is under 18.
20. How can you track the number of times each tool is used using a shared context attribute?
21. Refactor this hook so it logs duration and tool output only if tool name != "healthCheck":
python
Copy
Edit
async def on_tool_end(self, context, agent, tool, result):
    ...
22. Simulate a system where Agent A hands off to Agent B, and Agent B uses AgentHooks. What hooks will run?
23. Debug this faulty hook:
python
Copy
Edit
async def on_tool_end(self, result, context, agent, tool):
    ...
What's wrong with the method?

24. Write a hook that sets a flag ctx.metadata["warn"] = True if tool output contains "error".
25. Extend your on_end hook to log the final output only if its length > 200 characters.
26. Create a hook setup where RunHooks log to file and AgentHooks log to console.
27. Write an async on_agent_end that posts tool result to an external API.
28. Design a FallbackHooks that swaps agent execution based on output content.
29. How would you use metadata inside RunContextWrapper to share values between hooks? Give code example.
30. Build a dual-agent system where agent A validates input, and if valid, passes to agent B. Use hooks to log full context transition.
