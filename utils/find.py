from datetime import datetime


class FindUtils:
    @staticmethod
    async def find_user(name: str):
        try:
            return ("0", "photo", "fio", "admin", datetime.now(), True)
        except Exception:
            return None
