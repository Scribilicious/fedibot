import sys
import random
from libs.Crawler import Crawler
from libs.Sql import Sql

def init(self):
    self.Crawler = Crawler()

def run(self):
    self.Crawler.get('https://mossygiant.com/shop')
    image_urls = self.Crawler.findImages()

    if (not image_urls):
        return

    _Sql = Sql('mossygiant')
    _Sql.createTable('urls', 'url TEXT')

    for url in image_urls:
        if (not url.startswith("https://")):
            continue

        result = _Sql.execute('SELECT url FROM urls WHERE url = (?)', [url], True)

        if (not result):
            _Sql.execute('INSERT INTO urls VALUES (?)', [url])
            self.Post.init()
            self.Post.media(url, url)
            self.Post.status('https://mossygiant.com/shop')
            print(self.Post.send())