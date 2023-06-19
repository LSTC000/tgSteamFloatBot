from data.config import ROW_WIDTH

from data.callbacks import (
    CHANGE_PRICE_THRESHOLD_DATA,
    CHANGE_BUFF_PERCENT_THRESHOLD_DATA,
    CHANGE_STEAM_PERCENT_THRESHOLD_DATA,
    CHANGE_STEAM_RESAMPLE_DATA,
    CLOSE_CHANGE_SETTINGS_DATA,
    CHANGE_BUFF_PROXY_DATA,
    CHANGE_STEAM_PROXY_DATA
)

from data.messages import (
    CHANGE_PRICE_THRESHOLD_IKB_MESSAGE,
    CHANGE_BUFF_PERCENT_THRESHOLD_IKB_MESSAGE,
    CHANGE_STEAM_PERCENT_THRESHOLD_IKB_MESSAGE,
    CHANGE_STEAM_RESAMPLE_IKB_MESSAGE,
    CLOSE_CHANGE_SETTINGS_IKB_MESSAGE,
    CHANGE_BUFF_PROXY_IKB_MESSAGE,
    CHANGE_STEAM_PROXY_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def change_settings_ikb() -> InlineKeyboardMarkup:
    """
    :return: Клавиатура для изменения настроек.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(
        text=CHANGE_PRICE_THRESHOLD_IKB_MESSAGE,
        callback_data=CHANGE_PRICE_THRESHOLD_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CHANGE_BUFF_PERCENT_THRESHOLD_IKB_MESSAGE,
        callback_data=CHANGE_BUFF_PERCENT_THRESHOLD_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CHANGE_STEAM_PERCENT_THRESHOLD_IKB_MESSAGE,
        callback_data=CHANGE_STEAM_PERCENT_THRESHOLD_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CHANGE_STEAM_RESAMPLE_IKB_MESSAGE,
        callback_data=CHANGE_STEAM_RESAMPLE_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CHANGE_BUFF_PROXY_IKB_MESSAGE,
        callback_data=CHANGE_BUFF_PROXY_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CHANGE_STEAM_PROXY_IKB_MESSAGE,
        callback_data=CHANGE_STEAM_PROXY_DATA)
    )
    ikb.row(InlineKeyboardButton(
        text=CLOSE_CHANGE_SETTINGS_IKB_MESSAGE,
        callback_data=CLOSE_CHANGE_SETTINGS_DATA)
    )

    return ikb
