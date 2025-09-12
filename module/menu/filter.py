from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons import MainFilter

from addons.decorator import TelegramDecorator
from addons.lexicon import KeyboardLexicon
from addons.state import UserState


class MenuFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="MenuFilter.back_btn")
    async def back_btn(message: Message, state: FSMContext) -> bool:
        _state = await MainFilter.get_state(state)

        is_msg_text = message.text == KeyboardLexicon.BACK
        is_state = _state not in UserState.EDIT_STATES

        return is_state and is_msg_text and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="MenuFilter.back_btn_query")
    async def back_btn_query(callback: CallbackQuery, state: FSMContext) -> bool:
        is_call_data = callback.data == KeyboardLexicon.BACK_CALL

        return is_call_data and MainFilter.is_admin(call=callback)
