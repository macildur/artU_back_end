from random import random
from Model.Service.SkillService import SkillService
from Model import Skill


class SkillController:

    def __init__(self):
        self.skillService = SkillService()

    def getImages(self, category, subCategory):
        Skill.validateImageTags(category, subCategory, self.skillService.getImageTags())
        images = self.skillService.getMatchingImages(category, subCategory, None)
        random.shuffle(images)

        return images

    def getImages(self, category, subCategory, gender):
        Skill.validateImageTags(category, subCategory, self.skillService.getImageTags())
        images = self.skillService.getMatchingImages(category, subCategory, gender)
        random.shuffle(images)

        return images

    def getMysteryImages(self):
        tags = self.skillService.getImageTags()
        random.shuffle(tags)
        images = self.skillService.getMatchingImages(tags[0], tags[1], None)
        random.shuffle(images)

        return images
