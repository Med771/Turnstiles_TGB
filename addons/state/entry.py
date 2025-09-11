from aiogram.fsm.state import StatesGroup, State


class EntryState(StatesGroup):
    ENTRY = State(state="EntryState.ENTRY")
