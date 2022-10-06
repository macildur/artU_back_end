class User:

    def __init__(self, user_id: int, username: str, first_name: str, last_name: str, password: str,
                 profile_pic_URL: str, current_module: int, current_streak: int):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.profile_pic_URL = profile_pic_URL
        self.current_module = current_module
        self.current_streak = current_streak

    def login(self) -> bool:
        pass
