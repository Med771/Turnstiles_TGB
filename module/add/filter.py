from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons import MainFilter

from addons.state import UserState
from addons.decorator import TelegramDecorator
from addons.lexicon import KeyboardLexicon


class AddFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.spec_back_btn")
    async def back_btn(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) in UserState.ADD_STATES
        is_msg = message.text == KeyboardLexicon.BACK

        return is_state and is_msg and MainFilter.is_admin(message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.add_btn")
    async def add_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = callback.data == KeyboardLexicon.ADD_CAL

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.add_name")
    async def add_name(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.ADD_NAME

        return is_state and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.add_photo")
    async def add_photo(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.ADD_PHOTO
        is_photo = message.photo

        return is_photo and is_state and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.add_type")
    async def add_type(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.ADD_TYPE
        is_msg = message.text in KeyboardLexicon.TYPES

        return is_msg and is_state and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.add_date")
    async def add_date(message: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.ADD_DATE

        return is_state and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddFilter.open_close_btn")
    async def open_close_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.OPEN_CALL in callback.data or KeyboardLexicon.CLOSE_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)
