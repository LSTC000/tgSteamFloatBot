from loader import dp, bot

from data.callbacks import CHANGE_STEAM_PERCENT_THRESHOLD_DATA

from data.redis import LAST_IKB_REDIS_KEY, STEAM_PERCENT_THRESHOLD_REDIS_KEY

from data.messages import (
    CHANGE_STEAM_PERCENT_THRESHOLD_MESSAGE,
    SUCCESSFULLY_SAVE_STEAM_PERCENT_THRESHOLD_MESSAGE,
    ERROR_SAVE_STEAM_PERCENT_THRESHOLD_MESSAGE,
    CHANGE_SETTINGS_COMMAND_MESSAGE
)

from keyboards import change_settings_ikb

from functions import keyboards_clear

from states import ChangeSettingsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CHANGE_STEAM_PERCENT_THRESHOLD_DATA,
    state=ChangeSettingsStatesGroup.change_settings
)
async def change_steam_percent_threshold(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    await keyboards_clear(user_id=user_id, state=state)
    await bot.send_message(chat_id=user_id, text=CHANGE_STEAM_PERCENT_THRESHOLD_MESSAGE)

    await ChangeSettingsStatesGroup.change_steam_percent_threshold.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=ChangeSettingsStatesGroup.change_steam_percent_threshold
)
async def enter_steam_percent_threshold(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    async with state.proxy() as data:
        try:
            steam_percent_threshold = float(message.text)
            if steam_percent_threshold >= 0:
                data[STEAM_PERCENT_THRESHOLD_REDIS_KEY] = steam_percent_threshold
                await bot.send_message(chat_id=user_id, text=SUCCESSFULLY_SAVE_STEAM_PERCENT_THRESHOLD_MESSAGE)
            else:
                await bot.send_message(chat_id=user_id, text=ERROR_SAVE_STEAM_PERCENT_THRESHOLD_MESSAGE)
        except ValueError:
            await bot.send_message(chat_id=user_id, text=ERROR_SAVE_STEAM_PERCENT_THRESHOLD_MESSAGE)

        msg = await bot.send_message(
            chat_id=user_id,
            text=CHANGE_SETTINGS_COMMAND_MESSAGE,
            reply_markup=change_settings_ikb()
        )

        data[LAST_IKB_REDIS_KEY] = msg.message_id

    await ChangeSettingsStatesGroup.change_settings.set()
