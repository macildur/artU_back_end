from enum import Enum

class Module(object):
    lessons = [7]

    class ModuleId(Enum):
        FIRST_MODULE = 1
        SECOND_MODULE = 2

    def __init__(self, title):
        super().__init__()
        self.id = Module.ModuleId.FIRST_MODULE.value
        self.title = title

    def __init__(self, title, id):
        super().__init__()
        self.id = id.value
        self.title = title
