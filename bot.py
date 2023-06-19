import logging

from data.config import SKIP_UPDATES

from loader import dp, bot, logger

from handlers import (
    register_commands,
    set_default_commands,
    register_change_settings
)

from aiogram import Bot, Dispatcher
from aiogram.utils import executor


def register_all_handlers(dispatcher: Dispatcher):
    register_change_settings(dispatcher)
    register_commands(dispatcher)


async def set_all_default_commands(_bot: Bot):
    await set_default_commands(_bot)


async def on_startup(dispatcher: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Set all default commands')
    await set_all_default_commands(bot)

    logger.info('Register all handlers')
    register_all_handlers(dispatcher)

    logger.info('Starting bot!')


async def on_shutdown(dispatcher: Dispatcher):
    logger.info('Closing storage')
    await dp.storage.close()

    logger.info('Bot successfully stopped!')


if __name__ == '__main__':
    try:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=SKIP_UPDATES
        )
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
        raise
