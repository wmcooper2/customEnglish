"""Student class."""

# std lib
from typing import Text

# print("students.py:", __path__)

class Student():
    """Student class."""

    def __init__(self, first_name="john", last_name="doe") -> None:
        self.first_name: Text = first_name
        self.last_name: Text = last_name

    def __repr__(self) -> Text:
        return f"Student: {self.first_name} {self.last_name}"

    def __str__(self) -> Text:
        return f"{self.first_name} {self.last_name}"

if __name__ == "__main__":
    print("Creating Student objects...")
    alice = Student("alice", "zee")
    bob = Student("bob", "yankee")
    carol = Student("carol", "x-ray")
    print(alice)
    print(bob)
    print(carol)
