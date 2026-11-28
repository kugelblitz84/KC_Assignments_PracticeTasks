from enum import Enum, auto


class Screen(Enum):
    MAIN = auto()
    ADD_KNOWLEDGE = auto()
    SEARCH = auto()
    VIEW_ALL = auto()
    UPDATE = auto()
    DELETE = auto()
    HISTORY = auto()
    STATISTICS = auto()
    AUTH = auto()
    LOGIN = auto()
    SIGNUP = auto()


class Route:
    def __init__(self):
        self.stack = []

    def push(self, screen):
        self.stack.append(screen)

    def back(self):
        if len(self.stack) > 1:
            self.stack.pop()

    def exit(self):
        self.stack.clear()


route = Route()
