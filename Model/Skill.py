from Model.TeachingComponent import TeachingComponent


class Skill(TeachingComponent):

    def __init__(self, title):
        super().__init__()
        self.title = title

