📘 Pydantic Models vs Dataclasses (V2)


1. BaseModel (recommended, full-featured)


2. pydantic.dataclasses.dataclass (lightweight validation wrapper)



Dono ka purpose structured aur validated data create karna hai, lekin use-case different hain.


---

🔹 1. BaseModel

BaseModel Pydantic ka primary aur recommended approach hai. Ye full power deta hai:

✅ Built-in methods (.model_dump(), .model_validate(), .model_dump_json(), etc.)
✅ JSON schema generation
✅ Strong ecosystem support (settings, ORM, validators, computed fields)
✅ Direct integration with FastAPI, SQLModel, etc.
✅ Advanced config options (extra, validate_assignment, etc.)

Example:

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"

user = User(id="42")
print(user)  # id=42 name='John Doe'
print(user.model_dump_json(indent=2))


---

🔹 2. pydantic.dataclasses.dataclass

Agar tumhe Python’s built-in dataclasses pasand hain, lekin validation chahiye, to use @pydantic.dataclasses.dataclass.
Ye bilkul dataclasses.dataclass ki tarah behave karta hai, bas validation add karta hai.

⚠️ Limitations:

No .model_dump_json() (use RootModel or TypeAdapter)

Less ecosystem integration (not as flexible as BaseModel)

Some config options (extra='allow') supported nahi hain


Example:

from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None

user = User(id="42", signup_ts="2032-06-21T12:00")
print(user)  
# User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))


---

🔹 3. Major Differences

Feature	BaseModel ✅	Dataclass ⚠️

Validation	✔	✔
.model_dump() / .model_dump_json()	✔	❌ (need RootModel)
JSON Schema (.json_schema())	✔	Only via TypeAdapter
Ecosystem Support (FastAPI, ORM, Settings)	✔ Best	❌ Limited
Initialization Hooks	@model_validator	Works but slightly different
Config Options	Full support	Limited (no extra='allow')
Speed	Slightly slower	Slightly faster (less overhead)



---

🔹 4. When to Use What?

✅ Use BaseModel

Jab tum APIs, databases, configs, ORMs, JSON serialization ke sath kaam kar rahe ho

Jab tumhe ecosystem compatibility aur rich features chahiye

Ye default & recommended option hai


✅ Use Dataclass

Agar tumhe simple validation + dataclass style chahiye

Jab tum lightweight object banana chahte ho, bina full Pydantic power ke

Jab tumhara use-case internal computation hai, na ke JSON APIs



---

🔹 5. Example Comparison

BaseModel

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

p = Product(id="10", name="Coffee", price="99.9")
print(p.model_dump_json(indent=2))

Dataclass

import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

p = Product(id="10", name="Coffee", price="99.9")
print(p)  
# Product(id=10, name='Coffee', price=99.9)

Notice:

BaseModel → built-in JSON support

Dataclass → print hota hai, lekin JSON ke liye RootModel ya TypeAdapter lagana parta hai
