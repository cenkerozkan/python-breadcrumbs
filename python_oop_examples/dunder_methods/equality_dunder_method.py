class Person:
    """
    A short example written to demonstrate how the __eq__ dunder method works in Python.
    When defining the __eq__ method, it’s generally good practice to verify that the
    object passed to the method is an instance of that class, using the first parameter.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            raise TypeError(
                f"Cannot compare different classes than {self.__class__.__name__}"
            )
        return self.name == other.name and self.age == other.age


p1 = Person("John", 18)
p2 = Person("John", 18)
p3 = Person("Some other guy", 26)

print(p1 == p2)
print(p1 == p3)
