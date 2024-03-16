# from abc import ABC, abstractmethod
# from enum import Enum
# from typing import List
# import sys

from controller.controller_class import ControllerClass
from model.core.student import Student
from model.model_class import ModelClassList
from model.model_file_class import ModelClassFile
from view.view_class import ViewClass


def main():
    # Студенты
    student1 = Student("Иван", 21)
    student2 = Student("Анна", 20)
    student3 = Student("Сергей", 23)
    student4 = Student("Василий", 21)
    student5 = Student("Марина", 22)
    student6 = Student("Виталий", 25)
    student7 = Student("Добрыня", 44)
    student8 = Student("Владимир", 24)
    student9 = Student("Виктория", 21)
    student10 = Student("Александра", 22)
    student11 = Student("Корнелия", 23)
    student12 = Student("Ева", 21)


    # Формируем списки
    students1 = []
    students1.append(student1)
    students1.append(student2)
    students1.append(student3)
    students1.append(student4)
    students1.append(student5)
    students1.append(student6)
    students1.append(student7)
    students1.append(student8)
    students1.append(student9)
    students1.append(student10)
    students1.append(student11)
    students1.append(student12)

    modelFile = ModelClassFile("StudentDB.csv")
    modelFile.saveAllStudentToFile(students1)

    modelList = ModelClassList(students1)
    viewSimple = ViewClass()

    controller = ControllerClass(modelList, viewSimple)

    controller.run()

if __name__ == '__main__':
    main()












