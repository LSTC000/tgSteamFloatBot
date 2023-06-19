from data.redis import LAST_IKB_REDIS_KEY, START_PARSE_REDIS_KEY

from data.messages import CHANGE_SETTINGS_COMMAND_MESSAGE, NEED_STOP_PARSE_MESSAGE

from states import ChangeSettingsStatesGroup

from functions import keyboards_clear

from keyboards import change_settings_ikb

from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['change_settings'], state='*')
async def change_settings_command(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    await keyboards_clear(user_id=user_id, state=state)

    async with state.proxy() as data:
        start = data[START_PARSE_REDIS_KEY]

    if start:
        await bot.send_message(chat_id=user_id, text=NEED_STOP_PARSE_MESSAGE)
    else:
        msg = await bot.send_message(
            chat_id=user_id,
            text=CHANGE_SETTINGS_COMMAND_MESSAGE,
            reply_markup=change_settings_ikb()
        )

        async with state.proxy() as data:
            data[LAST_IKB_REDIS_KEY] = msg.message_id

        await ChangeSettingsStatesGroup.change_settings.set()
