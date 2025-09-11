from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from addons.lexicon.keyboard import KeyboardLexicon


ENTRY_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.OPEN_CLOSE,
    callback_data=KeyboardLexicon.OPEN_CLOSE_CALL,)

ADD_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.ADD,
    callback_data=KeyboardLexicon.ADD_CAL
)

FIND_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.FIND,
    callback_data=KeyboardLexicon.FIND_CALL
)


class MenuMarkup:
    START_MARKUP = InlineKeyboardMarkup(
        inline_keyboard=[
            [ENTRY_BTN],
            [ADD_BTN],
            [FIND_BTN]
        ]
    )
