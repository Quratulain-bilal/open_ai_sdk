


# 🧠 Pydantic v2 Ultimate Mastery Quiz   
*Test your deep understanding of Pydantic v2 — validation, serialization, settings, TypeAdapter, Field, validators, and more.*

## 📝 Questions


### 1. You are defining a Pydantic model for a user profile. You want to ensure the `username` field is provided, has a minimum length of 3, and a maximum length of 20. Which of the following `Field` definitions is **CORRECT**?

```python
a) username: str = Field(..., min_length=3, max_length=20)
b) username: str = Field(min_length=3, max_length=20)
c) username: str = Field(default=..., min_length=3, max_length=20)
d) username: str = Field(None, min_length=3, max_length=20)
```

---

### 2. Consider the following code snippet:

```python
from pydantic import BaseModel, ValidationError

class Data(BaseModel):
    value: int

try:
    obj = Data(value="not_a_number")
except ValidationError as e:
    error_messages = e.errors()
```

**What is the structure of a single element in the `error_messages` list?**

```python
a) {'field': 'value', 'error': 'type_error.integer'}
b) {'loc': ('value',), 'msg': 'Input should be a valid integer', 'type': 'int_type'}
c) {'location': 'value', 'message': 'value is not a valid integer'}
d) ('value', 'Input should be a valid integer')
```

---

### 3. You are parsing data from an API that uses `camelCase` keys into a model with `snake_case` attributes. The API sends `{"userName": "Ali"}`. Which model definition will correctly parse this into an attribute named `user_name`?

**a)**
```python
class User(BaseModel):
    user_name: str
```

**b)**
```python
class User(BaseModel):
    user_name: str = Field(alias="userName")
```

**c)**
```python
class User(BaseModel):
    userName: str
```

**d)**
```python
class User(BaseModel):
    user_name: str = Field(validation_alias="userName")
```

---

### 4. What is the primary purpose of a `@field_validator` decorator in Pydantic?

```python
a) To define custom serialization logic for converting a model to JSON.
b) To enforce type hints that are not natively supported by Python.
c) To implement custom, application-specific rules on a field's value beyond basic type checking.
d) To create an alias for a field name during data input.
```

---

### 5. You want to create a settings management class that reads the `DEBUG` environment variable, defaulting to `False` if it's not set. Which import and class definition is **CORRECT** for Pydantic v2?

**a)**
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
```

**b)**
```python
from pydantic import BaseModel

class Settings(BaseModel):
    debug: bool = False
```

**c)**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
```

**d)**
```python
import os
from pydantic import BaseModel

class Settings(BaseModel):
    debug: bool = os.getenv('DEBUG', False)
```

---

### 6. What is the key functional difference between Pydantic's standard (lax) mode and strict mode, as demonstrated by `StrictInt`?

```python
a) Lax mode is faster, while strict mode includes more detailed error messages.
b) Lax mode allows type coercion (e.g., string "123" to integer 123), while strict mode requires the exact type.
c) Strict mode allows for custom validators, while lax mode only uses built-in validators.
d) Lax mode requires all fields to be provided, while strict mode makes all fields optional.
```

---

### 7. How do you serialize a Pydantic model instance `user` into a Python dictionary in v2?

```python
a) user.dict()
b) user.to_dict()
c) user.model_dump()
d) dict(user)
```

---

### 8. You need to validate a simple list of integers without defining a full model. Which Pydantic v2 feature is most appropriate?

```python
a) Using a @dataclass validator
b) Creating a custom BaseModel with a single field of type list[int]
c) Using the TypeAdapter class
d) Using a Field validator with each_item=True
```

---

### 9. You define the following model:

```python
from pydantic import BaseModel

class M(BaseModel):
    x: int
    y: int = 10
```

**What happens when you instantiate it with `M(x=1)`?**

```python
a) A ValidationError is raised because y is not provided.
b) It succeeds, and the instance has values x=1, y=10.
c) It succeeds, and the instance has values x=1, y=None.
d) It succeeds only if y is explicitly set to None.
```

---

### 10. What is the main advantage of using `pydantic.dataclasses` over standard library `dataclasses`?

```python
a) pydantic.dataclasses are automatically frozen (immutable).
b) pydantic.dataclasses automatically generate a GUI form.
c) pydantic.dataclasses provide data validation on instantiation.
d) pydantic.dataclasses have a smaller memory footprint.
```

---

### 11. The `model_json_schema()` method of a Pydantic model generates:

