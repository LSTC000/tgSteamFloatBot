__all__ = ['register_commands', 'set_default_commands']


from .start import start_command
from .start_parse import start_parse_command
from .stop_parse import stop_parse_command
from .change_settings import change_settings_command
from .setting_commands import set_default_commands

from aiogram import Dispatcher


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_command)
    dp.register_message_handler(start_parse_command)
    dp.register_message_handler(stop_parse_command)
    dp.register_message_handler(change_settings_command)
