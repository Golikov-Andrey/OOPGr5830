from typing import List
from controller.interfaces.i_get_model import iGetModel

from model.core.student import Student


class ModelClassList(iGetModel):
    def __init__(self, students: List[Student]):
        self.students = students


    def getStudents(self) -> List[Student]:
        return self.students