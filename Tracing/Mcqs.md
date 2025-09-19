
🧠 20 Advanced MCQs on Tracing in OpenAI SDK


---

Q1.

If you call Runner.run() without explicitly wrapping it in with trace(...), what happens by default?
A. No trace is created, only spans are recorded
B. A single trace is automatically created containing spans for the agent, tools, and LLM calls ✅
C. A root trace plus a child trace are created
D. Only agent spans are recorded


---

Q2.

If you create a nested trace using with trace("Child", parent_id=parent.id) but the parent_id does not exist, what logically happens?
A. A runtime error is thrown
B. The SDK automatically promotes the trace to a new root trace ✅
C. The child trace is discarded silently
D. The SDK merges it into the nearest span


---

Q3.

Which of the following is true about the relationship between traces and spans?
A. A trace can exist without any spans
B. A span can exist without a parent trace
C. All spans must belong to exactly one trace ✅
D. A trace can belong to multiple spans simultaneously


---

Q4.

By default, which of the following events are NOT wrapped in spans?
A. Agent executions
B. Guardrail checks
C. Random Python exceptions ✅
D. LLM generations


---

Q5.

Suppose you want to combine multiple sequential Runner.run() calls into one single trace. What is the correct approach?
A. Pass group_id manually to each run
B. Wrap both runs inside with trace("workflow") ✅
C. Set RunConfig.trace_id explicitly for each run
D. Use custom_span()


---

Q6.

Which parameter allows you to disable recording sensitive data (like LLM inputs/outputs) inside traces?
A. RunConfig.tracing_disabled
B. RunConfig.trace_include_sensitive_data=False ✅
C. Trace.sensitive=False
D. SpanData.hidden=True


---

Q7.

If OPENAI_AGENTS_DISABLE_TRACING=1 is set in the environment, what is the behavior?
A. Tracing is disabled globally ✅
B. Tracing is disabled only for the current run
C. Tracing is replaced with no-op spans
D. Sensitive data is hidden, but traces still exist


---

Q8.

Which of the following spans are automatically parented under a speech group span?
A. Guardrail spans
B. Transcription and speech spans ✅
C. Handoff spans
D. Generation spans


---

Q9.

If you manually call trace.start() and trace.finish() without passing mark_as_current or reset_current, what potential problem arises?
A. The trace will not generate any spans
B. Concurrency context will lose track of the current trace ✅
C. The trace will automatically restart at the next span
D. The SDK raises an exception


---

Q10.

Which of the following correctly describes metadata in a trace?
A. Used only for internal OpenAI systems
B. Optional key–value data attached to a trace ✅
C. Required for parent-child linking of spans
D. Automatically filled with model settings


---

Q11.

What is the role of the TraceProvider in the tracing architecture?
A. Responsible for creating spans
B. Responsible for exporting traces to OpenAI’s backend
C. Responsible for creating traces ✅
D. Responsible for running RunConfig


---

Q12.

When using add_trace_processor(), what happens?
A. It replaces the default backend exporter
B. It adds an additional processor that receives traces alongside the default backend ✅
C. It disables OpenAI’s backend tracing
D. It disables sensitive data capture


---

Q13.

Which of the following is true for custom_span()?
A. It cannot be nested inside another span
B. It always starts a new trace
C. It allows developers to record arbitrary operations as spans ✅
D. It is automatically created by the SDK


---

Q14.

What is the difference between trace() and custom_span()?
A. trace() creates a top-level container of spans; custom_span() creates a child operation ✅
B. trace() always requires a parent ID, custom_span() doesn’t
C. trace() is optional, custom_span() is mandatory
D. Both are equivalent, just syntactic sugar


---

Q15.

If two different traces share the same group_id, what is the purpose?
A. To merge spans from both traces into one trace
B. To logically link related traces, such as a single chat thread ✅
C. To avoid duplicate trace IDs
D. To allow sensitive data capture across traces


---

Q16.

Which of the following is NOT automatically traced?
A. Tool function calls
B. Transcription of speech inputs
C. Manual Python logging statements ✅
D. Text-to-speech output


---

Q17.

If an organization is under Zero Data Retention (ZDR) policy, what happens to tracing?
A. Only metadata traces are allowed
B. All tracing is disabled ✅
C. Tracing continues but without sensitive data
D. Only custom spans are recorded


---

Q18.

What is the main difference between set_trace_processors() and add_trace_processor()?
A. set_trace_processors() adds processors, add_trace_processor() replaces them
B. set_trace_processors() replaces default processors ✅, add_trace_processor() adds alongside existing ones
C. Both do the same
D. Neither affects backend export


---

Q19.

What is the role of contextvars in tracing?
A. To manage trace persistence across sessions
B. To track the current active trace/span automatically in concurrent execution ✅
C. To encrypt sensitive data inside spans
D. To merge multiple group_ids


---

Q20.

When tracing non-OpenAI models with LitellmModel, how does tracing still work?
A. By disabling tracing and re-enabling manually
B. By setting set_tracing_export_api_key() with an OpenAI API key ✅
C. By wrapping every span manually with custom_span
D. Tracing is not possible at all


