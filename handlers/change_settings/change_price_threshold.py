from loader import dp, bot

from data.callbacks import CHANGE_PRICE_THRESHOLD_DATA

from data.redis import LAST_IKB_REDIS_KEY, PRICE_THRESHOLD_REDIS_KEY

from data.messages import (
    CHANGE_PRICE_THRESHOLD_MESSAGE,
    SUCCESSFULLY_SAVE_PRICE_THRESHOLD_MESSAGE,
    ERROR_SAVE_PRICE_THRESHOLD_MESSAGE,
    CHANGE_SETTINGS_COMMAND_MESSAGE
)

from keyboards import change_settings_ikb

from functions import keyboards_clear

from states import ChangeSettingsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CHANGE_PRICE_THRESHOLD_DATA,
    state=ChangeSettingsStatesGroup.change_settings
)
async def change_price_threshold(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    await keyboards_clear(user_id=user_id, state=state)
    await bot.send_message(chat_id=user_id, text=CHANGE_PRICE_THRESHOLD_MESSAGE)

    await ChangeSettingsStatesGroup.change_price_threshold.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=ChangeSettingsStatesGroup.change_price_threshold)
async def enter_price_threshold(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    async with state.proxy() as data:
        try:
            price_threshold = float(message.text)
            if price_threshold >= 0:
                data[PRICE_THRESHOLD_REDIS_KEY] = price_threshold
                await bot.send_message(chat_id=user_id, text=SUCCESSFULLY_SAVE_PRICE_THRESHOLD_MESSAGE)
            else:
                await bot.send_message(chat_id=user_id, text=ERROR_SAVE_PRICE_THRESHOLD_MESSAGE)
        except ValueError:
            await bot.send_message(chat_id=user_id, text=ERROR_SAVE_PRICE_THRESHOLD_MESSAGE)

        msg = await bot.send_message(
            chat_id=user_id,
            text=CHANGE_SETTINGS_COMMAND_MESSAGE,
            reply_markup=change_settings_ikb()
        )

        data[LAST_IKB_REDIS_KEY] = msg.message_id

    await ChangeSettingsStatesGroup.change_settings.set()
