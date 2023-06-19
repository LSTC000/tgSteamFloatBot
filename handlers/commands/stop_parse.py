from data.redis import START_PARSE_REDIS_KEY

from data.messages import STOP_PARSE_COMMAND_MESSAGE, ALREADY_STOP_PARSE_COMMAND_MESSAGE

from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['stop_parse'], state='*')
async def stop_parse_command(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        start = data[START_PARSE_REDIS_KEY]

        if start:
            data[START_PARSE_REDIS_KEY] = False
            await bot.send_message(chat_id=message.from_user.id, text=STOP_PARSE_COMMAND_MESSAGE)
        else:
            await bot.send_message(chat_id=message.from_user.id, text=ALREADY_STOP_PARSE_COMMAND_MESSAGE)
