import re

from data.redis import STEAM_PROXY_ID_REDIS_KEY

from functions import httpx_response

from data.config import STEAM_HEADERS

from utils import steam_data_prepare

from aiogram.dispatcher.storage import FSMContext


async def steam_parser(
    steam_proxy: str,
    user_id: int,
    steam_market_url: str,
    steam_resample: int,
    state: FSMContext
) -> tuple:
    '''
    :param steam_proxy: steam_proxy.
    :param user_id: Телеграм user id.
    :param steam_market_url: Ссылка на предмет в steam market.
    :param steam_resample: Период за который мы ищем среднюю стоимость предмета на steam market.
    :param state: FSMContext.
    :return: Средняя цена предмета в steam market за указанный период (steam_resample), количество проданных предметов
        и возможно новый прокси. В случае ошибки - None.
    '''

    response, steam_proxy = await httpx_response(
        proxy=steam_proxy,
        proxy_id_redis_key=STEAM_PROXY_ID_REDIS_KEY,
        url=steam_market_url,
        headers=STEAM_HEADERS,
        cookies=None,
        user_id=user_id,
        state=state
    )
    if response is None:
        return None, None, steam_proxy

    try:
        m = re.search(r'var line1=(.+);', response.text)
        data_price, data_sell = steam_data_prepare(data=m.group(1), steam_resample=steam_resample)

        data_price_mean = round(sum(data_price) / len(data_price), 2)
        data_price_threshold = data_price_mean + (data_price_mean * 0.2)
        new_data_price = []

        for price in data_price:
            if price <= data_price_threshold:
                new_data_price.append(price)

        return round(sum(new_data_price) / len(new_data_price), 2), sum(data_sell), steam_proxy
    except AttributeError:
        return None, None, steam_proxy
