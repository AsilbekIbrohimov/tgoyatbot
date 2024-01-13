from aiogram import executor
from loader import dp, db, bot, db2
import middlewares, handlers
from data.config import ADMINS#, #filters
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Ma'lumotlar bazasini yaratamiz:
    try:
        db.create_table_users()
        db2.create_table_messages()
    except Exception as err:
        print(err)
        await bot.send_message(chat_id = ADMINS[0], text = str(err))

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
