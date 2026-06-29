"""A simple timing decorator using functools.wraps."""

import functools
import time
from typing import Any, Callable


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Print how long the wrapped function took to run."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timer
def slow_square(n: int) -> int:
    time.sleep(0.2)
    return n * n


if __name__ == "__main__":
    print(slow_square(5))
