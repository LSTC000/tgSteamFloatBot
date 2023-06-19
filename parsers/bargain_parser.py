from typing import Union


async def bargain_parser(user_id: int, item: dict) -> Union[float, None]:
    '''
    :param user_id: Телеграм user id.
    :param item: Словарь с данными о предмете.
    :return: Минимальная цена предмета для торга, если он возможен. Иначе - None.
    '''

    try:
        item_info = item.get('asset_info').get('info')

        if 'inspect_state' in item_info.keys():
            return float(item.get('lowest_bargain_price'))
        else:
            return None
    except (AttributeError, KeyError):
        return None
