"""Singly linked list implementation from scratch."""

from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self) -> list[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    print(ll.to_list())  # [1, 2, 3]
