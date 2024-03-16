
from abc import ABC, abstractmethod
from typing import List

from model.core.student import Student


class iGetView(ABC):

    @abstractmethod
    def printAllStudent(self, students: List['Student']) -> None:
        pass

    @abstractmethod
    def prompt(self, msg: str) -> str:
        pass