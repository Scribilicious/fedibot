import sys
import importlib
import traceback
from libs.Post import Post

class Plugin:
    def __init__(self, plugin, url, key, Config = None, debug = False):
        self.Post = Post(url, key)
        self.Config = Config

        try:
            self.Plugin = importlib.import_module('libs.plugins.' + plugin)

        except Exception as e:
            print('Plugin:', plugin, 'does not exists.')
            traceback.print_exc()
            sys.exit()

        try:
            self.Plugin.init(self)

        except Exception as e:
            print('Can not initialize plugin', plugin)
            traceback.print_exc()
            sys.exit()

        # runs the plugin
        if debug:
            self.Plugin.run(self)
        else:
            try:
                self.Plugin.run(self)

            except Exception as e:
                print('Can not run plugin', plugin)

                traceback.print_exc()
                sys.exit()
