from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from addons.lexicon.keyboard import KeyboardLexicon


BACK_BTN = InlineKeyboardButton(
    text=KeyboardLexicon.BACK,
    callback_data=KeyboardLexicon.BACK_CALL,
)


class FindMarkup:
    back_markup = InlineKeyboardMarkup(
        inline_keyboard=[[BACK_BTN]],
    )
