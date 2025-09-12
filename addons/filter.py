from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from config import TelegramConfig

from addons.decorator.telegram import TelegramDecorator

class MainFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="MainFilter.is_owner")
    def is_owner(msg: Message = None, call: CallbackQuery = None) -> bool:
        msg_flag = msg and str(msg.chat.id) == TelegramConfig.OWNER_CHAT_ID
        call_flag = call and str(call.message.chat.id) == TelegramConfig.OWNER_CHAT_ID

        return msg_flag or call_flag

    @staticmethod
    @TelegramDecorator.log_call(prefix="MainFilter.is_admin")
    def is_admin(msg: Message = None, call: CallbackQuery = None) -> bool:
        msg_flag = msg and str(msg.chat.id) in TelegramConfig.ADMIN_CHAT_IDS
        call_flag = call and str(call.message.chat.id) in TelegramConfig.ADMIN_CHAT_IDS

        return msg_flag or call_flag or MainFilter.is_owner(msg=msg, call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="MainFilter.get_state")
    async def get_state(state: FSMContext):
        try:
            return await state.get_state()

        except Exception:
            return ""
