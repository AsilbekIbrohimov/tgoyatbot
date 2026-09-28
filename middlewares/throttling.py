import time
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


class ThrottlingMiddleware(BaseMiddleware):
    """Oddiy anti-flud: bir foydalanuvchidan juda tez kelgan xabarlarni tashlaydi."""

    def __init__(self, rate_limit: float = 0.4):
        self.rate_limit = rate_limit
        self._last: Dict[int, float] = {}
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user = getattr(event, "from_user", None)
        if user is not None:
            now = time.monotonic()
            last = self._last.get(user.id, 0.0)
            self._last[user.id] = now
            if now - last < self.rate_limit:
                return  # xabarni e'tiborsiz qoldiramiz
        return await handler(event, data)
