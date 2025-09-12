from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from addons.lexicon.keyboard import KeyboardLexicon


BACK_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.BACK,
    callback_data=KeyboardLexicon.BACK_CALL,
)

SPEC_BACK_BTN = KeyboardButton(text=KeyboardLexicon.BACK)

BACK_ADD_BTN = KeyboardButton(text=KeyboardLexicon.BACK)

ADMIN_BTN = KeyboardButton(text=KeyboardLexicon.ADMIN)
EMPLOYEE_BTN = KeyboardButton(text=KeyboardLexicon.EMPLOYEE)
STUDENT_BTN = KeyboardButton(text=KeyboardLexicon.STUDENT)
GUEST_BTN = KeyboardButton(text=KeyboardLexicon.GUEST)


class UserMarkup:
    back_markup = ReplyKeyboardMarkup(
        keyboard=[[BACK_ADD_BTN]],
        resize_keyboard=True,
    )

    type_markup = ReplyKeyboardMarkup(
        keyboard=[[ADMIN_BTN], [EMPLOYEE_BTN], [STUDENT_BTN], [GUEST_BTN], [BACK_ADD_BTN]],
        resize_keyboard=True,
    )

    spec_back_markup = ReplyKeyboardMarkup(
            keyboard=[[
                SPEC_BACK_BTN,
            ]],
            resize_keyboard=True,
        )

    @staticmethod
    def get_user_markup(is_open: bool, uid: str):
        EDIT_NAME_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.EDIT_NAME,
            callback_data=KeyboardLexicon.EDIT_NAME_CALL + str(uid),
        )

        EDIT_PHOTO_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.EDIT_PHOTO,
            callback_data=KeyboardLexicon.EDIT_PHOTO_CALL + str(uid),
        )

        EDIT_TYPE_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.EDIT_TYPE,
            callback_data=KeyboardLexicon.EDIT_TYPE_CALL + str(uid),
        )

        EDIT_DATE_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.EDIT_DATE,
            callback_data=KeyboardLexicon.EDIT_DATE_CALL + str(uid),
        )

        DELETE_BTN = InlineKeyboardButton(
            text=KeyboardLexicon.DELETE,
            callback_data=KeyboardLexicon.DELETE_CALL + str(uid),
        )

        if is_open:
            OPEN_CLOSE_BTN = InlineKeyboardButton(
                text=KeyboardLexicon.CLOSE,
                callback_data=KeyboardLexicon.CLOSE_CALL + str(uid),
            )
        else:
            OPEN_CLOSE_BTN = InlineKeyboardButton(
                text=KeyboardLexicon.OPEN,
                callback_data=KeyboardLexicon.OPEN_CALL + str(uid),
            )

        return InlineKeyboardMarkup(inline_keyboard=[
            [OPEN_CLOSE_BTN],
            [EDIT_NAME_BTN],
            [EDIT_PHOTO_BTN],
            [EDIT_TYPE_BTN],
            [EDIT_DATE_BTN],
            [DELETE_BTN],
            [BACK_BTN],
        ])

