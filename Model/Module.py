from enum import Enum

class Module():

    class ModuleId(Enum):
        FIRST_MODULE = 1
        SECOND_MODULE = 2

    def __init__(self, title, id):
        super().__init__()
        self.id = id.value
        self.title = title
        self.lessons = [7]
