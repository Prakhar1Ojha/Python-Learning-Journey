"""Problem: check if a string is a palindrome, ignoring case and spaces."""

import re


def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    tests = ["Racecar", "A man a plan a canal Panama", "Hello"]
    for t in tests:
        print(f"{t!r} -> {is_palindrome(t)}")
