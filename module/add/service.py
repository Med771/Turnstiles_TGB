from datetime import datetime

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from tools.admin import AdminTools

from addons.markup import UserMarkup, MenuMarkup, EntryMarkup
from addons.decorator import TelegramDecorator
from addons.lexicon import UserLexicon, MenuLexicon, KeyboardLexicon
from addons.state import UserState


class AddService:
    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.back_btn")
    async def back_btn(message: Message, state: FSMContext):
        is_state = await state.get_state()

        if is_state == UserState.ADD_DATE:
            await state.set_state(UserState.ADD_TYPE)

            await message.answer(text=UserLexicon.ADD_TYPE, reply_markup=UserMarkup.type_markup)
        elif is_state == UserState.ADD_TYPE:
            await state.set_state(UserState.ADD_PHOTO)

            await message.answer(text=UserLexicon.ADD_PHOTO, reply_markup=UserMarkup.back_markup)
        elif is_state == UserState.ADD_PHOTO:
            await state.set_state(UserState.ADD_NAME)

            await message.answer(text=UserLexicon.ADD_NAME, reply_markup=UserMarkup.back_markup)
        else:
            await state.clear()

            is_admin = AdminTools.is_admin(message.chat.id)

            msg = await message.answer(text=UserLexicon.DELETE_REPLY, reply_markup=ReplyKeyboardRemove())

            await AdminTools.delete_msg(msg)

            if is_admin:
                text = MenuLexicon.ADMIN_PANEL_TEXT
                markup = MenuMarkup.START_MARKUP
            else:
                text = MenuLexicon.USER_PANEL_TEXT
                markup = None

            await message.answer(text=text,reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.add_btn")
    async def add_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(message=callback.message)

        await state.set_state(UserState.ADD_NAME)
        await state.set_data({
            "full_name": "",
            "photo": b"",
            "type": "",
            "date": ""
        })

        await callback.message.answer(text=UserLexicon.ADD_NAME, reply_markup=UserMarkup.back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.add_name")
    async def add_name(message: Message, state: FSMContext):
        await state.set_state(UserState.ADD_PHOTO)
        await state.update_data(full_name=message.text)

        await message.answer(text=UserLexicon.ADD_PHOTO, reply_markup=UserMarkup.back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.add_photo")
    async def add_photo(message: Message, state: FSMContext):
        await state.set_state(UserState.ADD_TYPE)
        await state.update_data(photo=message.photo)

        await message.answer(text=UserLexicon.ADD_TYPE, reply_markup=UserMarkup.type_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.add_type")
    async def add_type(message: Message, state: FSMContext):
        await state.set_state(UserState.ADD_DATE)
        await state.update_data(type=message.text)

        await message.answer(text=UserLexicon.ADD_DATE, reply_markup=UserMarkup.back_markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.add_date")
    async def add_date(message: Message, state: FSMContext):
        await AdminTools.edit_reply(message=message)

        try:
            date = datetime.strptime(message.text, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            await message.answer(text=UserLexicon.DATE_ERROR, reply_markup=UserMarkup.back_markup)

            return

        data = await state.get_data()

        msg = await message.answer(text=UserLexicon.DELETE_REPLY, reply_markup=ReplyKeyboardRemove())

        await AdminTools.delete_msg(msg)

        await state.clear()

        resp = ("0",)

        text = UserLexicon.USER.format(full_name=data.get("full_name", ""),
                                       type=data.get("type", ""),
                                       end_time=message.text,
                                       action=UserLexicon.OPEN if True else UserLexicon.CLOSE)
        markup = UserMarkup.get_user_markup(is_open=True, uid=resp[0])

        await message.answer(text=text, reply_markup=markup)

    @staticmethod
    @TelegramDecorator.log_call(prefix="AddService.open_close_btn")
    async def open_close_btn(callback: CallbackQuery, state: FSMContext):
        await AdminTools.edit_reply(message=callback.message)

        if KeyboardLexicon.OPEN_CALL in callback.data:
            action = "открыт"
        else:
            action = "закрыт"

        resp = True

        if resp:
            await callback.message.answer(text=UserLexicon.ACTION_SUCCESS.format(action=action), reply_markup=EntryMarkup.back_markup)
        else:
            await callback.message.answer(text=UserLexicon.ACTION_SUCCESS.format(action=action), reply_markup=EntryMarkup.back_markup)
