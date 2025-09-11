from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from tools.admin import AdminTools

from utils.entry import EntryUtils

from addons.markup import EntryMarkup
from addons.decorator import TelegramDecorator
from addons.lexicon import EntryLexicon
from addons.state import EntryState


class EntryService:
    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.entry_btn")
    async def entry_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        await state.set_state(EntryState.ENTRY)

        res: tuple[bool, bool, bool, bool] = EntryUtils.check_status()

        is_admin_open: bool = res[0]
        is_employee_open: bool = res[1]
        is_student_open: bool = res[2]
        is_guest_open: bool = res[3]

        await state.set_data({
            "is_admin_open": is_admin_open,
            "is_employee_open": is_employee_open,
            "is_student_open": is_student_open,
            "is_guest_open": is_guest_open,
        })

        _open = EntryLexicon.OPEN
        _close = EntryLexicon.CLOSE

        text = EntryLexicon.INFO.format(status_admin=_open if is_admin_open else _close,
                                        status_employee=_open if is_employee_open else _close,
                                        status_student=_open if is_student_open else _close,
                                        status_guest=_open if is_guest_open else _close)

        markup = EntryMarkup.get_entry_markup(is_admin_open=is_admin_open,
                                              is_employee_open=is_employee_open,
                                              is_student_open=is_student_open,
                                              is_guest_open=is_guest_open)

        await callback.message.answer(text=text, reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.close_all_btn")
    async def close_all_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        await state.clear()

        resp = EntryUtils.close_all()

        text = EntryLexicon.ALL_SUCCESS.format(action="закрыт") if resp else EntryLexicon.ALL_ERROR.format(action="закрыт")
        markup = EntryMarkup.back_markup

        await callback.message.answer(text=text, reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.open_all_btn")
    async def open_all_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        await state.clear()

        resp = EntryUtils.open_all()

        text = EntryLexicon.ALL_SUCCESS.format(action="открыт") if resp else EntryLexicon.ALL_ERROR.format(action="открыт")
        markup = EntryMarkup.back_markup

        await callback.message.answer(text=text, reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.open_close_admin_btn")
    async def open_close_admin_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        status: dict = await state.get_data()

        await state.clear()

        if "is_admin_open" in status:
            resp = EntryUtils.set_admin_entry(status["is_admin_open"])

            markup = EntryMarkup.back_markup
            text = "закрыт" if status["is_admin_open"] else "открыт"

            if resp:
                await callback.message.answer(text=EntryLexicon.ADMIN_SUCCESS.format(action=text), reply_markup=markup)
            else:
                await callback.message.answer(text=EntryLexicon.ADMIN_ERROR.format(action=text), reply_markup=markup)

            return

        await callback.message.answer(text=EntryLexicon.ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.open_close_employee_btn")
    async def open_close_employee_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        status: dict = await state.get_data()

        await state.clear()

        if "is_employee_open" in status:
            resp = EntryUtils.set_admin_entry(status["is_employee_open"])

            markup = EntryMarkup.back_markup
            text = "закрыт" if status["is_employee_open"] else "открыт"

            if resp:
                await callback.message.answer(text=EntryLexicon.EMPLOYEE_SUCCESS.format(action=text), reply_markup=markup)
            else:
                await callback.message.answer(text=EntryLexicon.EMPLOYEE_ERROR.format(action=text), reply_markup=markup)

            return

        await callback.message.answer(text=EntryLexicon.ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.open_close_student_btn")
    async def open_close_student_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        status: dict = await state.get_data()

        await state.clear()

        if "is_student_open" in status:
            resp = EntryUtils.set_admin_entry(status["is_student_open"])

            markup = EntryMarkup.back_markup
            text = "закрыт" if status["is_student_open"] else "открыт"

            if resp:
                await callback.message.answer(text=EntryLexicon.STUDENT_SUCCESS.format(action=text), reply_markup=markup)
            else:
                await callback.message.answer(text=EntryLexicon.STUDENT_ERROR.format(action=text), reply_markup=markup)

            return

        await callback.message.answer(text=EntryLexicon.ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EntryService.open_close_guest_btn")
    async def open_close_guest_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        status: dict = await state.get_data()

        await state.clear()

        if "is_guest_open" in status:
            resp = EntryUtils.set_admin_entry(status["is_guest_open"])

            markup = EntryMarkup.back_markup
            text = "закрыт" if status["is_guest_open"] else "открыт"

            if resp:
                await callback.message.answer(text=EntryLexicon.GUEST_SUCCESS.format(action=text), reply_markup=markup)
            else:
                await callback.message.answer(text=EntryLexicon.GUEST_ERROR.format(action=text), reply_markup=markup)

            return

        await callback.message.answer(text=EntryLexicon.ERROR)