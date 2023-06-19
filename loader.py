import logging

from data.config import (
    BOT_TOKEN,
    PARSE_MODE,
    DISABLE_WEB_PAGE_PREVIEW,
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    ITEMS_MAXSIZE,
    ITEMS_TTL
)

from cachetools import TTLCache

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2


__all__ = ['bot', 'dp', 'items_cache', 'logger']

storage = RedisStorage2(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

bot = Bot(token=BOT_TOKEN, parse_mode=PARSE_MODE, disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW)
dp = Dispatcher(bot=bot, storage=storage)

items_cache = TTLCache(maxsize=ITEMS_MAXSIZE, ttl=ITEMS_TTL)

logger = logging.getLogger(__name__)
