🔸 Normal Class (bina @dataclass)

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Ali", 20)
print(p)   # Person(name=Ali, age=20)

👉 Yahan humne __init__ aur __repr__ manually likha.


---

🔸 Same Class with @dataclass

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Ali", 20)
print(p)   # Person(name='Ali', age=20)

👉 Yahan humein __init__ ya __repr__ likhne ki zarurat nahi — @dataclass automatically bana deta hai.


---

🔹 Fayda kya mila?

Boilerplate code kam ho gaya.

Sirf attributes likhne hain, baaki sab Python sambhal lega.

Readable aur clean code banta hai.



---

🔹 Aur Pydantic ka kya role hai?

Normal @dataclass validation nahi karta. Agar tum "20" string daal do age me, wo accept kar lega.

Lekin pydantic.dataclasses.dataclass validation add kar deta hai.
Matlab wohi dataclass style, lekin andar se Pydantic ka validation engine use hota hai.



---

👉 Easy way:

@dataclass (Python built-in) → Auto __init__, __repr__… but no validation.

@pydantic.dataclasses.dataclass → Same auto features + validation (age="20" → int(20), warna error).

