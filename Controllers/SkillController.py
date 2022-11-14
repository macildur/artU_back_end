from random import random
from Model.Service.SkillService import SkillService

class SkillController:

    def __init__(self):
        self.skillService = SkillService()

    def getImages(self, category, subCategories):
        images = self.skillService.getMatchingImages(category, subCategories)
        random.shuffle(images)

        return images
