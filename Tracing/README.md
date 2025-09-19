

🔍 Professional Guide: Tracing in OpenAI SDK



1. What is Tracing?

Tracing = Observability system for understanding what’s happening inside your agent or application.

Trace → Represents a single workflow execution (end-to-end journey).

Span → Represents a specific step inside that journey (child operation of a trace).





2. Why Tracing is Important?

1. Debugging → Samajhne ke liye agent ne kya kya steps liye.


2. Monitoring → Workflow ki performance track karna (latency, errors, retries).


3. Auditing → Kis input pe kya output generate hua, easily dekhna.


4. Optimization → Identify karna slow ya redundant steps ko.




---

3. Structure of a Trace

A trace generally consists of:

Trace ID: Unique identifier (SDK generates automatically).

Workflow Name: Developer-defined logical name (e.g. "JokeWorkflow").

Group ID: Multiple traces ko ek conversation ya session ke under link karne ke liye.

Metadata: Extra context (e.g. user ID, environment, app version).


with trace("JokeWorkflow", metadata={"user": "123"}):
    result = await runner.run(agent, "Tell me a joke")


---

4. What is a Span?

Span = Sub-operation under a trace.

Har span ka:

span_id hota hai

parent_id hota hai (agar nested hai)

Timing (start, end, duration)

Data (inputs/outputs/errors)



Types of spans in OpenAI SDK:

AgentSpanData → High-level agent run

GenerationSpanData → LLM response

FunctionSpanData → Tool/function call

GuardrailSpanData → Guardrail evaluation

HandoffSpanData → Agent handoff

TranscriptionSpanData / SpeechSpanData → Audio steps



---

5. Logic: Traces inside Traces (Nested Tracing)

6. 
🔄 Default Behavior

SDK jab aap Runner.run() chalate ho → ek trace ban jata hai.

Us trace ke andar automatically spans create ho jaate hain (LLM call, tool, guardrail, handoff).
👉 Matlab by default: Trace → multiple spans, but sirf ek root trace hota hai.



---

🧩 Custom Multiple / Nested Traces

Agar aap chahte ho:

1. Ek hi session ke andar multiple traces (parallel workflows).


2. Ek trace ke andar sub-traces (nested workflows).



To aapko with trace() ka use karna hoga.


---

1. Multiple Traces (Independent Workflows)

# Workflow 1
with trace("JokeWorkflow"):
    joke = await runner.run(agent, "Tell me a joke")

# Workflow 2
with trace("RatingWorkflow"):
    rating = await runner.run(agent, f"Rate this joke: {joke.final_output}")

➡️ Yahaan dono alag-alag traces banenge (JokeWorkflow aur RatingWorkflow).
Ye ek dusre ke andar nahi hain — independent workflows hain.


---

2. Nested Traces (Trace inside Trace)

with trace("ParentWorkflow") as parent:
    # Parent trace ke andar ek agent run
    result1 = await runner.run(agent, "Generate a story")

    # Ab ek nested trace start karte hain
    with trace("ChildWorkflow", parent_id=parent.id):
        result2 = await runner.run(agent, f"Summarize this story: {result1.final_output}")

➡️ Yahaan:

ParentWorkflow = root trace

ChildWorkflow = nested trace (linked via parent_id)

Iska fayda = monitoring dashboards mein aapko dikhega ke ek workflow ke andar dusra workflow hua.



---

3. Rule of Thumb (Professional Logic)

Use single trace → agar aapko ek hi workflow track karna hai.

Use multiple traces → agar aapko alag workflows ko separate dekhna hai (har ek apna root trace banayega).

Use nested traces → agar ek workflow ke andar ek complex sub-workflow hai (jiska apna detail chahiye).


Example:

Trace: OrderWorkflow

Span: Validate Cart

Span: Apply Discount

Nested Trace: PaymentWorkflow (child trace with its own spans)


7. Default vs Custom Tracing

✅ Default (SDK automatically generates):

Runner.run() → Trace

Agent steps → Spans

LLM calls → GenerationSpan

Tool invocations → FunctionSpan


🎯 Custom (Developer-defined):

Aap apne events ko bhi trace kar sakte ho:

with custom_span("DatabaseQuery", metadata={"query": "SELECT * FROM users"}):
    data = db.run("SELECT * FROM users")


---

7. Handling Sensitive Data

By default → LLM inputs/outputs, tool calls log ho jaate hain.

Agar sensitive hai (PII, passwords, tokens) → disable with:


RunConfig(trace_include_sensitive_data=False)


---

8. Trace Export and Processors

SDK ka default processor traces ko OpenAI Dashboard bhejta hai.

Aap custom processors laga sakte ho:

Send to observability tools (W&B, Langfuse, MLflow, Datadog).

Replace OpenAI backend if needed.



runner = Runner(config=RunConfig(processor=MyCustomProcessor()))


---

9. Best Practices (Professional Logic)

1. Keep traces focused: Ek trace = ek workflow. Don’t overload.


2. Use metadata wisely: User/session info add karo taake context clear ho.


3. Error handling spans: Agar error aaye, usko trace ke andar log karo.


4. Don’t log sensitive data: Always respect privacy.


5. Use nested traces for modular workflows: Independent steps should have their own sub-traces.


6. Correlate with logs/metrics: Combine traces with logging/metrics for full observability.






10. Visual Flow

Trace: "OrderWorkflow" (trace_id=1)
 ├── Span: "ValidateCart" (span_id=11)
 ├── Span: "ApplyDiscount" (span_id=12)
 └── Span: "ProcessPayment" (span_id=13)
      └── Trace: "PaymentGatewayTrace" (trace_id=2)
            ├── Span: "CardValidation" (span_id=21)
            ├── Span: "FraudCheck" (span_id=22)
            └── Span: "PaymentConfirmation" (span_id=23)




✅ In short:
Tracing in OpenAI SDK = A structured way to record, debug, and monitor workflows using Traces (big picture) and Spans (small steps). You can nest traces logically, add custom spans, control sensitive data, and export traces for observability.



