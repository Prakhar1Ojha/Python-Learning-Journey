"""File handling: reading, writing, and using context managers safely."""

from pathlib import Path

DATA_FILE = Path(__file__).parent / "sample.txt"


def write_lines(lines: list[str]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)


def read_lines() -> list[str]:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f]


if __name__ == "__main__":
    write_lines(["first line", "second line", "third line"])
    print(read_lines())
