from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    USER = State(state="UserState.USER")

    EDIT_NAME = State(state="UserState.EDIT_NAME")
    EDIT_PHOTO = State(state="UserState.EDIT_PHOTO")
    EDIT_TYPE = State(state="UserState.EDIT_TYPE")
    EDIT_DATE = State(state="UserState.EDIT_DATE")

    ADD_NAME = State(state="UserState.ADD_NAME")
    ADD_PHOTO = State(state="UserState.ADD_PHOTO")
    ADD_TYPE = State(state="UserState.ADD_TYPE")
    ADD_DATE = State(state="UserState.ADD_DATE")

    ADD_STATES: tuple = (
        ADD_NAME,
        ADD_PHOTO,
        ADD_TYPE,
        ADD_DATE)

    EDIT_STATES: tuple = (
        EDIT_NAME,
        EDIT_PHOTO,
        EDIT_TYPE,
        EDIT_DATE,
        USER
    )
