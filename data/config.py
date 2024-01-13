from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# BOT_TOKEN = '5204190868:AAGdR_cSlHjxw8S1nkkSUyoCr3lTMivjgMw'
# ADMINS = ['1024522810']
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5268428809:AAG-n1suE_60J5sJjK6gEPmuirpetxkSVFk"#env.str("BOT_TOKEN")  # Bot toekn
ADMINS = [1024522810,2090089858]#env.list("ADMINS")  # adminlar ro'yxati
IP = 'localhost'#env.str("ip")  # Xosting ip manzili
TELEGRAM_SUPPORT_CHAT_ID = -1001772344700#env.int('TELEGRAM_SUPPORT_CHAT_ID')
BOT_ID=[5268428809,5419255283]#env.list('BOT_ID')