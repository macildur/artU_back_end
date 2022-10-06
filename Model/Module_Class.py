import Expression_Component_Class
import Lesson_Class


class Module(Expression_Component_Class):

    def __init__(self, module_id: int, module_title: str, list_of_lessons: list[Lesson_Class]):
        super().__init__(module_id, module_title)
        self.lessons = list_of_lessons
