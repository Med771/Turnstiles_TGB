from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from addons import MainFilter

from addons.state import UserState
from addons.decorator import TelegramDecorator
from addons.lexicon import KeyboardLexicon


class EditFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.spec_back_btn")
    async def spec_back_btn(message: Message, state: FSMContext):
        is_msg = message.text == KeyboardLexicon.BACK
        is_state = await MainFilter.get_state(state) in UserState.EDIT_STATES

        return is_state and is_msg and MainFilter.is_admin(msg=message)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_name_btn")
    async def edit_name_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.EDIT_NAME_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_name")
    async def edit_name(msg: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.EDIT_NAME

        return is_state and MainFilter.is_admin(msg=msg)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_photo_btn")
    async def edit_photo_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.EDIT_PHOTO_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_photo")
    async def edit_photo(msg: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.EDIT_PHOTO
        is_photo = msg.photo

        return is_photo  and MainFilter.is_admin(msg=msg)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_type_btn")
    async def edit_type_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.EDIT_TYPE_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_type")
    async def edit_type(msg: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.EDIT_TYPE
        is_msg = msg.text in KeyboardLexicon.TYPES

        return is_msg and is_state and MainFilter.is_admin(msg=msg)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_date_btn")
    async def edit_date_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.EDIT_DATE_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.edit_date")
    async def edit_date(msg: Message, state: FSMContext):
        is_state = await MainFilter.get_state(state) == UserState.EDIT_DATE

        return is_state and MainFilter.is_admin(msg=msg)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditFilter.delete_btn")
    async def delete_btn(callback: CallbackQuery, state: FSMContext):
        is_call_data = KeyboardLexicon.DELETE_CALL in callback.data

        return is_call_data and MainFilter.is_admin(call=callback)
