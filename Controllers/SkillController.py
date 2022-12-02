import random
from SkillService import SkillService
from Model import Skill
import simplejson as json


def getImages(event, context):
    skillService = SkillService()
    try:
        primaryCategory = json.loads(event.get("body")).get("primary_category")
        secondary_category = json.loads(event.get("body")).get("secondary_category")
        tertiary_category = json.loads(event.get("body")).get("tertiary_category")

        # images = None
        Skill.validateImageTags(primaryCategory, secondary_category, skillService.getImageTags())

        if primaryCategory and secondary_category and tertiary_category:
            # primaryCategory, secondary_category, tertiary_category
            images = skillService.getMatchingImages(primaryCategory, secondary_category, tertiary_category)
            random.shuffle(images)

        elif primaryCategory and secondary_category:
            # primaryCategory, secondary_category
            images = skillService.getMatchingImages(primaryCategory, secondary_category, None)
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
