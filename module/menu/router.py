from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from addons import MainFilter

from module.menu.filter import MenuFilter
from module.menu.service import MenuService

menu_router = Router(name="menu_router")


@menu_router.message(Command(commands=["start"]), MainFilter.is_admin)
async def start_cmd(message: Message, state: FSMContext):
    await MenuService.start_cmd(message, state)


@menu_router.message(MenuFilter.back_btn)
async def back_btn(message: Message, state: FSMContext):
    await MenuService.back_btn(message, state)


@menu_router.callback_query(MenuFilter.back_btn_query)
async def back_btn_query(callback: CallbackQuery, state: FSMContext):
    await MenuService.back_btn_query(callback, state)
