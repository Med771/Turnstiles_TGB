from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from utils import FindUtils

from tools.admin import AdminTools

from addons.state import FindState
from addons.decorator import TelegramDecorator

from addons.markup import FindMarkup
from addons.markup import UserMarkup

from addons.lexicon import FindLexicon
from addons.lexicon import UserLexicon


class FindService:
    @staticmethod
    @TelegramDecorator.log_call(prefix="FindService.find_btn")
    async def find_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.set_state(FindState.FIND)

        await callback.message.answer(text=FindLexicon.FIND, reply_markup=FindMarkup.back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="FindService.find_msg")
    async def find_msg(message: Message, state: FSMContext):
        await state.clear()

        resp = await FindUtils.find_user(message.text)

        if resp:
            text = UserLexicon.USER.format(full_name=resp[2],
                                           type=resp[3],
                                           end_time=resp[4],
                                           action=UserLexicon.OPEN if resp[5] else UserLexicon.CLOSE)
            markup = UserMarkup.get_user_markup(is_open=resp[5], uid=resp[0])

            await message.answer(text=text, reply_markup=markup)
        else:
            await message.answer(text=UserLexicon.USER_NOT_FOUND, reply_markup=FindMarkup.back_markup)
