"""Simple CLI calculator supporting + - * /."""

import operator
from typing import Callable

OPS: dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(expression: str) -> float:
    """Parse 'a op b' and return the result."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Expression must be in the form 'a op b', e.g. '5 + 3'")
    a_str, op, b_str = parts
    if op not in OPS:
        raise ValueError(f"Unsupported operator: {op}")
    a, b = float(a_str), float(b_str)
    if op == "/" and b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return OPS[op](a, b)


def main() -> None:
    expr = input("Enter expression (e.g. 5 + 3): ")
    try:
        print(f"Result: {calculate(expr)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
