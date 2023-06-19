from typing import Union

from data.config import PROXIES

from utils import change_proxy

import httpx

from aiogram.dispatcher.storage import FSMContext


async def httpx_response(
    proxy: str,
    proxy_id_redis_key: str,
    url: str,
    headers: dict,
    cookies: Union[dict, None],
    user_id: int,
    state: FSMContext
) -> tuple:
    '''
    :param proxy: proxy.
    :param proxy_id_redis_key: proxy_id_redis_key.
    :param url: Url для запроса.
    :param headers: headers.
    :param cookies: cookies.
    :param user_id: Телеграм user id.
    :param state: FSMContext.
    :return: Ответ на запрос и прокси.
    '''

    new_proxy, none_flag = proxy, True

    for _ in range(len(PROXIES)):
        try:
            async with httpx.AsyncClient(proxies=new_proxy) as client:
                response = await client.get(
                    url=url,
                    headers=headers,
                    cookies=cookies,
                    params={'chat_id': user_id}
                )
            response.raise_for_status()
            none_flag = False
            break
        except (httpx.HTTPError, httpx.RequestError, httpx.TimeoutException):
            new_proxy = await change_proxy(state=state, proxy_id_redis_key=proxy_id_redis_key)

    return (None, proxy) if none_flag else (response, new_proxy)
