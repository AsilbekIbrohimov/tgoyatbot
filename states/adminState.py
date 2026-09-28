from aiogram.fsm.state import StatesGroup, State


class AdminState(StatesGroup):
    parol = State()
    admin = State()
    reklama = State()


class Feedback(StatesGroup):
    waiting = State()


class Settings(StatesGroup):
    menu = State()
    trans = State()
    reciter = State()
