from Model.Service.LoginService import LoginService
from Model.User import User


class LoginController:
    loginService = LoginService()

    def loginController(self):
        pass

    def signup(self, event, context):
        newUser = User(event['username'], event['password'], event['firstname'], event['lastname'])
        success = self.loginService.insertUser(newUser)
        return success #needs to also return the object, and 200/400 instead of bool

    def login(self, event, context):
        success = self.loginService.login(self, username, password)
        return success #needs to also return the object, and 200/400 instead of bool