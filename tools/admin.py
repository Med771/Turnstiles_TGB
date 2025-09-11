from config import TelegramConfig


class AdminTools:
    @staticmethod
    def is_admin(chat_id: int | str) -> bool:
        is_admin_id = str(chat_id) in TelegramConfig.ADMIN_CHAT_IDS
        is_owner_id = str(chat_id) == TelegramConfig.OWNER_CHAT_ID

        return is_admin_id or is_owner_id