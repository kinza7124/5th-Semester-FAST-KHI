# The Ultimate Python & OOP & Testing Masterclass
### A Beginner's Guide to the Smart Expense Sharing Project
---

> **Who is this for?**
> This guide is written for someone who has never seen Python before. You don't need to know anything. By the end, you will understand why every single line of code in this project exists, and how it works. We will start from the very beginning and build up to writing professional software tests.

---

## Table of Contents

1. [What is Python?](#what-is-python)
2. [Python Data Types — The Building Blocks](#python-data-types)
3. [Functions in Python](#functions-in-python)
4. [What is OOP? (Object-Oriented Programming)](#what-is-oop)
5. [The 4 Pillars of OOP](#the-4-pillars-of-oop)
6. [Classes and Objects in Python](#classes-and-objects)
7. [The `self` Keyword](#the-self-keyword)
8. [The `__init__` Method (Constructor)](#the-init-method)
9. [Inheritance in Python](#inheritance)
10. [Decorators in Python](#decorators)
11. [Python Dataclasses](#python-dataclasses)
12. [Dataclass vs Pydantic Model](#dataclass-vs-pydantic)
13. [Enums in Python](#enums)
14. [Type Hints and Typing Module](#type-hints)
15. [Error Handling in Python](#error-handling)
16. [Python Imports and Modules](#python-imports)
17. [UUID — Unique Identifiers](#uuid)
18. [What is Software Testing?](#software-testing)
19. [Types of Software Testing](#types-of-testing)
20. [Manual Test Case Design](#manual-testing)
21. [Automated Testing with `unittest`](#automated-testing)
22. [How to Write a Test Case Step by Step](#writing-test-cases)
23. [Assertions — The Heart of Testing](#assertions)
24. [Regression Testing](#regression-testing)
25. [Complete Project Code Walkthrough](#project-walkthrough)

---

## 1. What is Python?

Python is a **programming language** — a way to give instructions to a computer. It was created by Guido van Rossum and first released in 1991. Python is one of the most popular languages in the world because it is:

- **Easy to read**: Python code looks almost like English.
- **Versatile**: Used in web development, data science, AI, automation, and more.
- **Free and open source**: Anyone can use it.

### Your First Python Program

```python
print("Hello, World!")
```

That single line tells the computer to display the text `Hello, World!` on the screen.

### Variables

A variable is a **named container** for storing data.

```python
amount = 3000        # This stores the number 3000
name = "Ali"         # This stores the text "Ali"
is_paid = True       # This stores True (a yes/no value)
```

**In our project**, we use variables everywhere:

```python
# From system.py
user_id = str(uuid.uuid4())[:8]   # A variable storing a unique ID
```

### Indentation — Python's Most Important Rule

Unlike other languages that use `{}` curly braces, Python uses **indentation** (spaces at the start of a line) to define blocks of code.

```python
if amount > 0:
    print("Amount is valid")   # This is INSIDE the if block (4 spaces)
    print("Proceeding...")     # Still inside
print("This is outside")       # This is OUTSIDE (no spaces)
```

If your indentation is wrong, Python will give you an error. This is non-negotiable.

---

## 2. Python Data Types — The Building Blocks

Every piece of data in Python has a **type**. The type tells Python what kind of data it is and what you can do with it.

### 2.1 String (`str`)

A **string** is any text value, enclosed in single or double quotes.

```python
name = "Ali"
email = "ali@example.com"
description = "Dinner at restaurant"
```

**Useful string operations:**

```python
greeting = "Hello"
print(greeting.upper())       # HELLO
print(greeting.lower())       # hello
print(len(greeting))          # 5 (the length)
print(f"Hi, {name}!")         # Hi, Ali! (f-string formatting)
```

**In our project** (`models.py`):

```python
@dataclass
class User:
    user_id: str    # A string like "a1b2c3d4"
    name: str       # A string like "Ali"
    email: str      # A string like "ali@example.com"
```

### 2.2 Integer (`int`) and Float (`float`)

- **`int`**: Whole numbers (no decimal point). Example: `100`, `3000`
- **`float`**: Numbers with decimals. Example: `33.33`, `1500.0`

```python
total = 3000        # int
share = 1000.0      # float
percentage = 33.33  # float
```

**In our project** (`models.py`):

```python
@dataclass
class Split:
    user_id: str
    amount: float = 0.0       # A float — could be 33.33 or 1000.0
    percentage: float = 0.0   # A float — like 25.0 for 25%
```

### 2.3 Boolean (`bool`)

A `bool` can only be `True` or `False`. It's used for decisions.

```python
is_valid = True
has_paid = False
```

**In our project**, booleans appear in conditions:

```python
# From engine.py
if balance < -0.01:   # If the balance is negative (True or False)
    ...
```

### 2.4 List (`list`)

A **list** is an **ordered collection** of items. Items can be added, removed, or changed. Lists are written with square brackets `[]`.

```python
phone_numbers = ["0300-1234567", "0311-9876543"]
expenses = []           # An empty list
expenses.append(5000)   # Adding to the list
print(expenses[0])      # Accessing first item: 5000
```

**Key List operations:**

```python
nums = [3, 1, 2]
nums.append(4)      # [3, 1, 2, 4]
nums.remove(1)      # [3, 2, 4]
len(nums)           # 3
nums[0]             # 3 (first element)
nums[-1]            # 4 (last element)
```

**In our project** (`models.py` and `system.py`):

```python
# A User holds a list of phone numbers
phone_numbers: List[str] = field(default_factory=list)

# The system holds a list of all expenses ever added
self.expenses: List[Expense] = []
```

### 2.5 Set (`set`)

A **set** is a collection with **no duplicates**. Order is not guaranteed. Sets are written with curly braces `{}`.

```python
members = {"ali_id", "sara_id", "ahmed_id"}
members.add("ali_id")    # Won't duplicate! Still 3 items
members.remove("sara_id")
print("ali_id" in members)  # True
```

Think of a set like a guest list — a person can only be on the list once.

**In our project** (`models.py`):

```python
@dataclass
class Group:
    members: Set[str] = field(default_factory=set)
    admins: Set[str] = field(default_factory=set)
```

We use a `Set` for group members because **a user should only be in a group once**. If you try to add them twice, the set silently ignores the duplicate.

### 2.6 Dictionary (`dict`)

A **dictionary** stores **key-value pairs** — like a real dictionary where a word (key) maps to its definition (value). Written with `{}` and `:`.

```python
user_database = {
    "a1b2c3d4": "Ali",
    "e5f6g7h8": "Sara"
}

print(user_database["a1b2c3d4"])    # Ali
user_database["i9j0k1l2"] = "Ahmed" # Adding new entry
```

**In our project** (`system.py`):

```python
# Maps user_id (key) to User object (value)
self.users: Dict[str, User] = {}

# Maps group_id (key) to Group object (value)
self.groups: Dict[str, Group] = {}
```

This allows us to instantly find any user by their ID, just like looking up a word in a dictionary.

### 2.7 Tuple (`tuple`)

A **tuple** is like a list, but it is **immutable** (unchangeable after creation). Written with parentheses `()`.

```python
point = (10, 20)        # x and y coordinates
transaction = ("ali_id", "sara_id", 500.0)  # debtor, creditor, amount
```

**In our project** (`engine.py`):

```python
# The simplify_debts function returns a list of tuples
# Each tuple is (debtor_id, creditor_id, amount)
def simplify_debts(self) -> List[Tuple[str, str, float]]:
    ...
    transactions.append((debtor_id, creditor_id, round(settled_amount, 2)))
    return transactions
```

We use tuples for transactions because once a transaction record is created, it should not be changed.

---

## 3. Functions in Python

A **function** is a reusable block of code that performs a specific task. Functions avoid code repetition.

```python
def say_hello(name):     # def = define, "say_hello" = name, "name" = parameter
    print(f"Hello, {name}!")

say_hello("Ali")         # Call the function → prints "Hello, Ali!"
say_hello("Sara")        # Call again → prints "Hello, Sara!"
```

### Return Values

A function can also **return** a value back to the caller.

```python
def add(a, b):
    return a + b        # Sends the result back

result = add(10, 5)     # result = 15
```

**In our project** (`system.py`):

```python
def create_user(self, name: str, email: str, phones: List[str]) -> User:
    ...
    return user     # Returns the newly created User object
```

The `-> User` part (called Type Hint) is a hint saying "this function will return a User object."

---

## 4. What is OOP? (Object-Oriented Programming)

Imagine you are building a game with cars. Without OOP, you'd store all car data in dozens of separate variables:

```python
car1_color = "Red"
car1_speed = 200
car1_brand = "Toyota"

car2_color = "Blue"
car2_speed = 180
car2_brand = "Honda"
```

This becomes a nightmare as the program grows. OOP solves this by letting you create a **`Car` blueprint (Class)** and then create as many **individual cars (Objects)** as you need from it.

**OOP is the art of modeling real-world things in code.**

In our expense-sharing project, real-world things are:
- **Users** (Ali, Sara, Ahmed)
- **Groups** (Friends, Family)
- **Expenses** (Dinner: 3000, Fuel: 1500)
- **Splits** (How an expense is divided)

Each of these becomes a **Class** in Python.

---

## 5. The 4 Pillars of OOP

These are the fundamental principles that every OOP language follows.

### Pillar 1: Encapsulation (Grouping Data Together)

**Encapsulation** means bundling related data (variables) and the methods (functions) that work on that data into a single unit — a **class**.

Think of a capsule pill. It holds medicine inside and presents only the outer shell to the world. You take the pill; you don't have to know the chemical formulas inside.

**Simple Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance     # Data is INSIDE the class

    def deposit(self, amount):     # Method to change the data
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)   # 1500
```

**In our project** (`models.py`):

```python
@dataclass
class User:
    user_id: str
    name: str
    email: str
    phone_numbers: List[str] = field(default_factory=list)

    def add_phone(self, phone: str):        # The method BELONGS to the User
        if phone not in self.phone_numbers:
            self.phone_numbers.append(phone)
```

The `User` class **encapsulates** the user's identity (name, email) along with the logic for managing their phone numbers. The `add_phone` method is part of the `User` class — not floating loose in the code.

---

### Pillar 2: Abstraction (Hiding Complexity)

**Abstraction** means hiding the complicated internal details and showing only the simple, necessary parts to the user.

A classic example: When you use a TV remote, you press the "Volume Up" button. You don't need to know about the infrared signal, the circuit board, or the processor inside the TV. You just press the button and the volume goes up. The complexity is **abstracted away**.

**In our project** (`main.py` using `system.py`):

```python
# In main.py, we simply say:
system.add_expense("Dinner", 3000, ali.user_id, SplitType.EQUAL, splits_dinner)
```

But *inside* `system.py`, `add_expense` does many complex things:
1. Validates the payer exists.
2. Validates the amount is positive.
3. Calculates shares for each person.
4. Creates an Expense object.
5. Calls the Balance Engine to update debts.

The user of `main.py` doesn't see any of this complexity. That's abstraction.

---

### Pillar 3: Inheritance (Sharing Code Between Classes)

**Inheritance** allows a new class (child) to take on the properties and methods of an existing class (parent). This avoids rewriting the same code.

Think of it like biological inheritance. A child inherits features from their parent (eye color, height tendencies) but can also have their own unique features.

**Simple Example:**

```python
class Animal:              # PARENT class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):         # CHILD class — inherits from Animal
    def speak(self):       # OVERRIDES the parent method
        print(f"{self.name} barks!")

class Cat(Animal):         # Another CHILD class
    def speak(self):
        print(f"{self.name} meows!")

dog = Dog("Rex")
dog.speak()    # Rex barks!
cat = Cat("Whiskers")
cat.speak()    # Whiskers meows!
```

**In our project** (`models.py`):

The `Split` class is a base that both equal, exact, and percentage splits share:

```python
@dataclass
class Split:        # Base class
    user_id: str
    amount: float = 0.0
    percentage: float = 0.0
```

All split types use `user_id` and `amount`. We don't need to rewrite those fields every time.

---

### Pillar 4: Polymorphism (Many Forms)

**Polymorphism** (from Greek: "many shapes") means that different classes can respond to the same method call in their own way.

**In our project** (`system.py`):

```python
if split_type == SplitType.EQUAL:
    share = amount / len(splits)
    for s in splits:
        s.amount = share                          # EQUAL behavior

elif split_type == SplitType.PERCENT:
    for s in splits:
        s.amount = (s.percentage * amount) / 100  # PERCENT behavior

elif split_type == SplitType.EXACT:
    total_exact = sum(s.amount for s in splits)   # EXACT behavior
    if abs(total_exact - amount) > 0.01:
        raise ValueError("Total splits must equal amount")
```

The `splits` list gets an `amount` set on each member, but **how** that amount is calculated changes depending on the type. That is polymorphism — the same operation (`set amount`) behaves differently based on context.

---

## 6. Classes and Objects in Python

A **class** is the blueprint. An **object** is the actual thing built from that blueprint.

```python
# Defining the class (the blueprint)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")

# Creating objects (instances) from the blueprint
ali = Person("Ali", 22)       # Object 1
sara = Person("Sara", 25)     # Object 2

ali.greet()    # Hi, I'm Ali and I am 22 years old.
sara.greet()   # Hi, I'm Sara and I am 25 years old.
```

**In our project**, creating a user object:

```python
# This calls User's __init__ method and creates a User object
user = User(user_id, name, email, phones)
```

---

## 7. The `self` Keyword

`self` is Python's way of saying "this specific object". When you have 10 User objects, `self.name` on one User refers to THAT User's name, not all of them.

```python
class Counter:
    def __init__(self):
        self.count = 0      # Each Counter object has its own count

    def increment(self):
        self.count += 1     # self.count = THIS counter's count

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
print(c1.count)  # 2
print(c2.count)  # 0 — c2 is separate!
```

**In our project** (`engine.py`):

```python
class BalanceEngine:
    def __init__(self):
        self.user_balances = {}   # THIS engine's ledger
```

When `system.py` creates `self.engine = BalanceEngine()`, that engine object has its own private ledger. If you created two systems, they'd each have their own, separate engine.

---

## 8. The `__init__` Method (Constructor)

The `__init__` method is the **constructor** — it runs automatically the moment you create an object. Its job is to set up the object's initial state.

```python
class Expense:
    def __init__(self, description, amount):
        self.description = description   # Setup the description
        self.amount = amount             # Setup the amount

dinner = Expense("Dinner", 3000)         # __init__ runs here
print(dinner.description)    # Dinner
print(dinner.amount)         # 3000
```

Every class must have an `__init__` unless you use `@dataclass` which writes it for you automatically.

---

## 9. Inheritance in Python

Here is a more detailed example of inheritance:

```python
class Vehicle:             # Parent
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        print(f"I am a vehicle made by {self.brand}")

class Car(Vehicle):        # Child (inherits from Vehicle)
    def __init__(self, brand, doors):
        super().__init__(brand)   # Call parent's __init__
        self.doors = doors

    def describe(self):           # Override the parent method
        print(f"I am a car by {self.brand} with {self.doors} doors")

my_car = Car("Toyota", 4)
my_car.describe()   # I am a car by Toyota with 4 doors
```

`super().__init__(brand)` calls the **parent class's** `__init__` so you don't have to rewrite the `self.brand = brand` line.

---

## 10. Decorators in Python

A **decorator** is a special function that **wraps** another function or class to give it extra behavior.

Think of a decorator as a gift wrapper. The gift (your function) is already good on its own. But wrapping it (applying a decorator) makes it better or adds something extra.

### Built-in Decorator: `@staticmethod`

This tells Python: "This method doesn't need `self`. It belongs to the class but doesn't use any object data."

**In our project** (`engine.py`):

```python
class SplitValidator:
    @staticmethod
    def validate_splits(amount: float, split_type: str, splits: List) -> bool:
        if not splits:
            return False
        ...
```

You call it as `SplitValidator.validate_splits(...)` without creating an object.

### The Most Important Decorator: `@dataclass`

This deserves its own full section (next). But understand that `@dataclass` is a decorator that reads your class's type hints and **automatically generates** `__init__`, `__repr__`, and `__eq__` for you.

```python
@dataclass          # ← This decorator does the magic
class Split:
    user_id: str
    amount: float = 0.0
```

Without `@dataclass`, you'd have to write:

```python
class Split:
    def __init__(self, user_id: str, amount: float = 0.0):
        self.user_id = user_id
        self.amount = amount
    def __repr__(self):
        return f"Split(user_id={self.user_id}, amount={self.amount})"
```

The decorator saves you from writing all that boilerplate.

---

## 11. Python Dataclasses

Introduced in Python 3.7, `dataclasses` are a way to create classes that are **primarily data containers** with minimal code.

### Basic Dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
print(p.x)    # 3.0
print(p)      # Point(x=3.0, y=4.0) — __repr__ is auto-generated
```

### The `field()` Function — Critical for Beginners!

This is one of the trickiest aspects of dataclasses. Let's understand WHY you need `field()`.

**The Problem with mutable defaults:**

```python
# WRONG way (dangerous!)
@dataclass
class BadGroup:
    members: list = []   # Python raises a TypeError here!
```

Python disallows this because if you wrote `members = []` as a default, **every** `BadGroup` object would share the SAME list in memory. If you added "Ali" to Group 1's members, "Ali" would magically appear in Group 2's members too!

**The CORRECT way with `field()`:**

```python
from dataclasses import dataclass, field

@dataclass
class Group:
    members: Set[str] = field(default_factory=set)
```

`default_factory=set` tells Python: "Every time a new Group is created, call `set()` to create a FRESH, empty set for it." This ensures each Group gets its own private member set.

**In our project** (`models.py`):

```python
@dataclass
class User:
    user_id: str
    name: str
    email: str
    phone_numbers: List[str] = field(default_factory=list)  # Fresh list each time

@dataclass
class Group:
    group_id: str
    name: str
    members: Set[str] = field(default_factory=set)    # Fresh set each time
    admins: Set[str] = field(default_factory=set)     # Fresh set each time
```

---

## 12. Dataclass vs Pydantic Model

Both are ways to define data models in Python, but they serve different purposes.

| Feature | `@dataclass` | Pydantic `BaseModel` |
| :--- | :--- | :--- |
| **Library** | Built-in (no install) | `pip install pydantic` |
| **Type Validation** | None (types are just hints) | Strict (raises errors for wrong types) |
| **Use Case** | Simple data containers | APIs, user input, strict validation |
| **Performance** | Very fast | Slightly slower (due to validation) |
| **JSON Support** | Manual work needed | Built-in `.model_dump()` / `.json()` |

**Dataclass example:**

```python
@dataclass
class User:
    name: str
    age: int

User("Ali", "twenty-two")  # No error! Python doesn't validate.
```

**Pydantic example:**

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

User(name="Ali", age="twenty-two")   # ValidationError! "twenty-two" is not an int
```

**Why we used `@dataclass`:** Our project is a backend system where we control all inputs ourselves. We don't need Pydantic's strict validation because we validate inputs manually with `raise ValueError` in `system.py`. Dataclasses are simpler and faster for this use case.

---

## 13. Enums in Python

An **Enum** (Enumeration) is a set of named constant values. It prevents you from using raw strings that could be mistyped.

**Without Enum (dangerous):**

```python
# Anyone could accidentally type "equall" or "EQUAL" or "Equal"
split_type = "equall"   # Typo! The program might just silently fail
```

**With Enum (safe):**

```python
from enum import Enum

class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

split_type = SplitType.EQUAL   # Clean, readable, typo-proof
```

**In our project** (`models.py`):

```python
class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"
```

And used in `system.py`:

```python
if split_type == SplitType.EQUAL:
    ...
elif split_type == SplitType.PERCENT:
    ...
```

This makes the code crystal clear and prevents bugs caused by string typos.

---

## 14. Type Hints and the `typing` Module

Python is a **dynamically typed** language — you don't NEED to declare what type a variable is. But **Type Hints** let you add that information as documentation and allow tools to catch bugs early.

```python
name = "Ali"               # No type hint
name: str = "Ali"          # With type hint — makes intent clear
```

For complex types, we use the `typing` module:

```python
from typing import List, Dict, Set, Optional, Tuple

phone_numbers: List[str]         # A list that contains strings
users: Dict[str, User]           # A dictionary: string keys → User values
members: Set[str]                # A set of strings
group_id: Optional[str] = None   # Could be a string OR None
result: List[Tuple[str, str, float]]   # List of 3-item tuples
```

**In our project** (`system.py`):

```python
from typing import Dict, List, Optional

class ExpenseSharingSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}       # Type hinted!
        self.groups: Dict[str, Group] = {}
        self.expenses: List[Expense] = []
```

Type hints make the code **self-documenting**. Just by reading the variable declaration, another developer instantly knows what type of data to expect.

---

## 15. Error Handling in Python

Good software doesn't just crash when something goes wrong. It **handles errors gracefully**.

### Raising Errors

We use `raise` to intentionally stop the program when bad data is detected.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age
```

### Catching Errors

We use `try/except` to catch and handle errors:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

### In Our Project

**Raising errors** (`system.py`):

```python
def create_user(self, name: str, email: str, phones: List[str]) -> User:
    if any(u.email == email for u in self.users.values()):
        raise ValueError(f"User with email {email} already exists.")
    ...

def add_expense(self, ...):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    ...
    if abs(total_pct - 100) > 0.01:
        raise ValueError("Total percentage must be 100")
```

**Testing that errors are raised correctly** (`tests_system.py`):

```python
def test_unique_email_validation(self):
    with self.assertRaises(ValueError):
        self.system.create_user("Dupe", "u1@test.com", ["000"])
```

`assertRaises` checks that a `ValueError` is raised — if it's NOT raised, the test fails. This is how we verify our error handling actually works.

---

## 16. Python Imports and Modules

As a project grows, we split code into multiple files. Each file is called a **module**. We use `import` to bring code from one file into another.

### Types of Imports

```python
import uuid                          # Import an entire standard library module
from enum import Enum                # Import a specific class from a module
from typing import Dict, List        # Import multiple items at once
from models import User, Group       # Import from our own file "models.py"
```

### In Our Project

**`system.py` imports from:**

```python
from models import User, Group, Expense, Split, SplitType   # Our custom models
from engine import BalanceEngine, SplitValidator             # Our engine
from typing import Dict, List, Optional                      # Type hints
import uuid                                                  # Unique IDs
```

**`tests_system.py` imports:**

```python
import unittest                                             # The testing framework
from system import ExpenseSharingSystem, SplitType, Split  # What we want to test
```

This modular structure means each file has one focused job:
- `models.py` → Defines data structures.
- `engine.py` → Does the math.
- `system.py` → Connects everything together.
- `tests_system.py` → Tests all of the above.

---

## 17. UUID — Unique Identifiers

**UUID** stands for **Universally Unique Identifier**. It's a 128-bit number (shown as 32 hex characters) that is statistically guaranteed to be unique across the entire universe.

```python
import uuid

new_id = str(uuid.uuid4())
print(new_id)   # Example: "550e8400-e29b-41d4-a716-446655440000"
```

We use `uuid.uuid4()` which generates a **random** UUID.

**Why use UUID instead of 1, 2, 3...?**

- If you use incrementing numbers (1, 2, 3...), you have to track "what was the last number?". This is hard in distributed systems.
- UUIDs can be generated by ANY machine at any time without coordinating with others.
- UUIDs make IDs unpredictable, which is also a minor security benefit (no one can guess another user's ID).

**In our project** (`system.py`):

```python
user_id = str(uuid.uuid4())[:8]   # Take first 8 characters: "550e8400"
```

We take only the first 8 characters to keep IDs short and readable for our mini-project.

---

## 18. What is Software Testing?

**Software Testing** is the process of evaluating and verifying that a software application:
1. Does what it is supposed to do.
2. Does NOT do what it is not supposed to do.

### Why Test?

- **Catch Bugs Early**: Fixing a bug found in testing costs 10x less than fixing it in production.
- **Confidence**: Allows developers to make changes without fear of breaking things.
- **Documentation**: Tests describe expected behavior, acting as executable documentation.
- **Regression Guard**: Ensures old bugs do not come back when new code is added.

### The Testing Mindset

When testing, think like a detective. Assume the code is broken and try to prove it. Don't just test the "happy path" (things you expect to work). Actively try to break the system.

---

## 19. Types of Software Testing

### Level 1: Unit Testing
Tests a **single, isolated function or method**.
- "Does `create_user` return a User object with the correct email?"
- No database, no network — just pure function logic.

### Level 2: Integration Testing
Tests how **multiple components work together**.
- "When I `add_expense`, does the `BalanceEngine` correctly update?"
- Tests the handoff between our `system.py` and `engine.py`.

### Level 3: System Testing
Tests the **entire application** end-to-end.
- Running `main.py` and verifying the final output.

### Other Testing Types

#### Functional Testing
Verifies the system does what the requirements say.
- "The system must calculate who owes whom after expenses are added."

#### Boundary Value Testing (BVT)
Tests the **edges** of valid input ranges. Bugs often hide at boundaries.

| Boundary | Test Value | Why |
| :--- | :--- | :--- |
| Amount must be positive | `0` | Is zero handled? |
| Amount must be positive | `-1` | Is negative handled? |
| Percentage must total 100 | `99.99` | Just under — does it fail? |
| Percentage must total 100 | `100.01` | Just over — does it fail? |

**In our project** (`tests_system.py`):

```python
def test_invalid_negative_amount(self):
    with self.assertRaises(ValueError):
        self.system.add_expense("Fail", -10, self.u1.user_id, SplitType.EQUAL, [])
```

This tests the boundary of `amount <= 0`.

#### Equivalence Partitioning
Instead of testing every possible input, divide inputs into groups (partitions) where each member of a group is expected to behave the same way.

For expense amount:
- **Valid partition**: Any positive number (1, 100, 9999... just pick one to test)
- **Invalid partition**: Zero or negative (-10, -1, 0... just pick one to test)

#### Regression Testing
After fixing a bug, you write a test to make sure that bug never returns. Every time the project changes, you run ALL tests to make sure nothing regressed (went backwards).

---

## 20. Manual Test Case Design

A **manual test case** is a documented procedure that a human tester follows step-by-step.

### The Format (from our Technical Report)

| Testcase ID | Description | Input | Expected Output | Observed Output | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Create User | Name: Ali, Email: ali@test.com | User created | User created ✓ | PASS |
| TC-08 | Zero Amount | Amount: 0 | Raise ValueError | Error raised ✓ | PASS |

### How to Write a Manual Test Case

1. **TC ID**: Give each test a unique identifier (TC-01, TC-02...).
2. **Description**: What are you testing? Be brief.
3. **Input**: What data will you use?
4. **Expected Output**: What SHOULD happen?
5. **Observed Output**: What DID happen when you ran it?
6. **Status**: PASS or FAIL.

### Types of Manual Tests Used in Our Project

**Functional Tests**: Does the feature work correctly?
```
TC-04: Create group with admin → Group created, admin assigned → PASS
TC-12: Partial settlement → Balance reduced → PASS
```

**Boundary Tests**: Does it handle edge cases?
```
TC-08: Amount = 0 → ValueError raised → PASS
TC-09: Amount = -50 → ValueError raised → PASS
```

**Equivalence Partitioning Tests**: Valid vs Invalid classes?
```
TC-05: Exact splits summing to 100 (valid class) → Balance updated → PASS
TC-06: Exact splits summing to 90 (invalid class) → ValueError raised → PASS
```

---

## 21. Automated Testing with `unittest`

Python's built-in `unittest` module provides a framework for writing and running automated tests.

### Core Concepts

- **Test Suite**: A collection of test cases.
- **Test Case**: A class that inherits from `unittest.TestCase`.
- **Test Method**: A method whose name starts with `test_`.
- **setUp()**: Runs before EVERY test method to set up a clean state.
- **tearDown()**: Runs after every test method to clean up (we didn't need this).

### The Structure

```python
import unittest

class TestMyFeature(unittest.TestCase):   # Must inherit from TestCase
    def setUp(self):
        # This runs BEFORE every test
        # Create fresh objects so tests don't affect each other
        self.my_object = MyClass()

    def test_something(self):             # Name MUST start with "test_"
        result = self.my_object.do_something()
        self.assertEqual(result, "expected_value")

if __name__ == "__main__":
    unittest.main()    # Run all tests when this file is executed
```

### Why `setUp()` is Critical

Without `setUp()`, tests would share state and interfere with each other:

```python
# BAD — tests share one system instance
system = ExpenseSharingSystem()

class Tests(unittest.TestCase):
    def test_a(self):
        system.create_user("Ali", "ali@test.com", [])   # Creates user
    def test_b(self):
        system.create_user("Ali", "ali@test.com", [])   # FAILS: email already exists!
```

With `setUp()`, each test gets its own fresh `ExpenseSharingSystem`:

```python
# GOOD — each test gets a clean slate
class Tests(unittest.TestCase):
    def setUp(self):
        self.system = ExpenseSharingSystem()   # Fresh system for each test!
```

**In our project** (`tests_system.py`):

```python
class TestSmartExpenseSystem(unittest.TestCase):
    def setUp(self):
        self.system = ExpenseSharingSystem()
        self.u1 = self.system.create_user("User1", "u1@test.com", ["111"])
        self.u2 = self.system.create_user("User2", "u2@test.com", ["222"])
        self.u3 = self.system.create_user("User3", "u3@test.com", ["333"])
```

Every single test starts fresh with a new system and three test users.

---

## 22. How to Write a Test Case Step by Step

Every test follows the **AAA Pattern**: Arrange, Act, Assert.

### Step 1: Arrange (Set up the data)
Prepare everything you need for the test.

### Step 2: Act (Do the thing)
Call the function or method you are testing.

### Step 3: Assert (Check the result)
Verify the result is what you expected.

### Example from our project:

```python
def test_equal_split_calculation(self):
    # ARRANGE: Create the split objects
    splits = [Split(self.u1.user_id), Split(self.u2.user_id)]

    # ACT: Add the expense (this runs the calculation)
    self.system.add_expense("Lunch", 100, self.u1.user_id, SplitType.EQUAL, splits)

    # ASSERT: Check the math is correct
    self.assertEqual(self.system.get_user_net_balance(self.u2.user_id), -50.0)
    self.assertEqual(self.system.get_user_net_balance(self.u1.user_id), 50.0)
```

**Explanation:**
- User1 paid 100 for lunch, split equally with User2.
- Each person owes 50.
- User1 paid, so User1 has +50 (is owed money) — Credit.
- User2 didn't pay, so User2 has -50 (owes money) — Debt.

---

## 23. Assertions — The Heart of Testing

An **assertion** is a statement that says "I assert (claim) this is true. If it's not, fail the test."

### Common `unittest` Assertions

```python
self.assertEqual(a, b)           # a == b
self.assertNotEqual(a, b)        # a != b
self.assertTrue(x)               # x is True
self.assertFalse(x)              # x is False
self.assertIn(item, collection)  # item in collection
self.assertRaises(Error, func)   # func() raises Error
self.assertIsNone(x)             # x is None
self.assertIsNotNone(x)          # x is not None
```

### Real Examples from Our Project

**assertEqual** — Checking calculation results:
```python
def test_percentage_split_calculation(self):
    splits = [Split(self.u1.user_id, percentage=75), Split(self.u2.user_id, percentage=25)]
    self.system.add_expense("Gift", 1000, self.u1.user_id, SplitType.PERCENT, splits)
    self.assertEqual(self.system.get_user_net_balance(self.u2.user_id), -250.0)
```
User2 has 25% of 1000 = 250. They didn't pay, so they owe 250. Net = -250.0.

**assertRaises** — Checking error handling:
```python
def test_unique_email_validation(self):
    with self.assertRaises(ValueError):
        self.system.create_user("Dupe", "u1@test.com", ["000"])
```
The email `u1@test.com` was already registered in `setUp()`. Trying to register again MUST raise a `ValueError`.

**assertIn** — Checking membership:
```python
def test_group_management(self):
    group = self.system.create_group("Test Group", self.u1.user_id)
    self.system.add_to_group(group.group_id, self.u2.user_id)
    self.assertIn(self.u1.user_id, group.members)   # u1 must be in members
    self.assertIn(self.u1.user_id, group.admins)    # u1 must be in admins
```

---

## 24. Regression Testing

**Regression** means "going back to a worse state." Regression testing ensures that **fixing one bug doesn't break something that was working before.**

### Example Scenario:

1.  You add a new feature for percentage splits.
2.  This accidentally changes how equal splits are calculated.
3.  Your regression tests for equal splits immediately catch the problem.

In our project, every time you run `python tests_system.py`, you are running regression tests. All 10 tests check the entire system. If any of them fail after a code change, you know you've introduced a regression.

```
.FF.F..FF.     ← Some tests were failing (F) after a bug
..........     ← All pass (.) after the fix!
```

The dot (`.`) means a test passed. The `F` means a test failed.

---

## 25. Complete Project Code Walkthrough

Now let's tie everything together by walking through every file in our project.

### File 1: `models.py` (The Data Layer)

This file answers the question: **"What things exist in our system?"**

```python
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
from enum import Enum
```

**Line-by-line explanation:**
- `from dataclasses import dataclass, field`: Import the `@dataclass` decorator and the `field()` helper function.
- `from typing import ...`: Import type hint utilities.
- `from enum import Enum`: Import the Enum base class.

```python
class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"
```
Defines the three valid ways to split an expense. Prevents string typos.

```python
@dataclass
class User:
    user_id: str
    name: str
    email: str
    phone_numbers: List[str] = field(default_factory=list)

    def add_phone(self, phone: str):
        if phone not in self.phone_numbers:
            self.phone_numbers.append(phone)
```
- `@dataclass` automatically generates `__init__` for us.
- `user_id`, `name`, `email` are required fields (no default).
- `phone_numbers` uses `field(default_factory=list)` to give each User a fresh list.
- `add_phone` uses **Encapsulation** — the User manages its own phones.

```python
@dataclass
class Group:
    group_id: str
    name: str
    members: Set[str] = field(default_factory=set)
    admins: Set[str] = field(default_factory=set)

    def add_member(self, user_id: str):
        self.members.add(user_id)

    def remove_member(self, user_id: str):
        if user_id in self.members:
            self.members.remove(user_id)
            if user_id in self.admins:
                self.admins.remove(user_id)

    def add_admin(self, user_id: str):
        if user_id in self.members:
            self.admins.add(user_id)
```
- `members` is a `Set` — no duplicate members.
- `remove_member` also removes the user from admins if they were one.

```python
@dataclass
class Split:
    user_id: str
    amount: float = 0.0
    percentage: float = 0.0
```
A Split represents one person's share of an expense. The `amount` starts at 0 and gets calculated later by `system.py`.

```python
@dataclass
class Expense:
    expense_id: str
    description: str
    amount: float
    paid_by: str
    split_type: SplitType
    splits: List[Split]
    group_id: Optional[str] = None
```
- `paid_by` stores the user_id of whoever paid.
- `group_id` is `Optional[str] = None` — an expense doesn't have to belong to a group.

---

### File 2: `engine.py` (The Math Layer)

This file answers: **"How do we calculate who owes whom?"**

```python
class BalanceEngine:
    def __init__(self):
        self.user_balances: Dict[str, Dict[str, float]] = {}
```
A nested dictionary. `user_balances["ali_id"]["ahmed_id"] = -500` means Ali owes Ahmed 500.

```python
    def update_balance(self, debtor: str, creditor: str, amount: float):
        if debtor == creditor:
            return
        self.user_balances[debtor][creditor] = self.user_balances[debtor].get(creditor, 0.0) - amount
        self.user_balances[creditor][debtor] = self.user_balances[creditor].get(debtor, 0.0) + amount
```
When User A owes User B `amount`:
- A's balance relative to B decreases by `amount` (goes negative → owes).
- B's balance relative to A increases by `amount` (goes positive → is owed).

```python
    def simplify_debts(self) -> List[Tuple[str, str, float]]:
```
**The Debt Simplification Algorithm** — The most complex part of the project:
1. Calculate each person's net balance (positive = owed money, negative = owes money).
2. Put debtors in a min-heap (most debt first).
3. Put creditors in a max-heap (most credit first).
4. Match the biggest debtor with the biggest creditor and settle as much as possible.
5. Repeat until everyone is settled.

This dramatically reduces the number of transactions needed. Instead of 6 people all paying each other (15 transactions!), it might only need 5 transactions.

---

### File 3: `system.py` (The Controller Layer)

This file answers: **"How do all the pieces work together?"**

```python
class ExpenseSharingSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, Group] = {}
        self.expenses: List[Expense] = []
        self.engine = BalanceEngine()
```
The system holds three dictionaries/lists (the data) and one engine (the algorithms). This is **Abstraction** — the `main.py` file doesn't need to know about any of these internals.

```python
    def create_user(self, name: str, email: str, phones: List[str]) -> User:
        if any(u.email == email for u in self.users.values()):
            raise ValueError(f"User with email {email} already exists.")
        user_id = str(uuid.uuid4())[:8]
        user = User(user_id, name, email, phones)
        self.users[user_id] = user
        return user
```
- Checks if email already exists (unique email validation).
- Generates a UUID for the user.
- Creates a `User` object and stores it in the `self.users` dictionary.

---

### File 4: `tests_system.py` (The Safety Net)

This file answers: **"Does everything actually work?"**

```python
import unittest
from system import ExpenseSharingSystem, SplitType, Split
```
Import the `unittest` framework and the things we want to test.

```python
class TestSmartExpenseSystem(unittest.TestCase):
    def setUp(self):
        self.system = ExpenseSharingSystem()
        self.u1 = self.system.create_user("User1", "u1@test.com", ["111"])
        self.u2 = self.system.create_user("User2", "u2@test.com", ["222"])
        self.u3 = self.system.create_user("User3", "u3@test.com", ["333"])
```
The class inherits from `unittest.TestCase`. `setUp` creates fresh users for every test.

10 test methods cover:
1. Unique email enforcement
2. Group creation and member management
3. Equal split math accuracy
4. Exact split math accuracy
5. Exact split invalid sum rejection
6. Percentage split math accuracy
7. Debt simplification algorithm (linear chain)
8. Circular debt resolution
9. Settlement recording
10. Boundary test: negative amount

---


## Conclusion

You have now learned:
- Python syntax, variables, and all core data types.
- The 4 Pillars of OOP with real-world analogies and project code.
- How to implement classes, `__init__`, `self`, and inheritance.
- What decorators are and how `@dataclass` works.
- The difference between Dataclasses and Pydantic.
- How to use Enums, type hints, UUID, and proper imports.
- Error handling with `raise ValueError`.
- All types of software testing (Unit, Integration, Functional, Boundary, Regression).
- How to write manual test cases in standard table format.
- How to write `unittest` automated tests from scratch using the AAA pattern.

Every concept above is directly visible in the project files. Open any file alongside this guide and you should be able to trace every idea to a real line of code.

---

## Appendix A: Pydantic `BaseModel` — Deep Dive

Pydantic is a **data validation library** for Python. It is the standard for defining data models in modern APIs (especially FastAPI). It goes far beyond what dataclasses offer.

### Installation

```bash
pip install pydantic
```

### Defining a Pydantic Model

You inherit from `BaseModel` (just like `unittest.TestCase`):

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
```

### Automatic Validation

When you create a Pydantic model, it **immediately validates** every field:

```python
# Valid creation
ali = User(name="Ali", email="ali@email.com", age=22)
print(ali.name)    # Ali

# Invalid creation — Pydantic raises ValidationError
User(name="Sara", email="sara@email.com", age="twenty")
# pydantic_core.ValidationError: age: Input should be a valid integer
```

### Field Validators and Constraints

Pydantic lets you add **constraints** to fields using `Field()`:

```python
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr                             # Validates email format automatically!
    age: int = Field(ge=0, le=150)             # ge = >=0, le = <=150
    balance: float = Field(default=0.0, ge=0)  # Balance must be non-negative
```

### Custom Validators

You can write custom validation logic using `@field_validator`:

```python
from pydantic import BaseModel, field_validator

class Expense(BaseModel):
    description: str
    amount: float

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

# This raises immediately:
Expense(description="Lunch", amount=-10)
# ValueError: Amount must be positive
```

Notice how this is similar to what we did **manually** in `system.py`:

```python
# Our manual validation in system.py
if amount <= 0:
    raise ValueError("Amount must be positive")
```

With Pydantic, you put the validation inside the **model itself**, so it's impossible to create an invalid Expense object anywhere in your codebase.

### Serialization (Converting to JSON / Dict)

Pydantic makes it trivial to convert objects to JSON for APIs:

```python
user = User(name="Ali", email="ali@email.com", age=22)

# Convert to dictionary
user.model_dump()
# {'name': 'Ali', 'email': 'ali@email.com', 'age': 22}

# Convert to JSON string
user.model_dump_json()
# '{"name":"Ali","email":"ali@email.com","age":22}'
```

With `@dataclass`, you'd have to write this conversion manually.

### Nested Models

Pydantic handles nested objects elegantly:

```python
from pydantic import BaseModel
from typing import List

class Split(BaseModel):
    user_id: str
    amount: float = 0.0

class Expense(BaseModel):
    description: str
    amount: float
    splits: List[Split]    # A list of Split models

# Creating nested models
expense = Expense(
    description="Dinner",
    amount=3000,
    splits=[
        Split(user_id="ali_id", amount=1000),
        Split(user_id="sara_id", amount=1000),
        Split(user_id="ahmed_id", amount=1000),
    ]
)

print(expense.model_dump())
# {'description': 'Dinner', 'amount': 3000.0,
#  'splits': [{'user_id': 'ali_id', 'amount': 1000.0}, ...]}
```

### Pydantic vs Dataclass — Head-to-Head Summary

| Scenario | Use `Dataclass` | Use `Pydantic` |
| :--- | :--- | :--- |
| Internal data containers | ✅ Yes | Can, but overkill |
| API request/response body | ❌ No | ✅ Yes |
| User input from a form | ❌ No | ✅ Yes |
| Config files | ✅ Yes | ✅ Yes |
| Performance-critical objects | ✅ Yes | Slightly slower |
| Need JSON serialization | Manual | ✅ Built-in |
| Need email/URL validation | Manual | ✅ Built-in |

**In production Splitwise-like apps**, you'd use Pydantic to define the request bodies for your REST API (what the mobile app sends to the server) and use simpler dataclasses or SQLAlchemy models for the internal database layer.

---

## Appendix B: Flask vs FastAPI — Web Framework Comparison

Once you have a backend system (like our `ExpenseSharingSystem`), the next step is to expose it to the world via a **REST API** — a way for mobile apps, websites, or other services to communicate with your system over the internet.

The two most popular Python web frameworks for this are **Flask** and **FastAPI**.

### What is a REST API?

A REST API is a set of **endpoints** (URLs) that clients can call to get data or trigger actions:

```
GET  /users/ali_id         → Returns Ali's profile
POST /users                → Creates a new user
POST /expenses             → Adds a new expense
GET  /balances             → Returns who owes whom
```

---

### Flask (The Classic)

Flask was created in 2010. It is a **micro-framework** — it gives you the *minimum* needed and lets you add everything else yourself.

#### Installation

```bash
pip install flask
```

#### Hello World in Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")           # Decorator defining the URL route
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)   # Start the server
```

#### Adding Our Project to Flask

```python
from flask import Flask, request, jsonify
from system import ExpenseSharingSystem, SplitType, Split

app = Flask(__name__)
system = ExpenseSharingSystem()

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json          # Read JSON from the request body
    try:
        user = system.create_user(
            name=data["name"],
            email=data["email"],
            phones=data.get("phones", [])
        )
        return jsonify({"user_id": user.user_id, "name": user.name}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400   # 400 = Bad Request

@app.route("/balances", methods=["GET"])
def get_balances():
    balances = system.get_balances()
    result = [
        {"debtor": d, "creditor": c, "amount": a}
        for d, c, a in balances
    ]
    return jsonify(result), 200
```

**Flask Characteristics:**
- Very flexible — you decide everything.
- No automatic validation of request bodies.
- No built-in API documentation.
- You must manually parse `request.json` and validate it.
- Synchronous by default (handles one request at a time in a basic setup).

---

### FastAPI (The Modern Standard)

FastAPI was created in 2018. It is built on top of **Starlette** and uses **Pydantic** for automatic request validation. It is now the most popular choice for new Python APIs.

#### Installation

```bash
pip install fastapi uvicorn
```

#### Hello World in FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")             # Route decorator, also defines the HTTP method
def hello():
    return {"message": "Hello, World!"}
```

Run the server with:
```bash
uvicorn main:app --reload
```

#### Adding Our Project to FastAPI (with Pydantic validation)

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from system import ExpenseSharingSystem, SplitType, Split

app = FastAPI(title="Smart Expense Sharing API")
system = ExpenseSharingSystem()


# --- Pydantic Request/Response Models ---

class CreateUserRequest(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr                      # Validates email format automatically!
    phones: List[str] = []

class UserResponse(BaseModel):
    user_id: str
    name: str
    email: str

class BalanceResponse(BaseModel):
    debtor: str
    creditor: str
    amount: float


# --- API Endpoints ---

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(body: CreateUserRequest):    # FastAPI auto-parses & validates body!
    try:
        user = system.create_user(body.name, body.email, body.phones)
        return UserResponse(user_id=user.user_id, name=user.name, email=user.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/balances", response_model=List[BalanceResponse])
def get_balances():
    raw = system.get_balances()
    return [BalanceResponse(debtor=d, creditor=c, amount=a) for d, c, a in raw]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str):               # Path parameter — FastAPI extracts it automatically
    user = system.users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(user_id=user.user_id, name=user.name, email=user.email)
```

#### The Interactive API Docs (Swagger UI)

This is FastAPI's killer feature. Once your server is running, navigate to:

```
http://127.0.0.1:8000/docs
```

You get a **full interactive documentation page** — all your endpoints listed with their request/response schemas. You can test them directly from the browser. FastAPI generates this automatically from your Pydantic models and type hints. Flask has no equivalent built-in.

---

### Flask vs FastAPI — Complete Comparison

| Feature | Flask | FastAPI |
| :--- | :--- | :--- |
| **Release Year** | 2010 | 2018 |
| **Type** | Micro-framework | Full framework |
| **Performance** | Good (WSGI) | Excellent (ASGI, async) |
| **Request Validation** | Manual (`request.json`) | Automatic (Pydantic) |
| **Auto API Docs** | ❌ None | ✅ Swagger + ReDoc |
| **Async Support** | Limited | ✅ First-class (`async def`) |
| **Learning Curve** | Easy | Easy (Pydantic knowledge needed) |
| **Community & Plugins** | Very large, mature | Growing rapidly |
| **Use Case** | Smaller apps, quick prototypes | Production-grade modern APIs |
| **Type Hint Usage** | Optional | Core to the framework |

### When to Use Which?

**Use Flask when:**
- You're building a quick prototype.
- You need maximum flexibility.
- You're maintaining an existing Flask project.
- You need a large number of existing Flask extensions.

**Use FastAPI when:**
- You're building a new production API.
- Your team uses type hints and Pydantic.
- You need the automatic interactive documentation.
- You want the best performance out of the box.
- Your API is consumed by a mobile app or SPA (Single Page App).

### Async in FastAPI (Bonus)

FastAPI natively supports `async`/`await` — which allows handling thousands of concurrent requests without blocking:

```python
import asyncio

@app.get("/balances")
async def get_balances():        # async def instead of def
    await asyncio.sleep(0.1)     # Simulating a database query without blocking
    return system.get_balances()
```

Flask does NOT support this natively (though Flask 2.x added limited async support).

---

## Appendix C: Glossary of Terms

A quick-reference dictionary of every key term used in this guide and the project.

| Term | One-Line Definition |
| :--- | :--- |
| **Algorithm** | A step-by-step procedure for solving a problem. |
| **Abstraction** | Hiding internal complexity behind a simple interface. |
| **API** | Application Programming Interface — a way for software to talk to other software. |
| **Assertion** | A statement in a test that checks if a condition is true. If false, the test fails. |
| **Automated Test** | A test written as code that runs without human intervention. |
| **BaseModel** | The Pydantic base class that adds validation to a class. |
| **Boolean** | A data type that is either `True` or `False`. |
| **Boundary Testing** | Testing the minimum and maximum edges of valid input. |
| **Class** | A blueprint used to create objects. |
| **Constructor** | The `__init__` method; runs when an object is created. |
| **Dataclass** | A Python decorator that auto-generates `__init__` and other methods. |
| **Decorator** | A function that wraps another function or class to modify its behavior. |
| **Dictionary** | A Python data type that stores key-value pairs. |
| **Encapsulation** | Grouping data and methods that operate on that data into one unit (class). |
| **Enum** | A set of named constant values used instead of raw strings. |
| **Equivalence Partitioning** | Grouping inputs into valid/invalid classes and testing one from each. |
| **FastAPI** | A modern, high-performance Python web framework with auto validation and docs. |
| **field()** | A helper for dataclasses to safely define mutable defaults (like lists). |
| **Flask** | A classic, lightweight Python web framework (micro-framework). |
| **Float** | A number with a decimal point (e.g., 33.33). |
| **Function** | A reusable block of code that performs a specific task. |
| **Greedy Algorithm** | An algorithm that makes locally optimal choices at each step. |
| **HTTP** | HyperText Transfer Protocol — the language of the web. |
| **Indentation** | Spaces at the start of a line that define code blocks in Python. |
| **Inheritance** | A child class reusing properties and methods from a parent class. |
| **Import** | Bringing code from another file or library into the current file. |
| **Instance** | A specific object created from a class blueprint. |
| **Integration Test** | Testing how multiple components interact together. |
| **Integer** | A whole number (e.g., 3000). |
| **JSON** | JavaScript Object Notation — a lightweight format for sending data over the internet. |
| **List** | An ordered, mutable collection of items in Python. |
| **Manual Testing** | A human running a test by hand and checking the result. |
| **Method** | A function defined inside a class. |
| **Module** | A Python file (`.py`) that can be imported into other files. |
| **Object** | A specific instance created from a class. |
| **OOP** | Object-Oriented Programming — organizing code around objects and classes. |
| **Optional** | A type hint meaning a value can be of a type OR `None`. |
| **Pydantic** | A Python library for data validation using type hints and `BaseModel`. |
| **Polymorphism** | The ability for different objects to respond to the same operation differently. |
| **raise** | A Python keyword to intentionally trigger an error. |
| **Regression Testing** | Re-running tests after changes to ensure old bugs don't return. |
| **REST API** | A design pattern for building APIs using HTTP methods (GET, POST, etc.). |
| **return** | A keyword that sends a value from a function back to the caller. |
| **self** | A reference to the current object instance inside a class method. |
| **Set** | An unordered collection with no duplicate values. |
| **setUp()** | A `unittest` method that runs before every test to prepare a clean state. |
| **SplitType** | An Enum in our project defining how an expense is divided. |
| **String** | A text value enclosed in quotes. |
| **super()** | A way to call the parent class's method from within a child class. |
| **Tuple** | An immutable (unchangeable), ordered collection of items. |
| **Type Hint** | A notation (like `: str`) that declares what type a variable should be. |
| **unittest** | Python's built-in module for writing automated tests. |
| **Unit Test** | A test for a single, isolated function or method. |
| **UUID** | Universally Unique Identifier — a 128-bit random ID guaranteed to be unique. |
| **Validation** | Checking that data meets specific rules before processing it. |
| **ValueError** | A Python error raised when a function receives an argument of the right type but wrong value. |
| **Variable** | A named container for storing data. |
