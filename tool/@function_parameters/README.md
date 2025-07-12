##@functiontoll
🔹 1. name_override

✅ Kya karta hai?
Is parameter se aap apne function ka tool name manually specify kar sakte ho.


Normally, function ka naam hi tool ka naam ban jaata hai. Agar aap name_override="add_numbers" likhtay ho, to SDK function ka naam add_in_google_style ho ya kuch bhi, tool ka naam add_numbers set karega.

🔧 Use Case:
Agar multiple functions ka logic same hai lekin docstring style alag hai (jaise testing ke liye), to aap sabko ek hi name_override dekar ek naam se tool bana sakte ho.

🔹 2. description_override


✅ Kya karta hai?
Aap manually tool ka description provide kar sakte ho, jo LLM ko samjhata hai ke tool kya karta hai.


Agar aap docstring se description lena nahi chahte ya aapka function description alag dena chahte ho, to yahan description_override="Add two numbers" likh sakte ho.

🔧 Use Case:
Docstring short ho ya specific instructions chahiye ho to manual override kaam aata hai.

🔹 3. use_docstring_info


✅ Default: True

Agar aap chahte hain ke SDK aapki docstring se tool ke parameters, types, aur return value extract kare to ise True rakhein.
Agar aap manually name_override, description_override, ya dusre metadata de rahe ho, to False bhi kar sakte ho.

🔧 Use Case:
Agar aap apni docstring follow nahi kar rahe ya custom info chahiye ho.

🔹 4. docstring_style


✅ Options:
"google"

"numpy"

"sphinx"


Yeh batata hai SDK ko ke docstring kis format mein likhi gayi hai. Us format ke mutabiq SDK parameters aur return type extract karta hai.

🔧 Use Case:
Correct format specify karna zaroori hai taake LLM accurate schema samajh sake.

🔹 5. hidden
✅ Default: False



Agar aap tool ko LLM ke samne hide karna chahte ho (means wo suggestable na ho), to hidden=True kar dein. Tool backend mein available hoga, lekin LLM ko nahi dikhai dega.

🔧 Use Case:
Sensitive tools ya internal-only tools ko expose nahi karna ho.

🔹 6. manual_schema



✅ Kya karta hai?
Yeh allow karta hai ke aap function ka OpenAI-style JSON schema manually define karo.

Normally SDK khud schema bana deta hai, lekin agar aapko poora schema control karna ho to yeh use hota hai.

🔧 Use Case:
Advance use cases jahan SDK ke auto-generated schema se kaam na chale.

🔹 7. tool_config


✅ Kya karta hai?
Yeh tool ke liye advanced configuration deta hai — jaise ki tool_choice, parallel, stop_on_first_tool, etc. Lekin zyada use Agent() level par hota hai.
