from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from addons import MainFilter

from addons.decorator import TelegramDecorator
from addons.lexicon import KeyboardLexicon


class EntryFilter:
    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.entry_btn")
    async def entry_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_CLOSE_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.close_all_btn")
    async def close_all_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.CLOSE_ALL_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.open_all_btn")
    async def open_all_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_ALL_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.open_close_admin_btn")
    async def open_close_admin_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_CLOSE_ADMIN_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.open_close_employee_btn")
    async def open_close_employee_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_CLOSE_EMPLOYEES_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.open_close_student_btn")
    async def open_close_student_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_CLOSE_STUDENTS_CALL

        return is_call_data and MainFilter.is_admin(call=call)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryFilter.open_close_guest_btn")
    async def open_close_guest_btn(call: CallbackQuery, state: FSMContext):
        is_call_data = call.data == KeyboardLexicon.OPEN_CLOSE_GUESTS_CALL

        return is_call_data and MainFilter.is_admin(call=call)
