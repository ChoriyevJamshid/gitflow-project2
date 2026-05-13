import json


class TelegramUser:

    def __init__(self,
                 telegram_id: str,
                 first_name: str,
                 last_name: str | None = None,
                 username: str | None = None,
                 language_code: str = "uz"):

        self.__telegram_id = telegram_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code


    @property
    def telegram_id(self) -> str:
        return self.__telegram_id


    @classmethod
    def get(cls, telegram_id: str):

        try:
            with open("database.json", mode="r", encoding="utf-8") as database_file:
                database = json.load(database_file)

        except FileNotFoundError:
            return None

        users_table = database.get("users")
        if not users_table:
            return None

        user = users_table.get(telegram_id)
        if not user:
            return None

        return TelegramUser(**user)






