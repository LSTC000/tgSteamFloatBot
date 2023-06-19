from data.config import PROXIES, PROXY_LOGIN, PROXY_PASSWORD

from data.redis import BUFF_PROXY_ID_REDIS_KEY, BUFF_PROXY_REDIS_KEY, STEAM_PROXY_REDIS_KEY

from aiogram.dispatcher.storage import FSMContext


async def change_proxy(state: FSMContext, proxy_id_redis_key: str) -> str:
    '''
    :param state: FSMContext.
    :param proxy_id_redis_key: proxy_redis_key.
    :return: Новый прокси.
    '''

    async with state.proxy() as data:
        if data[proxy_id_redis_key] == len(PROXIES) - 1:
            data[proxy_id_redis_key] = 0
        else:
            data[proxy_id_redis_key] += 1

        new_proxy = f'http://{PROXY_LOGIN}:{PROXY_PASSWORD}@{PROXIES[data[proxy_id_redis_key]]}'

        if proxy_id_redis_key == BUFF_PROXY_ID_REDIS_KEY:
            data[BUFF_PROXY_REDIS_KEY] = new_proxy
        else:
            data[STEAM_PROXY_REDIS_KEY] = new_proxy

    return new_proxy
