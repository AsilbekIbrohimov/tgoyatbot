from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# BOT_TOKEN = '5204190868:AAGdR_cSlHjxw8S1nkkSUyoCr3lTMivjgMw'
# ADMINS = ['1024522810']
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN", "5268428809:AAG-n1suE_60J5sJjK6gEPmuirpetxkSVFk")  # avval .env dan o'qiladi
ADMINS = [1024522810,2090089858]#env.list("ADMINS")  # adminlar ro'yxati
IP = 'localhost'#env.str("ip")  # Xosting ip manzili
TELEGRAM_SUPPORT_CHAT_ID = -1001772344700#env.int('TELEGRAM_SUPPORT_CHAT_ID')
BOT_ID=[5268428809,5419255283]#env.list('BOT_ID')

# Telegram Mini App (WebApp) manzili — HTTPS bo'lishi shart.
# Deploy qilgach o'zgartiring yoki .env da WEBAPP_URL bering.
WEBAPP_URL = env.str("WEBAPP_URL", "https://asilbekibrohimov.github.io/oyatbot/webapp/")