from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from module.entry.filter import EntryFilter
from module.entry.service import EntryService


entry_router = Router(name="entry_router")


@entry_router.callback_query(EntryFilter.entry_btn)
async def entry_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.entry_btn(callback, state)


@entry_router.callback_query(EntryFilter.close_all_btn)
async def close_all_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.close_all_btn(callback, state)


@entry_router.callback_query(EntryFilter.open_all_btn)
async def open_all_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.open_all_btn(callback, state)


@entry_router.callback_query(EntryFilter.open_close_admin_btn)
async def open_close_admin_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.open_close_admin_btn(callback, state)


@entry_router.callback_query(EntryFilter.open_close_employee_btn)
async def open_close_employee_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.open_close_employee_btn(callback, state)


@entry_router.callback_query(EntryFilter.open_close_student_btn)
async def open_close_student_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.open_close_student_btn(callback, state)


@entry_router.callback_query(EntryFilter.open_close_guest_btn)
async def open_close_guest_btn(callback: CallbackQuery, state: FSMContext):
    await EntryService.open_close_guest_btn(callback, state)
