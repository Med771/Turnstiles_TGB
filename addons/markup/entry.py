from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from addons.lexicon.keyboard import KeyboardLexicon


OPEN_ALL_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.OPEN_ALL,
    callback_data=KeyboardLexicon.OPEN_ALL_CALL,
)

CLOSE_ALL_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.CLOSE_ALL,
    callback_data=KeyboardLexicon.CLOSE_ALL_CALL,
)

BACK_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.BACK,
    callback_data=KeyboardLexicon.BACK_CALL,
)


class EntryMarkup:
    back_markup = InlineKeyboardMarkup(
        inline_keyboard=[[BACK_BTN]],
    )


    @staticmethod
    def get_entry_markup(is_admin_open: bool,
                         is_employee_open: bool,
                         is_student_open: bool,
                         is_guest_open: bool) -> InlineKeyboardMarkup:
        ENTRY_ADMIN_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.OPEN_ADMINS if not is_admin_open else KeyboardLexicon.CLOSE_ADMINS,
            callback_data=KeyboardLexicon.OPEN_CLOSE_ADMIN_CALL
        )

        ENTRY_EMPLOYEE_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.OPEN_EMPLOYEES if not is_employee_open else KeyboardLexicon.CLOSE_EMPLOYEES,
            callback_data=KeyboardLexicon.OPEN_CLOSE_EMPLOYEES_CALL
        )

        ENTRY_STUDENT_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.OPEN_STUDENTS if not is_student_open else KeyboardLexicon.CLOSE_STUDENTS,
            callback_data=KeyboardLexicon.OPEN_CLOSE_STUDENTS_CALL
        )

        ENTRY_GUEST_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.OPEN_GUESTS if not is_guest_open else KeyboardLexicon.CLOSE_GUESTS,
            callback_data=KeyboardLexicon.OPEN_CLOSE_GUESTS_CALL
        )

        return InlineKeyboardMarkup(
            inline_keyboard=[
                [OPEN_ALL_BTN],
                [ENTRY_ADMIN_BTN],
                [ENTRY_EMPLOYEE_BTN],
                [ENTRY_STUDENT_BTN],
                [ENTRY_GUEST_BTN],
                [CLOSE_ALL_BTN],
                [BACK_BTN],
            ]
        )