```python
a) A sample JSON output based on the model's default values.
b) A JSON object that describes the model's structure, following the JSON Schema specification.
c) A JSON string that can be used to configure a Pydantic settings object.
d) A serialized version of the model's current instance data.
```

---

### 12. In the context of performance, why is Pydantic considered fast?

```python
a) It is written entirely in C++.
b) It uses lazy evaluation for all validators.
c) Its core validation logic is implemented in Rust.
d) It doesn't perform any validation until explicitly called.
```

---

### 13. What does the `...` (Ellipsis) signify when used as the first argument to the `Field` function?

```python
a) It indicates that the field is optional and can be omitted.
b) It indicates that the field has no default value and must be provided.
c) It is a placeholder for a future default value.
d) It enables strict mode for that specific field.
```

---

### 14. You want to add a validator that checks if an `age` field is 18 or older. Where should the `@field_validator` decorator be placed?

```python
a) On a standalone function that takes the model and value as arguments.
b) On a static method within the model class.
c) On a class method within the model class that takes the cls and value as arguments.
d) On an instance method within the model class that takes self and value as arguments.
```

---

### 15. Which of the following statements about Pydantic's type handling is **FALSE**?

```python
a) It can automatically convert a string representing a datetime into a datetime object.
b) It can validate a field against a union of types, e.g., int | str.
c) It can convert a string like "123" into an integer, even without strict mode.
d) It can natively validate and parse arbitrary generic Python objects without any setup.
```

---

### 16. You receive the following validation error output:

```python
[{'type': 'int_parsing', 'loc': ('id',), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'abc'}]
```

**What was the most likely input?**

```python
a) {"id": 123}
b) {"id": "123"}
c) {"id": "abc"}
d) {"id": None}
```

---

### 17. Which of these is **NOT** a valid way to provide a default value for a field in a Pydantic model?

```python
a) name: str = "John Doe"
b) name: str = Field(default="John Doe")
c) name: str = Field("John Doe")
d) name: str = Field(default_factory="John Doe")
```

---

### 18. The `ValidationError` object provides two primary attributes for understanding what went wrong: `errors()` and `__str__()`. What is the key difference?

```python
a) errors() returns a list of detailed error dictionaries, while __str__() returns a single, formatted string message.
b) errors() is for development, while __str__() is for production logging.
c) __str__() returns the raw input data, while errors() returns the corrected data.
d) There is no difference; they return the same information in different formats.
```

---

### 19. You want a field to be available for validation and serialization but **not included** when dumping the model to a dictionary with `model_dump()`. Which parameter of `Field` would you use?

```python
a) include=False
b) exclude=True
c) dump_default=False
d) serialize=False
```

---

### 20. What is the purpose of the `alias` parameter in the `Field` function?

```python
a) It allows one field to use the validator from another field.
b) It provides an alternative name for the field when accepting input data.
c) It creates a synonym for the field type, e.g., str or int.
d) It defines a different name to be used when the model is serialized to JSON.
```

---

### 21. Consider this code:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)

p = Product(name="Book", price=10.5) # A
p = Product(name="Book", price=0.0)  # B
```

**What is the outcome?**

```python
a) Both A and B will succeed.
b) A will succeed, B will raise a ValidationError.
c) A will raise a ValidationError, B will succeed.
d) Both A and B will raise a ValidationError.
```

---

### 22. How does Pydantic primarily leverage Python's type hints?

```python
a) As runtime specifications for data validation and parsing.
b) Only for static type checking with tools like mypy; they are ignored at runtime.
c) To generate database migration scripts automatically.
d) To create HTML documentation for the model.
```

---

### 23. You are building a high-throughput API. Why is Pydantic a good choice for processing request data?

```python
a) Because it is written in pure Python, making it easy to debug.
b) Because its Rust-based core makes it very fast at parsing and validation.
c) Because it automatically generates API documentation.
d) Because it requires no model definitions, speeding up development.
```

---

### 24. What is the correct way to handle a situation where a field can either be an integer or `None`?

```python
a) value: int = None
b) value: int | None = None
c) value: Optional[int]
d) Both b and c are correct.
```

---

### 25. The `@field_validator` decorator for a field named `email` should be written as:

```python
a) @field_validator("email")
b) @field_validator(email)
c) @field_validator(field="email")
d) @field_validator(for="email")
```

---

### 26. What does the `ge` parameter stand for in `Field(..., ge=18)`?

```python
a) "generate example"
b) "greater than or equal"
c) "generic error"
d) "get environment"
```

---

### 27. When using `TypeAdapter(list[int])`, what is the result of `ta.validate_python(["1", "2", 3])`?

```python
a) ["1", "2", 3] (no change)
b) [1, 2, 3] (strings converted to ints)
c) A ValidationError because "1" and "2" are strings.
d) ["1", "2", 3] but a warning is logged.
```

---

### 28. In the context of `BaseSettings`, what is the order of priority for loading values?

```python
a) Environment variables > init arguments > default values on the model.
b) Init arguments > environment variables > default values on the model.
c) Default values on the model > environment variables > init arguments.
d) Init arguments > default values on the model > environment variables.
```

---

### 29. Which method is used to serialize a model directly to a JSON string?

```python
a) model.json()
b) model.to_json()
c) model.model_dump_json()
d) json.dumps(model)
```

---

### 30. What is the final output of the following code?

```python
from pydantic import BaseModel, TypeAdapter

