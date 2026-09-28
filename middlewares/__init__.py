from .throttling import ThrottlingMiddleware


def setup(dp):
    """Middleware'larni dispatcher'ga ulaydi (app.py dan chaqiriladi)."""
    dp.message.middleware(ThrottlingMiddleware())
