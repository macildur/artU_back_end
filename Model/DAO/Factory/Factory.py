from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def initUserDAO(self):
        pass

    @abstractmethod
    def initSkillDAO(self):
        pass

    @abstractmethod
    def initModuleDAO(self):
        pass

    @abstractmethod
    def initLessonDAO(self):
        pass
