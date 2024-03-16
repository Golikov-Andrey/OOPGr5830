from abc import ABC, abstractmethod
from typing import List

from model.core.student import Student

class iGetModel(ABC):
    @abstractmethod
    def getStudents(self) -> List['Student']:
        pass    