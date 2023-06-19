from loader import dp

from data.callbacks import CLOSE_CHANGE_SETTINGS_DATA

from functions import keyboards_clear

from states import ChangeSettingsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CLOSE_CHANGE_SETTINGS_DATA,
    state=ChangeSettingsStatesGroup.change_settings
)
async def close_change_settings(callback: types.CallbackQuery, state: FSMContext) -> None:
    await keyboards_clear(user_id=callback.from_user.id, state=state)
