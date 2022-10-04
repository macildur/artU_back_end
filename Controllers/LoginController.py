from artU_back_end.Model.Service.LoginService import LoginService
from artU_back_end.Model.User import User


class LoginController:
    loginService = LoginService()

    def loginController(self):
        pass

    def signup(self):
        newUser = User()
        self.loginService.insertUser(newUser)
        pass

    def login(self):
        pass