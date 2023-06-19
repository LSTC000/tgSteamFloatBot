from data.messages import (
    START_SHORT_COMMAND_MESSAGE,
    START_PARSE_SHORT_COMMAND_MESSAGE,
    STOP_PARSE_SHORT_COMMAND_MESSAGE,
    CHANGE_SETTINGS_SHORT_COMMAND_MESSAGE
)

from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description=START_SHORT_COMMAND_MESSAGE),
            BotCommand(command='start_parse', description=START_PARSE_SHORT_COMMAND_MESSAGE),
            BotCommand(command='stop_parse', description=STOP_PARSE_SHORT_COMMAND_MESSAGE),
            BotCommand(command='change_settings', description=CHANGE_SETTINGS_SHORT_COMMAND_MESSAGE)
        ]
    )
