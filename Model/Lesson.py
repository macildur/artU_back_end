from enum import Enum

class Lesson():

    class LessonId(Enum):
        FIRST_LESSON = 1
        SECOND_LESSON = 2

    def __init__(self, title, lessonUrl, moduleId):
        super().__init__()
        self.id = Lesson.LessonId.FIRST_LESSON.value
        self.title = title
        self.lessonUrl = lessonUrl
        self.moduleId = moduleId.value

    def __init__(self, title, lessonUrl, moduleId, id):
        super().__init__()
        self.id = id.value
        self.title = title
        self.lessonUrl = lessonUrl
        self.moduleId = moduleId.value
