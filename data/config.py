from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# BOT_TOKEN = '5204190868:AAGdR_cSlHjxw8S1nkkSUyoCr3lTMivjgMw'
# ADMINS = ['1024522810']
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
TELEGRAM_SUPPORT_CHAT_ID = env.int('TELEGRAM_SUPPORT_CHAT_ID')
BOT_ID=env.list('BOT_ID')