import os

from fake_useragent import UserAgent
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ua = UserAgent()


STEAM_HEADERS = {
    'User-Agent': ua.random
}
BUFF_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://buff.163.com/market/csgo',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Opera";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
BUFF_COOKIES = {
    'Device-Id': '6RCJfWbDswkX3D6LMc1D',
    'Locale-Supported': 'ru',
    'game': 'csgo',
    'NTES_YD_SESS': '42YkwPVPvCpOIl.ugo7X37ijVpr6nCMHvf4iTxJjHHYSiDSy9tWxvT3utoJzMIl25WiRUX0tzYZIwcszJ05C2nKTIx12QCKnc'
                    'ZXZlxT9iDUql1wfY6NbGqewx_BqYvCYJFEWCwIJcPNuibrcJkpJCtJZfVldbflKbRkbjnWOZppW1VwvkUPSedzU__vR1GLJ1I'
                    'I8xagHU_iODzMktFPr4ELDFaEbZQZSik7OFwXG2N1eG',
    'S_INFO': '1687113143|0|0&60##|7-9132170674',
    'P_INFO': '7-9132170674|1687113143|1|netease_buff|00&99|RO&1683187528&netease_buff#RU&null#10#0#0|&0|null|7-9132170674',
    'session': '1-lDYKbyzjvDGiz8hTZKTYbSLjoX0Kb_9rgl7MTFnl2fS42030364611',
    'csrf_token': 'IjZjNjkzYmI2NjVkZjRlYTIzMWZmNjFiODBmMzExZjA0M2Q5MjdmMjUi.F3F_jw.RncsDk0PXTDnnijQC99AwSYv5l8'
}

PROXIES = os.getenv('PROXIES').split(',')
PROXY_LOGIN = os.getenv('PROXY_LOGIN')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')

BUFF_SLEEP_TIME = 3
STEAM_SLEEP_TIME = 0.1
