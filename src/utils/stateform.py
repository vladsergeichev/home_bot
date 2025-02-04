from aiogram.fsm.state import StatesGroup, State


class AppealsForm(StatesGroup):
    GET_NUMBER = State()
    TYPE_ENTRY = State()
