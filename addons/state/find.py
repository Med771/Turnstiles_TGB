from aiogram.fsm.state import StatesGroup, State


class FindState(StatesGroup):
    FIND = State(state="FindState.FIND")
