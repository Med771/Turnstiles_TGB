from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from module.edit.filter import EditFilter
from module.edit.service import EditService


edit_router = Router(name="edit_router")

@edit_router.message(EditFilter.spec_back_btn)
async def edit_back_btn(message: Message, state: FSMContext):
    await EditService.spec_back_btn(message=message, state=state)


@edit_router.callback_query(EditFilter.edit_name_btn)
async def edit_name_btn(callback: CallbackQuery, state: FSMContext):
    await EditService.edit_name_btn(callback, state)


@edit_router.callback_query(EditFilter.edit_photo_btn)
async def edit_photo_btn(callback: CallbackQuery, state: FSMContext):
    await EditService.edit_photo_btn(callback, state)


@edit_router.callback_query(EditFilter.edit_type_btn)
async def edit_type_btn(callback: CallbackQuery, state: FSMContext):
    await EditService.edit_type_btn(callback, state)


@edit_router.callback_query(EditFilter.edit_date_btn)
async def edit_date_btn(callback: CallbackQuery, state: FSMContext):
    await EditService.edit_date_btn(callback, state)


@edit_router.callback_query(EditFilter.delete_btn)
async def delete_btn(callback: CallbackQuery, state: FSMContext):
    await EditService.delete_btn(callback, state)


@edit_router.message(EditFilter.edit_name)
async def edit_name(message: Message, state: FSMContext):
    await EditService.edit_name(message, state)


@edit_router.message(EditFilter.edit_photo)
async def edit_photo(message: Message, state: FSMContext):
    await EditService.edit_photo(message, state)


@edit_router.message(EditFilter.edit_type)
async def edit_type(message: Message, state: FSMContext):
    await EditService.edit_type(message, state)


@edit_router.message(EditFilter.edit_date)
async def edit_date(message: Message, state: FSMContext):
    await EditService.edit_date(message, state)
