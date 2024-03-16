from model.core.person import Person


class Student(Person):
    generalId = 0

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.id = Student.generalId
        Student.generalId += 1

    def getId(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"Students [age={super().getAge()}, name={super().getName()}, id={self.id}]"