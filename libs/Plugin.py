import sys
import importlib
from libs.Post import Post

class Plugin:
    def __init__(self, plugin, url, key, Config = None):
        self.Post = Post(url, key)
        self.Config = Config

        try:
            self.Plugin = importlib.import_module('libs.plugins.' + plugin)

        except Exception as e:
            print('Plugin:', plugin, 'does not exists.')
            print(e)
            sys.exit()

        try:
            self.Plugin.init(self)

        except Exception as e:
            print('Can not initialize plugin', plugin)
            print(e)
            sys.exit()

        try:
            self.Plugin.run(self)

        except Exception as e:
            print('Can not run plugin', plugin)
            print(e)
            sys.exit()
