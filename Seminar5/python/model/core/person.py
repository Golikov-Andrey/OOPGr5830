class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getAge(self) -> int:
        return self.age

    def setAge(self, age: int) -> None:
        self.age = age

    def __str__(self) -> str:
        return f"Person [name={self.name}, age={self.age}]"