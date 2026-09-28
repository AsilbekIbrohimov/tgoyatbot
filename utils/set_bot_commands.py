from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Botni ishga tushurish"),
            BotCommand(command="help", description="Yordam"),
            BotCommand(command="search", description="Oyatdan qidirish"),
        ]
    )
