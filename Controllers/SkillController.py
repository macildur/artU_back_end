from random import random
from Model.Service.SkillService import SkillService
from Model import Skill


class SkillController:

    def __init__(self):
        self.skillService = SkillService()

    def getImages(self, category, subCategory):
        Skill.validateImageTags(category, subCategory)
        images = self.skillService.getMatchingImages(category, subCategory, None)
        random.shuffle(images)

        return images

    def getImages(self, category, subCategory, gender):
        Skill.validateImageTags(category, subCategory)
        images = self.skillService.getMatchingImages(category, subCategory, gender)
        random.shuffle(images)

        return images
