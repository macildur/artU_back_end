import random
from SkillService import SkillService
from Model import Skill
import simplejson as json


def getImages(event, context):
    skillService = SkillService()
    try:
        category = json.loads(event.get("body")).get("category")
        subCategory = json.loads(event.get("body")).get("subCategory")
        gender = json.loads(event.get("body")).get("gender")

        # images = None
        Skill.validateImageTags(category, subCategory, skillService.getImageTags())

        if category and subCategory and gender:
            # category, subCategory, gender
            images = skillService.getMatchingImages(category, subCategory, gender)
            random.shuffle(images)

        elif category and subCategory:
            # category, subCategory
            images = skillService.getMatchingImages(category, subCategory, None)
            random.shuffle(images)

        else:
            # mystery (nothing else)
            tags = skillService.getImageTags()
            random.shuffle(tags)
            images = skillService.getMatchingImages(tags[0], tags[1], None)
            random.shuffle(images)

        response = {
            'statusCode': 200,
            'body': json.dumps(images, use_decimal=True)
        }
        return response

    except NameError as tagNotFoundException:
        response = {
            "errorType": "Not Found Error",
            "errorMessage": str(tagNotFoundException)
        }
        statusCode = 400
        return {
            'statusCode': statusCode,
            'body': json.dumps(response)
        }

def getMysteryImage(events, context):
    skillService = SkillService()
    tags = skillService.getImageTags()

    random.shuffle(tags.get('primary_categories'))
    random.shuffle(tags.get('secondary_categories'))
    images = skillService.getMatchingImages(tags.get('primary_categories')[0], tags.get('secondary_categories')[0], None)
    random.shuffle(images)

    response = {
        'statusCode': 200,
        'body': json.dumps(images, use_decimal=True)
    }
    return response
