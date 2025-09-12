from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from module.add.filter import AddFilter
from module.add.service import AddService


add_router = Router(name="add_router")


@add_router.message(AddFilter.back_btn)
async def back_btn(message: Message, state: FSMContext):
    await AddService.back_btn(message=message, state=state)


@add_router.callback_query(AddFilter.add_btn)
async def add_btn(callback: CallbackQuery, state: FSMContext):
    await AddService.add_btn(callback, state)


@add_router.message(AddFilter.add_name)
async def add_name(message: Message, state: FSMContext):
    await AddService.add_name(message, state)


@add_router.message(AddFilter.add_photo)
async def add_photo(message: Message, state: FSMContext):
    await AddService.add_photo(message, state)


@add_router.message(AddFilter.add_type)
async def add_type(message: Message, state: FSMContext):
    await AddService.add_type(message, state)


@add_router.message(AddFilter.add_date)
async def add_date(message: Message, state: FSMContext):
    await AddService.add_date(message, state)


@add_router.callback_query(AddFilter.open_close_btn)
async def open_close_btn(callback: CallbackQuery, state: FSMContext):
    await AddService.open_close_btn(callback, state)
