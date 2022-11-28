
class Skill:

    def __init__(self, title):
        super().__init__()
        self.title = title

    @staticmethod
    def validateImageTags(primaryCategory, subCategory):
        # TODO: get tags from database
        tags = []
        if primaryCategory not in tags or subCategory not in tags:
            raise Exception("Tag in not found")
