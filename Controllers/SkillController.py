from random import random
from SkillService import SkillService
from Model import Skill
import simplejson as json


def getImages(event, context):
    skillService = SkillService()
    try:
        category = json.loads(event.get("body")).get("category")
        subCategory = json.loads(event.get("body")).get("subCategory")
        gender = json.loads(event.get("body")).get("gender")

        if category and subCategory and gender:
            #category, subCategory, gender
            Skill.validateImageTags(category, subCategory, skillService.getImageTags())
            images = skillService.getMatchingImages(category, subCategory, gender)
            random.shuffle(images)
            response = {
                'statusCode': 200,
                'body': json.dumps(images, use_decimal=True)
            }
            return response

        elif category and subCategory:
            #category, subCategory
            Skill.validateImageTags(category, subCategory, skillService.getImageTags())
            images = skillService.getMatchingImages(category, subCategory, None)
            random.shuffle(images)
            response = {
                'statusCode': 200,
                'body': json.dumps(images, use_decimal=True)
            }
            return response

        else:
            #mystery (nothing else)
            tags = skillService.getImageTags()
            random.shuffle(tags)
            images = skillService.getMatchingImages(tags[0], tags[1], None)
            random.shuffle(images)
            response = {
                'statusCode': 200,
                'body': json.dumps(images, use_decimal=True)
            }
            return response

    except:
            response = {
                "errorType": "Not Found Error",
                "errorMessage":"No Images found with that tag"
            }
            statusCode = 400
            return {
                'statusCode': statusCode,
                'body': json.dumps(response)
            }