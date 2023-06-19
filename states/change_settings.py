from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeSettingsStatesGroup(StatesGroup):
    change_settings = State()
    change_price_threshold = State()
    change_buff_percent_threshold = State()
    change_steam_percent_threshold = State()
    change_buff_proxy = State()
    change_steam_proxy = State()
    change_steam_resample = State()
