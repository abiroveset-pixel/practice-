class Person:
    """Represents a person."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! My name is {self.name}")

person = Person("Eset")
person.greet()