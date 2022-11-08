from Model.TeachingComponent import TeachingComponent
from enum import Enum


class Skill(TeachingComponent):

    def __init__(self, title):
        super().__init__()
        self.title = title

