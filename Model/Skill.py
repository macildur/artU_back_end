from artU_back_end.Model.TeachingComponent import TeachingComponent
from enum import Enum


class Skill(TeachingComponent):
    lessons = [7]

    class SkillId(Enum):
        FIRST_SKILL = 1
        SECOND_SKILL = 2

    def __init__(self, title):
        super().__init__()
        self.id = Skill.SkillId.FIRST_SKILL.value
        self.title = title

    def __init__(self, title, id):
        super().__init__()
        self.id = id.value
        self.title = title
