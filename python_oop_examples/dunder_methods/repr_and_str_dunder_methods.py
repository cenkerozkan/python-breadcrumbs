class Person:
    """
    A short example written to demonstrate how the __hash__ dunder method works in Python.
    """

    def __init__(
        self,
        name: str,
        surname: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age
        self.surname = surname

    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            raise TypeError(
                f"Cannot compare different classes than {self.__class__.__name__}"
            )
        return self.name == other.name and self.age == other.age

    def __hash__(self) -> int:
        return hash((self.name, self.surname, self.age))

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, {self.age}"

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.surname}, {self.age})"


p1 = Person("John", "Doe", 18)
print(p1)
print(repr(p1))
