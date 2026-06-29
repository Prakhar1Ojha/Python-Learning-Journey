"""Context manager for timing a block of code."""

import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def timed(label: str = "block") -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label} took {time.perf_counter() - start:.4f}s")


if __name__ == "__main__":
    with timed("sleep"):
        time.sleep(0.1)
