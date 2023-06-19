import json

from currency_converter import CurrencyConverter


def steam_data_prepare(data: str, steam_resample: int) -> tuple:
    '''
    :param data: Строка с данными steam market.
    :param steam_resample: Период за который мы ищем среднюю стоимость предмета на steam market.
    :return: Список цен в йенах и количество проданных предметов.
    '''

    data = json.loads(data)

    price_counter, len_counter, steam_resample_counter, i = 1, 1, 0, len(data) - 2
    price_sum, sell_counter, prev_date = data[-1][1], int(data[-1][2]), ''.join(data[-1][0].split()[:3])
    price_list, sell_list = [], []

    while len_counter != len(data) and steam_resample_counter != steam_resample:
        now_date = ''.join(data[i][0].split()[:3])

        if prev_date == now_date:
            price_sum += data[i][1]
            sell_counter += int(data[i][2])
            price_counter += 1
        else:
            prev_date = now_date
            price_list.append(price_sum / price_counter)
            sell_list.append(sell_counter)
            price_sum, sell_counter = data[i][1], int(data[i][2])
            steam_resample_counter += 1
            price_counter = 1

        len_counter += 1
        i -= 1

    price_list.append(price_sum / price_counter)
    sell_list.append(sell_counter)

    c = CurrencyConverter()

    for i in range(len(price_list)):
        price_list[i] = round((c.convert(price_list[i], 'USD', 'CNY')), 2)

    return price_list, sell_list
