from aiogram.types import Message

from config import TelegramConfig

from addons.decorator import TelegramDecorator


class AdminTools:
    @staticmethod
    @TelegramDecorator.log_del(prefix="AdminTools.delete_msg")
    async def delete_msg(message: Message):
        await message.delete()

    @staticmethod
    @TelegramDecorator.log_call(prefix="AdminTools.edit_reply")
    async def edit_reply(message: Message):
        await message.edit_reply_markup(reply_markup=None)

    @staticmethod
    def is_admin(chat_id: int | str) -> bool:
        is_admin_id = str(chat_id) in TelegramConfig.ADMIN_CHAT_IDS
        is_owner_id = str(chat_id) == TelegramConfig.OWNER_CHAT_ID

        return is_admin_id or is_owner_id