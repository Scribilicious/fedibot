import sys
import random
from libs.Crawler import Crawler
from libs.Sql import Sql
from typing import Union

crawler_urls = [
    {'name': 'Synplant', 'url': 'https://soniccharge.com/synplant', 'regex': '"price": "(.*?)"'},
    {'name': 'Auto-Tune', 'url': 'https://www.reasonstudios.com/shop/rack-extension/auto-tune-reason/', 'regex': '(\$|€)([0-9.,]+)', 'group': 1, 'subgroup': 0},
    {'name': 'Industrializer', 'url': 'https://www.reasonstudios.com/shop/rack-extension/industrializer/', 'regex': '(\$|€)([0-9.,]+)', 'group': 1, 'subgroup': 0},
    {'name': 'Flipper Zero', 'url': 'https://shop.flipperzero.one/', 'regex': '"price" :(.*?),'},
    {'name': 'Starfield', 'url': 'https://store.steampowered.com/app/1716740/Starfield/', 'regex': 'data-price-final="([0-9.,]+)"', 'force_decimal': True},
]

def init(self):
    self.Crawler = Crawler()

def run(self):
    for crawl in crawler_urls:
        try:
            group = crawl['group']
        except:
            group = 0

        try:
            subgroup = crawl['subgroup']
        except:
            subgroup = None

        try:
            force_decimal = crawl['force_decimal']
        except:
            force_decimal = False

        self.Plugin.getPrice(self, crawl['name'], crawl['url'], crawl['regex'], group, subgroup, force_decimal)

    return

def getPrice(self, name: str, url: str, regex: str, group: int = 0, subgroup: Union[int, None] = None, force_decimal: bool = False):
    self.Crawler.get(url)
    price = self.Crawler.find(regex)

    if subgroup is not None:
        try:
            price = price[subgroup]
        except:
            print('No price found for "{}".'.format(name))
            return None

    if isinstance(group, int):
        try:
            price = price[group]
            price = float(price.replace(',', '.'))
        except:
            print(self.Crawler.getResponse())
            print('No price found for "{}".'.format(name))
            return None
    else:
        print('Group value for "{}" is not an integer.'.format(name))
        return None

    if force_decimal:
        price = price / 100

    try:
        formatted_price = '{:.2f}'.format(price)
    except:
        print('Can not format "{}".'.format(name))
        return None

    _Sql = Sql('pricewatch')
    key = _Sql.generateKey(name, '')
    _Sql.createTable(key, 'id INTEGER PRIMARY KEY AUTOINCREMENT, price REAL')
    result = _Sql.execute('SELECT price FROM {} ORDER BY id DESC LIMIT 1'.format(key), [], True)

    if (not result):
        _Sql.execute('INSERT INTO {} (price) VALUES (?)'.format(key), [price])
        self.Post.init()
        bleeps = ['Bleep' for _ in range(random.randint(1, 3))]
        self.Post.status('{}... There is a new price for "{}".\nThe new price is "{}".\n\nLink: {}\n\n#pricewatch #{}'.format(', '.join(bleeps), name, formatted_price, url, key))
        print(self.Post.send())