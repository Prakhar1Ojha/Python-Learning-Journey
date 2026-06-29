# 🐍 Python Cheat Sheet

## Variables & Types
```python
x = 5                  # int
y = 3.14                # float
name = "Prakhar"        # str
is_active = True        # bool
items = [1, 2, 3]        # list
point = (1, 2)           # tuple
unique = {1, 2, 3}        # set
person = {"name": "P", "age": 21}  # dict
```

## Strings
```python
s = "Hello World"
s.lower(); s.upper(); s.strip()
s.split(" ")            # -> ['Hello', 'World']
f"{name} is {x} years"  # f-string
```

## Lists
```python
lst = [1, 2, 3]
lst.append(4)
lst.pop()
lst[::-1]                # reverse
[x**2 for x in lst]      # list comprehension
```

## Dictionaries
```python
d = {"a": 1}
d.get("a", 0)
d.items(); d.keys(); d.values()
{k: v for k, v in d.items()}
```

## Functions
```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting string."""
    return f"{greeting}, {name}!"
```

## Control Flow
```python
if x > 0:
    pass
elif x == 0:
    pass
else:
    pass

for i in range(5):
    pass

while x > 0:
    x -= 1
```

## Classes
```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks."
```

## Exceptions
```python
try:
    risky()
except ValueError as e:
    print(f"Error: {e}")
finally:
    cleanup()
```

## File Handling
```python
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("Hello")
```

## Lambda / Map / Filter / Reduce
```python
from functools import reduce
square = lambda x: x ** 2
list(map(square, [1, 2, 3]))
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
reduce(lambda a, b: a + b, [1, 2, 3, 4])
```

## Decorators
```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow():
    ...
```

## Generators
```python
def counter(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

## Virtual Environments
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
deactivate
```

## Git Quick Reference
```bash
git init
git clone <url>
git add .
git commit -m "message"
git push origin main
git pull
git branch -M main
git checkout -b feature/x
```
