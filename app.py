import asyncio
import logging

import utils.misc.logging  # noqa: F401  (logging sozlamasi)
from aiogram.types import MenuButtonWebApp, WebAppInfo
from loader import bot, dp, db, db2
import middlewares
import handlers
from data.config import WEBAPP_URL
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify


async def on_startup():
    await set_default_commands(bot)
    # Chap-pastdagi "menu" tugmasini Mini App'ga bog'laymiz
    try:
        await bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(text="Qur'on", web_app=WebAppInfo(url=WEBAPP_URL))
        )
    except Exception as err:
        logging.exception(err)
    try:
        db.create_table_users()
        db2.create_table_messages()
    except Exception as err:
        logging.exception(err)
    await on_startup_notify(bot)


async def _start_web():
    """Mini App admin backendini (aiohttp) ishga tushiradi."""
    from aiohttp import web
    from utils.webserver import create_app
    from data.config import WEBAPP_API_PORT
    runner = web.AppRunner(create_app())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', WEBAPP_API_PORT)
    await site.start()
    logging.info("Admin backend http://0.0.0.0:%s da ishga tushdi", WEBAPP_API_PORT)


async def main():
    # Middleware'lar
    middlewares.setup(dp)

    # Routerlar (tartib bilan)
    for router in handlers.user_routers:
        dp.include_router(router)
    dp.include_router(handlers.errors_router)

    await on_startup()

    from data.config import WEBAPP_API_ENABLED
    if WEBAPP_API_ENABLED:
        try:
            await _start_web()
        except Exception as err:
            logging.exception(err)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi")
