from LoginService import LoginService
from User import User
import simplejson as json

def signup(event, context):
    loginService = LoginService()
    try:
        username = json.loads(event.get("body")).get("username")
        password = json.loads(event.get("body")).get("username")
        firstname = json.loads(event.get("body")).get("username")
        lastname = json.loads(event.get("body")).get("username")
        newUser = User(username, password, firstname, lastname)
        success = loginService.insertUser(newUser)
        response = {
            'statusCode': 200,
            'body': json.dumps(success, use_decimal=True)
        }
        return response    
    except:
        response = {
            "errorType": "Auth Error",
            "errorMessage":"Username or Password is incorrect"
        }
        statusCode = 400
        return {
            'statusCode': statusCode,
            'body': json.dumps(response)
        }
        
def login(event, context):
        print(type(event))
        print(event)
        loginService = LoginService()
        try:
            success = loginService.login(json.loads(event.get("body")).get("username"), json.loads(event.get("body")).get("password"))
        except:
            response = {
                "errorType": "Auth Error",
                "errorMessage":"Username or Password is incorrect"
            }
            statusCode = 400
            return {
                'statusCode': statusCode,
                'body': json.dumps(response)
            }
        else:
            response = {
                'statusCode': 200,
                'body': json.dumps(success, use_decimal=True)
            }
            return response