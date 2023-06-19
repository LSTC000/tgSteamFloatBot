__all__ = ['register_change_settings']


from .change_price_threshold import change_price_threshold, enter_price_threshold
from .change_buff_percent_threshold import change_buff_percent_threshold, enter_buff_percent_threshold
from .change_steam_percent_threshold import change_steam_percent_threshold, enter_steam_percent_threshold
from .change_steam_resample import change_steam_resample, enter_steam_resample
from .change_buff_proxy import change_buff_proxy, enter_buff_proxy
from .change_steam_proxy import change_steam_proxy, enter_steam_proxy
from .close_change_settings import close_change_settings

from aiogram import Dispatcher


def register_change_settings(dp: Dispatcher):
    dp.register_callback_query_handler(change_price_threshold)
    dp.register_message_handler(enter_price_threshold)
    dp.register_callback_query_handler(change_buff_percent_threshold)
    dp.register_message_handler(enter_buff_percent_threshold)
    dp.register_callback_query_handler(change_steam_percent_threshold)
    dp.register_message_handler(enter_steam_percent_threshold)
    dp.register_callback_query_handler(change_steam_resample)
    dp.register_message_handler(enter_steam_resample)
    dp.register_callback_query_handler(change_buff_proxy)
    dp.register_message_handler(enter_buff_proxy)
    dp.register_callback_query_handler(change_steam_proxy)
    dp.register_message_handler(enter_steam_proxy)
    dp.register_callback_query_handler(close_change_settings)
