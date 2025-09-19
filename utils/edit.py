from datetime import datetime
from typing import Optional


class EditUtils:
    @staticmethod
    async def find_by_id(_id: str) -> Optional[tuple]:
        try:
            return ("0", "photo", "fio", "admin", datetime.now(), True)
        except Exception:
            return None

    @staticmethod
    async def delete_by_id(_id: str) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    async def edit_name_by_uid(uid: str, name: str) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    async def edit_photo_by_uid(uid: str, photo) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    async def edit_type_by_uid(uid: str, _type: str) -> bool:
        try:
            return True
        except Exception:
            return False

    @staticmethod
    async def edit_date_by_uid(uid: str, date: str) -> bool:
        try:
            return True
        except Exception:
            return False
