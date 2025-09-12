from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons import MainFilter

from addons.state import FindState
from addons.decorator import TelegramDecorator
from addons.lexicon import KeyboardLexicon


class FindFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="FindFilter.find_btn")
    async def find_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = callback.data == KeyboardLexicon.FIND_CALL

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="FindFilter.find_msg")
    async def find_msg(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == FindState.FIND

        return is_state and MainFilter.is_admin(msg=message)
