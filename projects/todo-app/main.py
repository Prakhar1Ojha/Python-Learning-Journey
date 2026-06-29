"""A persistent CLI todo app backed by a JSON file."""

import json
from pathlib import Path
from typing import TypedDict

TASKS_FILE = Path(__file__).parent / "tasks.json"


class Task(TypedDict):
    text: str
    done: bool


def load_tasks() -> list[Task]:
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: list[Task]) -> None:
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def print_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "x" if t["done"] else " "
        print(f"[{status}] {i}: {t['text']}")


def main() -> None:
    tasks = load_tasks()
    print("Todo App — commands: add <task> | list | done <i> | remove <i> | exit")
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        cmd, _, arg = raw.partition(" ")
        if cmd == "add" and arg:
            tasks.append({"text": arg, "done": False})
            save_tasks(tasks)
        elif cmd == "list":
            print_tasks(tasks)
        elif cmd == "done" and arg.isdigit():
            idx = int(arg)
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
        elif cmd == "remove" and arg.isdigit():
            idx = int(arg)
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif cmd == "exit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
