from typing import Optional


class AddUtils:
    @staticmethod
    async def add_user(data: dict) -> Optional[tuple]:
        try:
            return ("01",)
        except Exception:
            return None

    @staticmethod
    async def open_close(is_open: bool) -> bool:
        try:
            return True
        except Exception:
            return False
