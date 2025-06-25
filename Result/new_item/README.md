📦 new_items 
new_items har wo event ya action represent karta hai jo agent run ke dauraan hua. Har item aik RunItem class ka object hota hai, jisme LLM ka raw output ya action encapsulated hota hai.

Lifecycle flow simple hai:

User input Runner ko diya gaya.

Agent run start hoti hai — prompt model ko diya jata hai.

Jo bhi step hota hai (message, tool call, handoff) → wo as RunItem capture hota hai.

Ye sab sequentially new_items list me store hote jate hain.

RunItem types & meanings:

MessageOutputItem: LLM ne koi jawab ya message banaya.

ReasoningItem: LLM ne soch express ki.

ToolCallItem: Tool ko call kiya gaya.

ToolCallOutputItem: Tool ka result mila.

HandoffCallItem: Kisi agent ko forward karna decide hua.

HandoffOutputItem: Agent handoff ke result ka item.

Purpose:
Ye list developer ko ye samajhne deti hai ke model ne kya kya socha, kya step liya, kis sequence me, taake aap debugging, logging, ya display me accurate information use kar saken.

Example short logic:


Input: "What is the weather in Karachi?"

new_items:
├── ReasoningItem → "Let's check the weather using a tool"
├── ToolCallItem → Call: weather_lookup(city="Karachi")
├── ToolCallOutputItem → Response: "30°C and sunny"
├── MessageOutputItem → "The weather in Karachi is 30°C and sunny."
