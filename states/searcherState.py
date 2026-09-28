from aiogram.fsm.state import StatesGroup, State


class Searcher(StatesGroup):
    """Umumiy izlash (butun Qur'on bo'yicha)."""
    search = State()


class OyatRead(StatesGroup):
    """Oyat o'qish: sura tanlash -> oyat(lar)ni o'qish."""
    choose_sura = State()
    reading = State()


class SuraSearch(StatesGroup):
    """Bitta sura ichidan izlash: sura tanlash -> qidirish."""
    choose_sura = State()
    searching = State()
