from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tools.admin import AdminTools

from addons.markup import MenuMarkup
from addons.decorator import TelegramDecorator
from addons.lexicon import MenuLexicon


class MenuService:
    @staticmethod
    @TelegramDecorator.log_call(prefix="MenuService.start_cmd")
    async def start_cmd(message: Message, state: FSMContext):
        await state.clear()

        is_admin = AdminTools.is_admin(message.chat.id)

        if is_admin:
            text = MenuLexicon.ADMIN_PANEL_TEXT
        else:
            text = MenuLexicon.USER_PANEL_TEXT

        await message.answer(text=text, reply_markup=MenuMarkup.START_MARKUP)

    @staticmethod
    @TelegramDecorator.log_call(prefix="MenuService.back_btn")
    async def back_btn(message: Message, state: FSMContext):
        await state.clear()

        await AdminTools.edit_reply(message)

        await MenuService.start_cmd(message, state)

    @staticmethod
    @TelegramDecorator.log_call(prefix="MenuService.back_btn_query")
    async def back_btn_query(call: CallbackQuery, state: FSMContext):
        await state.clear()

        await AdminTools.edit_reply(call.message)

        await MenuService.start_cmd(call.message, state)
