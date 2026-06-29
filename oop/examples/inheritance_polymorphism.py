"""Object-Oriented Programming basics: inheritance & polymorphism."""

from __future__ import annotations


class Animal:
    """Base class for all animals."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """Return the sound this animal makes. Subclasses override this."""
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


def main() -> None:
    animals: list[Animal] = [Dog("Rex"), Cat("Whiskers")]
    for animal in animals:
        print(animal.speak())  # Polymorphism: same call, different behavior


if __name__ == "__main__":
    main()
