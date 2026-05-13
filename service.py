

from .models import TelegramUser


def get_user(telegram_id: str | int) -> TelegramUser | None:

    try:
        user = TelegramUser.get(telegram_id=telegram_id)
    except Exception:
        user = None

    return user






