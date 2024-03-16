from typing import List
from controller.interfaces.i_get_view import iGetView

from model.core.student import Student

class ViewClass(iGetView):
    def printAllStudent(self, students: List[Student]) -> None:
        print("----------- Список студентов -----------")
        for s in students:
            print(s)
        print("----------------------------------------")


    def prompt(self, msg: str) -> str:
        print(msg)
        return input()