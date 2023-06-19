from loader import dp, bot

from data.config import PROXIES, PROXY_LOGIN, PROXY_PASSWORD

from data.callbacks import CHANGE_STEAM_PROXY_DATA

from data.redis import LAST_IKB_REDIS_KEY, STEAM_PROXY_ID_REDIS_KEY, STEAM_PROXY_REDIS_KEY

from data.messages import (
    CHANGE_STEAM_PROXY_MESSAGE,
    SUCCESSFULLY_SAVE_STEAM_PROXY_MESSAGE,
    ERROR_SAVE_STEAM_PROXY_MESSAGE,
    CHANGE_SETTINGS_COMMAND_MESSAGE
)

from keyboards import change_settings_ikb

from functions import keyboards_clear

from states import ChangeSettingsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CHANGE_STEAM_PROXY_DATA,
    state=ChangeSettingsStatesGroup.change_settings
)
async def change_steam_proxy(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    await keyboards_clear(user_id=user_id, state=state)
    async with state.proxy() as data:
        await bot.send_message(
            chat_id=user_id,
            text=CHANGE_STEAM_PROXY_MESSAGE.format(data[STEAM_PROXY_ID_REDIS_KEY], len(PROXIES))
        )

    await ChangeSettingsStatesGroup.change_steam_proxy.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=ChangeSettingsStatesGroup.change_steam_proxy)
async def enter_steam_proxy(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    async with state.proxy() as data:
        try:
            max_proxies = len(PROXIES) - 1
            new_proxy = int(message.text)
            if 0 <= new_proxy <= max_proxies:
                data[STEAM_PROXY_ID_REDIS_KEY] = new_proxy
                data[STEAM_PROXY_REDIS_KEY] = f'http://{PROXY_LOGIN}:{PROXY_PASSWORD}@{PROXIES[new_proxy]}'
                await bot.send_message(chat_id=user_id, text=SUCCESSFULLY_SAVE_STEAM_PROXY_MESSAGE)
            else:
                await bot.send_message(chat_id=user_id, text=ERROR_SAVE_STEAM_PROXY_MESSAGE.format(max_proxies))
        except ValueError:
            await bot.send_message(chat_id=user_id, text=ERROR_SAVE_STEAM_PROXY_MESSAGE.format(max_proxies))

        msg = await bot.send_message(
            chat_id=user_id,
            text=CHANGE_SETTINGS_COMMAND_MESSAGE,
            reply_markup=change_settings_ikb()
        )

        data[LAST_IKB_REDIS_KEY] = msg.message_id

    await ChangeSettingsStatesGroup.change_settings.set()
