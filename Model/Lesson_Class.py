class Lesson:

    def __init__(self, lesson_URL: str):
        self.module_id = None
        self.lesson_URL = lesson_URL

    def set_module_id(self, module_id):
        self.module_id = module_id
