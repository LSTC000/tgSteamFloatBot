from asyncio import sleep

from data.redis import (
    PRICE_THRESHOLD_REDIS_KEY,
    BUFF_PERCENT_THRESHOLD_REDIS_KEY,
    STEAM_PERCENT_THRESHOLD_REDIS_KEY,
    STEAM_RESAMPLE_REDIS_KEY,
    START_PARSE_REDIS_KEY
)

from data.config import BUFF_SLEEP_TIME

from data.messages import START_PARSE_COMMAND_MESSAGE

from parsers import buff_parser, bargain_parser

from functions import keyboards_clear

from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start_parse'], state='*')
async def start_parse_command(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    await keyboards_clear(user_id=user_id, state=state)
    await bot.send_message(chat_id=user_id, text=START_PARSE_COMMAND_MESSAGE)

    async with state.proxy() as data:
        data[START_PARSE_REDIS_KEY] = True
        price_threshold = data[PRICE_THRESHOLD_REDIS_KEY]
        buff_percent_threshold = data[BUFF_PERCENT_THRESHOLD_REDIS_KEY]
        steam_percent_threshold = data[STEAM_PERCENT_THRESHOLD_REDIS_KEY]
        steam_resample = data[STEAM_RESAMPLE_REDIS_KEY]

    while True:
        stop = await buff_parser(
            user_id=user_id,
            price_threshold=price_threshold,
            buff_percent_threshold=buff_percent_threshold,
            steam_percent_threshold=steam_percent_threshold,
            steam_resample=steam_resample,
            state=state
        )

        if stop is not None:
            break

        await sleep(BUFF_SLEEP_TIME)
