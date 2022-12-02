from SkillsService import SkillsService
import simplejson as json

def signup(event, context):
    skillsService = SkillsService()
    try:
        tag = json.loads(event.get("body")).get("tag")
        success = skillsService.getImage(tag)
        response = {
            'statusCode': 200,
            'body': json.dumps(success, use_decimal=True)
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
