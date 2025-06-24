🧠 What is Runner.run_sync()?

official Documentation 
Run a workflow synchronously, starting at the given agent. Note that this just wraps the run method, so it will not work if there's already an event loop (e.g. inside an async function, or in a Jupyter notebook or async context like FastAPI). For those cases, use the run method instead. The agent will run in a loop until a final output is generated. The loop runs like so: 1. The agent is invoked with the given input. 2. If there is a final output (i.e. the agent produces something of type agent.output_type, the loop terminates. 3. If there's a handoff, we run the loop again, with the new agent. 4. Else, we run tool calls (if any), and re-run the loop. In two cases, the agent may raise an exception: 1. If the max_turns is exceeded, a MaxTurnsExceeded exception is raised. 2. If a guardrail tripwire is triggered, a GuardrailTripwireTriggered exception is raised. Note that only the first agent's input guardrails are run. Args: starting_agent: The starting agent to run. input: The initial input to the agent. You can pass a single string for a user message, or a list of input items. context: The context to run the agent with. max_turns: The maximum number of turns to run the agent for. A turn is defined as one AI invocation (including any tool calls that might occur). hooks: An object that receives callbacks on various lifecycle events. run_config: Global settings for the entire agent run. previous_response_id: The ID of the previous response, if using OpenAI models via the Responses API, this allows you to skip passing in input from the previous turn. Returns: A run result containing all the inputs, guardrail results and the output of the last agent. Agents may perform handoffs, so we don't know the specific type of the output.

Details

Runner.run_sync() aik synchronous method hai jo OpenAI Agents SDK ka part hai. Iska kaam hai:

✅ Ek agent se AI workflow start karna
✅ Har step ko evaluate karna
✅ Jab tak final output na mil jaye, process ko loop mein chalate rehna

Yeh method un scenarios mein useful hoti hai jahan tum asynchronous programming use nahi kar rahe ho — jaise:

Normal Python scripts

CLI-based tools

Simple command line apps

Educational examples

Testing environments



🧩 Core Functionality: How Does run_sync() Work?
🔁 Loop-based Execution
run_sync() aik loop mein agent ko baar baar run karta hai jab tak:

Agent final output de de

Ya handoff ho kisi naye agent ko

Ya tool call ho jaye

Ya koi error ya max_turn exceed ho jaye

🧭 Internal Steps (Conceptually)
text
Copy
Edit
1. Start from Agent A
2. Agent A gets input from user
3. Agent checks: Is this my final output?
     → YES: return output
     → NO:
         a. Any tool to call?
         b. Any new agent to handoff?
         c. Go again (loop continues)
4. Return result as RunResult object


🛠️ run_sync() Function Signature
python
Copy
Edit
Runner.run_sync(
  starting_agent,
  input,
  context = None,
  max_turns = 20,
  hooks = None,
  run_config = None,
  previous_response_id = None
) → RunResult
📦 Lifecycle Breakdown (Inside Out)
1. Input Received
starting_agent = wo agent jo pehle task handle karega.

input = user ka message ya list of structured items.

Example:

python
Copy
Edit
writer_agent = Agent(name="Writer", instructions="Write stories")
Runner.run_sync(writer_agent, input="Write about AI")
2. Internal Loop Starts
Jese async run() mein hota hai, yahan bhi loop chalta hai internally until koi final response milta hai.


LOOP:
    Call agent
    Check response
    -> Final Output?
    -> Tool Call?
    -> Handoff?
    -> Repeat if needed
3. Final Output Produced
Loop ke end mein agent ek complete output return karta hai:


response = Runner.run_sync(...)
print(response.final_output)
Yahan koi stream ya chunks nahi hotay. Tum sirf final aggregated response dekhte ho.

