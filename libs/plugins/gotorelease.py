import requests
import random
from libs.Sql import Sql

def init(self):
    self.Sql = Sql('gotorelease')
    self.Sql.createTable('version', 'version TEXT')

def run(self):
    version = self.Plugin.getversion(self)
    result = self.Sql.execute('SELECT version FROM version WHERE version = (?)', [version['version']], True)

    if (result):
        return

    self.Sql.execute('INSERT INTO version VALUES (?)', [version['version']])

    bleeps = ['Bleep' for _ in range(random.randint(1, 3))]

    self.Post.status(
        ', '.join(bleeps) + '... ' +
        'There is a new version of GoToSocial! The new version is ' +
        version['version'] +
        ' and it\'s called:\n\n' +
        version['name'] +
        '\n\n' +
        version['url'] +
        '\n\n#GoToSocial #Release')
    print(self.Post.send())


def getversion(self):
    res = requests.get("https://api.github.com/repos/superseriousbusiness/gotosocial/releases/latest").json()
    return {'name': res['name'], 'version': res['tag_name'], 'date': res['published_at'], 'url': res['html_url']}
