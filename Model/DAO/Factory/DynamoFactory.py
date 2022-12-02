from Model.DAO.Factory.Factory import AbstractFactory
from Model.DAO.UserDAO import UserDAO
from Model.DAO.SkillDAO import SkillDAO
from Model.DAO.ImageTagDAO import ImageTagDAO


class DynamoFactory(AbstractFactory):

    def initUserDAO(self):
        return UserDAO()

    def initSkillDAO(self):
        return SkillDAO()

    def initImageTagDAO(self):
        return ImageTagDAO()

    def initModuleDAO(self):
        pass

    def initLessonDAO(self):
        pass
