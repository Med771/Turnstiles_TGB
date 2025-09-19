from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from utils import EditUtils

from tools.admin import AdminTools

from addons.markup import EntryMarkup, UserMarkup
from addons.decorator import TelegramDecorator
from addons.state import UserState
from addons.lexicon import UserLexicon


class EditService:
    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.spec_back_btn")
    async def spec_back_btn(message: Message, state: FSMContext):
        data = await state.get_data()

        await state.set_state(UserState.USER)

        msg = await message.answer(text=UserLexicon.DELETE_REPLY, reply_markup=ReplyKeyboardRemove())

        await AdminTools.delete_msg(msg)

        resp = await EditUtils.find_by_id(data.get("uid"))

        text = UserLexicon.USER.format(full_name=resp[2],
                                       type=resp[3],
                                       end_time=resp[4],
                                       action=UserLexicon.OPEN if resp[5] else UserLexicon.CLOSE)
        markup = UserMarkup.get_user_markup(is_open=resp[5], uid=resp[0])

        await message.answer(text=text, reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_name_btn")
    async def edit_name_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.set_state(UserState.EDIT_NAME)
        await state.update_data(uid=1)

        await callback.message.answer(text=UserLexicon.EDIT_NAME, reply_markup=UserMarkup.spec_back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_photo_btn")
    async def edit_photo_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.set_state(UserState.EDIT_PHOTO)
        await state.update_data(uid=1)

        await callback.message.answer(text=UserLexicon.EDIT_PHOTO, reply_markup=UserMarkup.spec_back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_type_btn")
    async def edit_type_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.set_state(UserState.EDIT_TYPE)
        await state.update_data(uid=1)

        await callback.message.answer(text=UserLexicon.EDIT_TYPE, reply_markup=UserMarkup.spec_back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_date_btn")
    async def edit_date_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(callback.message)

        await state.set_state(UserState.EDIT_DATE)
        await state.update_data(uid=1)

        await callback.message.answer(text=UserLexicon.EDIT_DATE, reply_markup=UserMarkup.spec_back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.delete_btn")
    async def delete_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.delete_msg(callback.message)

        data = await state.get_data()

        await state.set_state(UserState.USER)

        resp = await EditUtils.delete_by_id(data.get("uid"))

        if resp:
            await callback.message.answer(text=UserLexicon.DELETE_USER_SUCCESS, reply_markup=EntryMarkup.back_markup)
        else:
            await callback.message.answer(text=UserLexicon.DELETE_USER_ERROR, reply_markup=EntryMarkup.back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_name")
    async def edit_name(message: Message, state: FSMContext):
        data = await state.get_data()

        await state.set_state(UserState.USER)

        resp = await EditUtils.edit_name_by_uid(data.get("uid"), message.text)

        if resp:
            await message.answer(text=UserLexicon.EDIT_NAME_SUCCESS)
        else:
            await message.answer(text=UserLexicon.EDIT_NAME_ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_photo")
    async def edit_photo(message: Message, state: FSMContext):
        data = await state.get_data()

        await state.set_state(UserState.USER)

        resp = await EditUtils.edit_photo_by_uid(data.get("uid"), message.photo)

        if resp:
            await message.answer(text=UserLexicon.EDIT_PHOTO_SUCCESS)
        else:
            await message.answer(text=UserLexicon.EDIT_PHOTO_ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_type")
    async def edit_type(message: Message, state: FSMContext):
        data = await state.get_data()

        await state.set_state(UserState.USER)

        resp = await EditUtils.edit_type_by_uid(data.get("uid"), message.text)

        if resp:
            await message.answer(text=UserLexicon.EDIT_TYPE_SUCCESS)
        else:
            await message.answer(text=UserLexicon.EDIT_TYPE_ERROR)

    @staticmethod
    @TelegramDecorator.log_call(prefix="EditService.edit_date")
    async def edit_date(message: Message, state: FSMContext):
        data = await state.get_data()

        await state.set_state(UserState.USER)

        resp = await EditUtils.edit_date_by_uid(data.get("uid"), message.text)

        if resp:
            await message.answer(text=UserLexicon.EDIT_DATE_SUCCESS)
        else:
            await message.answer(text=UserLexicon.EDIT_DATE_ERROR)
