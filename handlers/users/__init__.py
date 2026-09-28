"""Foydalanuvchi routerlari — tartib muhim (aniqroq handlerlar avval)."""
from .start import start_router
from .admin import admin_router
from .donate import donate_router
from .menu import menu_router
from .settings import settings_router
from .regex import regex_router
from .search_global import global_router
from .sura_read import read_router
from .sura_search import sura_search_router
from .feedback import feedback_router
from .inline import inline_router
from .fallback import fallback_router

routers = [
    start_router,
    admin_router,
    donate_router,
    menu_router,
    settings_router,
    regex_router,
    global_router,
    read_router,
    sura_search_router,
    feedback_router,
    inline_router,
    fallback_router,  # eng oxirida
]