class Container(BaseModel):
    items: list[str]

adapter = TypeAdapter(Container)
data = adapter.validate_python({"items": [1, 2, 3]})
print(data)
```

```python
a) Container(items=['1', '2', '3'])
b) Container(items=[1, 2, 3])
c) A ValidationError is raised.
d) {'items': ['1', '2', '3']}
```


In Pydantic's default mode, if a field is defined as id: int in a BaseModel, and input data provides "123" as a string, what happens during model instantiation?
A) It raises a ValidationError immediately, as strings are not integers.
B) It converts "123" to 123 automatically and proceeds without error.
C) It converts only if the string is numeric, otherwise stores as string.
D) It raises an error unless StrictInt is used, which allows conversion.
When using Field() to set constraints like ge=18 and le=100 for an age field, what exact error type would occur if age=101 is provided?
A) ValueError with message about exceeding maximum.
B) ValidationError detailing the field and "greater than or equal" violation.
C) ValidationError specifying the input should be less than or equal to 100.
D) TypeError if the input was a string like "101" in lax mode.
In the example of custom validators with @field_validator("age"), if value=17 is passed, what is the precise exception raised inside the validator?
A) ValidationError with a custom message "User must be 18+".
B) ValueError explicitly raised with "User must be 18+".
C) TypeError if age was not an integer before validation.
D) AssertionError unless the validator returns the value unmodified.
For serialization, calling model_dump() on a User model with id=1 and name="Ali" returns a dict. How does model_dump_json() differ in output format?
A) It returns a JSON string like '{"id":1,"name":"Ali"}'.
B) It returns a dict but with JSON-compatible types only.
C) It serializes datetime fields automatically if present.
D) It excludes None fields by default unless specified.
In strict mode using StrictInt for field x, why does Model(x="123") fail while Model(x=123) succeeds?
A) Strict mode disables all type coercion, requiring exact type match.
B) Lax mode allows coercion, but strict checks for integer subclass only.
C) StrictInt enforces no conversion from strings, even numeric ones.
D) It fails in both modes if the field is not annotated with Union[str, int].
When using aliases like full_name: str = Field(..., alias="fullName"), if data={"fullName": "Ali Khan"}, what attribute access returns "Ali Khan"?
A) u.full_name, as alias maps input but not output.
B) u.fullName, since alias overrides the Python attribute.
C) Both u.full_name and u.fullName, for compatibility.
D) u.model_dump()["fullName"], but direct access uses full_name.
In Settings Management with BaseSettings, if debug: bool = False is defined, and no env var is set, what value does s.debug hold after instantiation?
A) False, as it's the default and env vars are optional.
B) True, if any env var like DEBUG exists implicitly.
C) None, unless explicitly set in env or overridden.
D) Raises error if database_url is missing but debug has default.
Using pydantic.dataclasses on a standard @dataclass with id: int, if id="123" is passed, what occurs?
A) Automatic conversion to 123, adding validation to dataclass.
B) No conversion, as dataclass lacks BaseModel inheritance.
C) ValidationError unless Field() is used for rules.
D) Works like BaseModel but without custom validators support.
Calling User.model_json_schema() on a model with id: int and name: str generates what kind of output?
A) A dict representing JSON Schema with type validations.
B) A string of JSON Schema, ready for API documentation.
C) Includes aliases if defined, but excludes defaults.
D) Schema for serialization, not for input validation.
With TypeAdapter(list[int]), validating ["1", 2, 3] returns [1, 2, 3]. What happens if ["1", "two", 3] is passed?
A) ValidationError for the invalid string "two".
B) Partial conversion [1, "two", 3] in lax mode.
C) Full list as strings, ignoring int annotation.
D) Raises error only if strict mode is enabled on adapter.
In validation errors, for input id="abc" and name=123, the errors() list contains loc as ["id"] and ["name"]. What msg for "name"?
A) "Input should be a valid string" since 123 is int.
B) "Input should be a valid integer" mismatched.
C) "value is not a valid str" with type details.
D) Combined error if both fields fail simultaneously.
Why is Pydantic's core written in Rust mentioned in performance?
A) For speed in APIs and large data handling.
B) To enable strict mode without slowdowns.
C) For better error messages in validation.
D) To support environment variables natively.
In models, if signup_ts: datetime | None = None, and data provides "2024-01-01 10:30", it converts to datetime. What if omitted?
A) Sets to None, as default allows optional.
B) Raises error unless Field(default=None) is used.
C) Converts to current datetime implicitly.
D) Validation passes but attribute is missing.
For Field(min_length=3, max_length=20) on username, if "Ab" is provided, what error details?
A) ValidationError: input too short for min_length.
B) ValueError if custom validator checks length.
C) TypeError if input is not string first.
D) Passes if lax mode coerces non-strings.
Custom validator with @field_validator("age") raises ValueError for <18. If age=18, what does it return?
A) The value unchanged, as per standard.
B) Modified value if additional logic present.
C) None if no return statement executed.
D) Raises if cls parameter is misused.
Serialization with model_dump_json() on a model with datetime field outputs ISO format. What if exclude_none=True?
A) Omits fields with None, but not defaults.
B) Includes all, as it's not mentioned in content.
C) Affects dict but not JSON string directly.
D) Requires alias for None fields.
Strict vs Lax: In lax, "123" to int works. In strict with StrictInt, it fails. How to enable strict globally?
A) Not directly; per-field with Strict types.
B) Via model config for all fields.
C) Only in BaseSettings, not BaseModel.
D) By installing pydantic-settings extra.
Aliases: If alias="fullName" for full_name, data uses "fullName". What if data uses "full_name"?
A) Fails, as alias strictly maps input key.
B) Works if lax mode allows key coercion.
C) Both keys accepted for flexibility.
D) Uses population by alias config.
In BaseSettings, database_url: str reads from env. If missing, what happens?
A) Raises ValidationError for required field.
B) Uses default if provided, else error.
C) Sets to empty string for str types.
D) Optional if =None is added.
Pydantic dataclass with id: int converts "123" to 123. How does it differ from BaseModel?
A) Lacks full serialization methods like dump.
B) Supports validation but no custom validators.
C) Uses post_init for extra checks.
D) Identical behavior but lighter weight.
model_json_schema() output includes "properties" with types. For id: int, it's?
A) {"type": "integer"} in schema dict.
B) {"type": "number"} for flexibility.
C) Includes min/max if Field used.
D) String schema, not dict.
TypeAdapter for list[int] coerces strings to ints. If empty list [], validates to?
A) [], as list can be empty.
B) Error if min_items not set.
C) None, treating as optional.
D) [0] default for int lists.
Why use Pydantic over plain type hints?
A) Enforces validation at runtime.
B) Hints are static, Pydantic dynamic.
C) Automatic conversion in hints too.
D) For Rust speed in type checking.
In recap, BaseModel is for schemas. Field for rules. What subtle link?
A) Field enhances BaseModel validations.
B) BaseModel requires Field for all.
C) Rules optional without Field.
D) Recap omits strict mode tie-in.
If User(id="abc"), error loc=["id"], msg="Input should be a valid integer". If id=1.5?
A) Same msg, as not integer.
B) "Input should be integer, got float".
C) Converts to 1 in lax mode.
D) No error for numeric types.
Custom validator can modify value. If return value + 1, for age=18 returns?
A) 19, if logic to modify.
B) Must return unchanged per guide.
C) Error if not matching type.
D) Optional modification allowed.
Serialization excludes private fields?
A) No, all defined fields included.
B) Yes, if _prefix used.
C) Configurable via model.
D) Only in JSON, not dict.
Strict mode for one field, lax for others possible?
A) Yes, using StrictInt per field.
B) No, model-wide setting.
C) Via aliases and validators.
D) Only in dataclasses.
Settings Management requires pydantic-settings install. For what?
A) BaseSettings class usage.
B) Env var handling in BaseModel.
C) Optional, core has it.
D) For debug bool defaults.
TypeAdapter vs BaseModel for quick validations?
A) Adapter for non-class types like list.
B) BaseModel faster for simple.
C) Adapter lacks schema generation.
D) Both same for serialization.
18.4sExpert
