from environs import Env

# Sozlamalar .env fayldan o'qiladi (maxfiy ma'lumotlar kodda saqlanmaydi)
env = Env()
env.read_env()


def _int_list(name, default):
    out = []
    for x in env.list(name, default):
        try:
            out.append(int(str(x).strip()))
        except ValueError:
            pass
    return out


BOT_TOKEN = env.str("BOT_TOKEN", "")                       # @BotFather tokeni (.env da bering)
ADMINS = _int_list("ADMINS", ["1024522810", "2090089858"])  # admin ID lari
BOT_ID = _int_list("BOT_ID", ["5268428809", "5419255283"])  # bot ID lari (feedback uchun)
TELEGRAM_SUPPORT_CHAT_ID = env.int("TELEGRAM_SUPPORT_CHAT_ID", -1001772344700)
IP = env.str("IP", "localhost")

# Mini App (WebApp) manzili
WEBAPP_URL = env.str("WEBAPP_URL", "https://asilbekibrohimov.github.io/oyatbot/webapp/")

# Admin panel paroli
ADMIN_PASSWORD = env.str("ADMIN_PASSWORD", "rtwgjmja")

# Mini App admin backend (aiohttp)
WEBAPP_API_PORT = env.int("WEBAPP_API_PORT", 8080)
WEBAPP_API_ENABLED = env.bool("WEBAPP_API_ENABLED", True)
