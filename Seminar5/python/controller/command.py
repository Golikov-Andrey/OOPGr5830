from enum import Enum


class Command(Enum):
    NONE = 0
    READ = 1
    CREATE = 2
    UPDATE = 3
    LIST = 4
    DELETE = 5
    EXIT = 6