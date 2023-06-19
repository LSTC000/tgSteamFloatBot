from typing import Union


def create_good_report(
    good_name: str,
    paint_wear: float,
    steam_market_mean_price: float,
    steam_market_count_sell: int,
    sell_min_price: float,
    buff_good_url: str,
    lowest_bargain_price: Union[float, None]
) -> str:
    '''
    :param good_name: Название предмета.
    :param paint_wear: Износ предмета.
    :param steam_market_mean_price: Средняя стоимость предмета в steam market.
    :param steam_market_count_sell: Количество продаж предмета в steam market.
    :param sell_min_price: Стоимость 1-го предмета для покупки.
    :param buff_good_url: Ссылка на предмет в Buff.
    :param lowest_bargain_price: Минимальная цена предмета для торга, если он возможен. Иначе - None.
    :return: Строка с информацией о товаре.
    '''

    clear_steam_market_mean_price = steam_market_mean_price * 0.87
    bargain = f'✅ ({lowest_bargain_price}Y - {sell_min_price}Y)' if lowest_bargain_price is not None else '❌'

    return f'Предмет: <a href="{buff_good_url}">{good_name}</a>\n' \
           f'Износ: {paint_wear: .8f}\n' \
           f'Цена покупки buff: {sell_min_price}Y\n' \
           f'Цена стим: {steam_market_mean_price: .2f}Y ({clear_steam_market_mean_price: .2f}Y)\n' \
           f'Профит ~ {((clear_steam_market_mean_price - sell_min_price) * 100) / sell_min_price: .2f}%\n' \
           f'Количество продаж: {steam_market_count_sell}\n' \
           f'Торговаться: {bargain}\n' \
