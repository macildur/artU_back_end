from Model.DOA.Factory import Factory

class SkillService:
    factory = Factory.AbstactFactory()

    def getMatchingImages(self, requestedAttrs):
        return self.factory.initSkillDAO().get_matching_images(requestedAttrs)
