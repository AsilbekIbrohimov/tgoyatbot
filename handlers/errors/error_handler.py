import logging

from aiogram import Router
from aiogram.types import ErrorEvent

errors_router = Router()


@errors_router.errors()
async def errors_handler(event: ErrorEvent):
    """Barcha ushlanmagan xatolarni jurnalga yozadi."""
    logging.exception(
        "Update: %s\nException: %s", event.update, event.exception
    )
    return True
