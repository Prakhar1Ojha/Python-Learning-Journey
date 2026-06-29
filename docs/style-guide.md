# Style Guide

This repo follows **PEP8** with a few additions.

## Naming
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants

## Type Hints
Always type-hint function signatures:
```python
def add(a: int, b: int) -> int:
    return a + b
```

## Docstrings
Use triple-quoted docstrings for every public function/class:
```python
def divide(a: float, b: float) -> float:
    """Divide a by b and return the result.

    Raises:
        ZeroDivisionError: if b is 0.
    """
    return a / b
```

## Comments
Comment the **why**, not the **what**. Code should be readable enough that line-by-line comments aren't needed.

## File Organization
- One concept per file inside `examples/`
- Mini-projects get their own folder with `README.md`, `main.py`, and (if needed) `requirements.txt`

## Formatting
Use `black` for auto-formatting and `flake8`/`ruff` for linting before committing.
