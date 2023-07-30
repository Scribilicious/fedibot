import sys
import os
import argparse
import configparser

from libs.Plugin import Plugin

Parser = argparse.ArgumentParser()
plugin = None
url = None
key = None

Parser.add_argument('-p', '--plugin', type=str, help='The plugin to run.')
Parser.add_argument('-u', '--url', type=str, help='The URL of the Fediverse instance.')
Parser.add_argument('-k', '--key', type=str, help='The key used for the Fediverse instance.')
Parser.add_argument('-c', '--config', type=str, help='Use a config file.')
Parser.add_argument('-f', '--free', action='store_true', help='Free temp files.')
Parser.add_argument('-n', '--new', type=str, help='Create a new config file. If the -c parameter is set then use that file as a copy.')

Args = Parser.parse_args()

print('    ───────────────')
print(' ┌──────┐ ┌────┐ ────')
print(' │┌┐┌┐┌┐│ │◕  ◕│ ──────')
print(' │└┘└┘└┘│ └─┬┬─┘ ┌────┐')
print(' │┌┐┌┐┌┐│ ┌┬┴┴┬┐ │┌┐┌┐│')
print(' │└┘└┘└┘│ ││FB││ │└┘└┘│')
print(' │┌┐  ┌┐│ ││──││ │┌┐┌┐│')
print(' │└┘┌┐└┘│ ■└┬┬┘■ │└┘└┘│')
print('─┴──┴┴──┴── ││ ──┴────┴───')
print('  ───────── ││ ─────────')
print('    ────── ▀▀▀▀ ──────')

if (Args.config):
    Config = configparser.ConfigParser()
    try:
        Config.read(os.path.dirname(__file__) + '/config/' + Args.config + '.ini')

    except:
        print('No config file', Args.config, 'found...')
        sys.exit()

    try:
        plugin = Config['SETTINGS']['plugin']

    except:
        pass

    try:
        url = Config['SETTINGS']['url']

    except:
        pass

    try:
        key = Config['SETTINGS']['key']

    except:
        pass

if (Args.new):
    path = os.path.dirname(__file__) + '/config/'
    try:
        if (Args.config):
            os.system('cp ' + path + Args.config + '.ini ' + path + Args.new + '.ini')

        else:
            with open(path + Args.new + '.ini', 'w') as f:
                f.write('[SETTINGS]')

        print('Created new ini file', Args.new, '...')

    except:
        print('Can not create a new ini file', Args.new, '...')

    sys.exit()

if (Args.plugin):
    plugin = Args.plugin

if (Args.url):
    url = Args.url

if (Args.key):
    key = Args.key

if (Args.free):
    folder_path = os.path.dirname(__file__) + '/data/temp/'
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        print('Removing', file_path)
        os.remove(file_path)

    print('done...')
    sys.exit()

if (plugin and url and key):
    print('Plugin:', plugin)
    print('URL:', url)
    print('Key:', key)
    print()
    Plugin(plugin, url, key, Config)

else:
    Parser.print_help()
