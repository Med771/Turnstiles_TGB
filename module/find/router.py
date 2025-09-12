from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from module.find.filter import FindFilter
from module.find.service import FindService


find_router = Router(name="find_router")


@find_router.callback_query(FindFilter.find_btn)
async def find_btn(callback:CallbackQuery, state: FSMContext):
    await FindService.find_btn(callback, state)


@find_router.message(FindFilter.find_msg)
async def find_msg(message: Message, state: FSMContext):
    await FindService.find_msg(message, state)
