from typing import List
from controller.command import Command
from controller.interfaces.i_get_model import iGetModel
from controller.interfaces.i_get_view import iGetView
from model.core.student import Student


class ControllerClass:
    def __init__(self, model: iGetModel, view: iGetView):
        self.model = model
        self.view = view
        self.students = []


    def testData(self, studs: List['Student']) -> bool:
        return len(studs) > 0

    def update(self) -> None:
        #MVP
        self.students = self.model.getStudents()

        if self.testData(self.students):
            self.view.printAllStudent(self.students)
        else:
            print("Список студентов пуст!")
            
        #MVC
        #self.view.printAllStudent(self.model.getStudents())

    def run(self) -> None:
        com = Command.NONE
        getNewIter = True

        while getNewIter:
            command = self.view.prompt("Введите команду:")
            com = Command[command.upper()]

            if com == Command.EXIT:
                getNewIter = False
                print("Выход из программы")
            elif com == Command.LIST:
                self.view.printAllStudent(self.model.getStudents())