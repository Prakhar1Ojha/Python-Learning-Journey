"""Generators: lazy evaluation with yield."""

from typing import Iterator


def fibonacci(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers up to `limit` count, lazily."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    for num in fibonacci(10):
        print(num)
