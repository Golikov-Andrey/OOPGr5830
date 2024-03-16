
from typing import List
from controller.interfaces.i_get_model import iGetModel

from model.core.student import Student


class ModelClassFile(iGetModel):
    def __init__(self, fileName: str):
        self.fileName = fileName
        try:
            with open(fileName, 'w') as fw:
                fw.flush()
        except Exception as e:
          print(e)


    def getStudents(self) -> List[Student]:
        students = []
        try:
            with open(self.fileName, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    params = line.split(" ")
                    pers = Student(params[0], int(params[1]))
                    students.append(pers)
        except Exception as e:
            print(e)

        return students

    def saveAllStudentToFile(self, students: List[Student]) -> None:
        try:
            with open(self.fileName, 'a') as fw:
                for pers in students:
                    fw.write(f"{pers.getName()} {pers.getAge()} {pers.getId()}\n")
                fw.flush()
        except Exception as e:
            print(e)
