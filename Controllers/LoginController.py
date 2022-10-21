from Model.Service.LoginService import LoginService
from Model.User import User


class LoginController:

    def loginController(self):
        self.loginService = LoginService()

    def signup(self, event, context):
        newUser = User(event['username'], event['password'], event['firstname'], event['lastname'])
        try:
            success = self.loginService.insertUser(newUser)
        except:
            response = {
                'statusCode': 400,
                'isBase64Encoded': False,
                'headers': { 'Access-Control-Allow-Origin' : '*',
                'Content-Type': 'application/json' },
                'body': {"ErrorMessage":"Failed to create new user"}
            }
            return response
        else:
            response = {
                'statusCode': 200,
                'isBase64Encoded': False,
                'headers': { 'Access-Control-Allow-Origin' : '*',
                'Content-Type': 'application/json' },
                'body': success
            }
            return response

    def login(event, context):
        loginService = LoginService()
        try:
            success = loginService.login(event.get('username'), event.get('password'))
        except:
            response = {
                'statusCode': 400,
                'isBase64Encoded': False,
                'headers': { 'Access-Control-Allow-Origin' : '*',
                'Content-Type': 'application/json' },
                'body': {"ErrorMessage":"Username or Password is incorrect"}
            }
            return response
        else:
            response = {
                'statusCode': 200,
                'isBase64Encoded': False,
                'headers': { 'Access-Control-Allow-Origin' : '*',
                'Content-Type': 'application/json' },
                'body': success
            }
            return response