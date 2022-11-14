from random import random
from Model.Service.SkillService import SkillService

class SkillController:

    def __init__(self):
        self.skillService = SkillService()

    def getImages(self, requestedAttrs):
        images = self.skillService.getMatchingImages(requestedAttrs)
        random.shuffle(images)

        return images
