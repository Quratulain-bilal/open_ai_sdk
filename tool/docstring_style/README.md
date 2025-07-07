
🔹 1. sphinx Docstring Style
✅ Format:
"""
Function summary.

:param a: The first number.
:type a: int
:param b: The second number.
:type b: int
:returns: The sum of both numbers.
:rtype: int
"""
🧠 Roman Urdu Explanation:
Sphinx style mein har parameter aur return ka alag tag hota hai:

:param <name>: — parameter ka description

:type <name>: — parameter ki type

:returns: — return value ka explanation

:rtype: — return ki type

Yeh style documentation generators (like Sphinx tool) ke liye standard hai.

📌 SDK Behavior:
Jab docstring_style="sphinx" hota hai, SDK in lines ko read karke function tool ka description aur types extract karta hai — LLM ko samajh aata hai ke a aur b integers hain aur return bhi int hai.

🔹 2. google Docstring Style
✅ Format:
"""
Function summary.

Args:
    a (int): The first number.
    b (int): The second number.

Returns:
    int: The sum of both numbers.
"""
🧠 Roman Urdu Explanation:
Google style mein:

Args: ke andar har argument ki line hoti hai name (type): description format mein.

Returns: section return ka type aur explanation deta hai.

Yeh Google engineers ka mostly use kiya gaya readable aur neat format hai.

📌 SDK Behavior:
Agar aap docstring_style="google" likhte ho, SDK Args: aur Returns: ko parse karta hai, aur samajhta hai kaun se arguments hain, unki types kya hain, aur return value kya hai. LLM is info ko tool generate karte waqt use karta hai.

🔹 3. numpy Docstring Style
✅ Format:

"""
Function summary.

Parameters
----------
a : int
    The first number.
b : int
    The second number.

Returns
-------
int
    The sum of both numbers.
"""
🧠 Roman Urdu Explanation:
Numpy style documentation scientific aur data-science libraries mein use hoti hai.

Parameters section mein har argument ka naam, type aur description alag lines mein hota hai.

Returns section return type aur uska explanation deta hai.

Yeh format structured aur visually clear hota hai for technical documentation.

📌 SDK Behavior:
Jab docstring_style="numpy" hota hai, SDK Parameters aur Returns ko parse karta hai aur LLM ko exact parameter mapping provide karta hai. Isse tools ka interface robust banta hai.
