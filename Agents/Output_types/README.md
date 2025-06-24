📦 Output Types 


Official Documentation

Output types
By default, agents produce plain text (i.e. str) outputs. If you want the agent to produce a particular type of output, you can use the output_type parameter. A common choice is to use Pydantic objects, but we support any type that can be wrapped in a Pydantic TypeAdapter - dataclasses, lists, TypedDict, etc.


DETAIL

By default, agent ka output sirf ek normal string (text/str) hota hai, jaise: "Hello, how can I help?".

Lekin agar aap chahein ke output structured format mein aaye (jaise form data), to aap output_type= parameter use kar sakti hain.

Iska faida ye hota hai ke agent specific structure follow karta hai — jaise naam, age, email waghera properly fields mein miltay hain.

Sabse zyada popular output type hota hai Pydantic model, lekin aap dataclass, list, TypedDict waghera bhi use kar sakti ho — bus wo Pydantic ke TypeAdapter se compatible honi chahiye.

Output type set karne se agent input ko samajh kar us format mein automatically convert kar deta hai — aapko manually kuch bhi extract karna nahi padta.

Ye system especially tab useful hota hai jab aap APIs, forms, resume builders, dashboards jese applications bana rahi ho jahan data structured hona zaroori ha