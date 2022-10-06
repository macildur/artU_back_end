import Expression_Component_Class


class Skill(Expression_Component_Class):

    def __init__(self, skill_id: int, skill_title: str):
        super().__init__(skill_id, skill_title)
