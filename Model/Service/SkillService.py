from DynamoFactory import DynamoFactory
import random

class SkillsService:
    factory = DynamoFactory()

    def getImage(self, tag):
        response = self.factory.initSkillDAO().get_skill_images(tag)
        i = random.randint(0,5)
        image = ["monalisa.png", "school.png", "stary.jfif", "sunflowers.jfif", "vangogh.jfif", "bedroom.jfif"]
        response = {"imageUrl":"https://skill-images-artu.s3.us-east-2.amazonaws.com/" + image[i]}
        return response