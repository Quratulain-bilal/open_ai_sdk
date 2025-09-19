

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

Kabhi ek trace ke andar aur trace dikhana zaroori hota hai.
👉 Example: Ek e-commerce agent workflow:

1. User query aaya → Trace: CheckoutWorkflow


2. Inside this workflow:

Span: Validate cart

Span: Apply discount code

Span: Payment process

Iske andar ek sub-trace bana sakte ho (PaymentGatewayTrace)

Span: Card validation

Span: Fraud check

Span: Payment confirmation






🔑 Rule of thumb:

Agar step independent aur complex workflow hai → use a new trace.

Agar step workflow ka part hai → keep it as a span.



---

6. Default vs Custom Tracing

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



