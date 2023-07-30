# FediBot
```
    ───────────────       
 ┌──────┐ ┌────┐ ────     
 │┌┐┌┐┌┐│ │◕  ◕│ ──────   
 │└┘└┘└┘│ └─┬┬─┘ ┌────┐   
 │┌┐┌┐┌┐│ ┌┬┴┴┬┐ │┌┐┌┐│   
 │└┘└┘└┘│ ││FB││ │└┘└┘│   
 │┌┐  ┌┐│ ││──││ │┌┐┌┐│   
 │└┘┌┐└┘│ ■└┬┬┘■ │└┘└┘│   
─┴──┴┴──┴── ││ ──┴────┴───
  ───────── ││ ─────────  
    ────── ▀▀▀▀ ──────    
```
An easy way to program multiple FediBots for the Fediverse 🤖 The main goal of this project is to offer a simple way to create multiple bots for the Fediverse.

## Features
- Write posts / statuses.
- Include files (images) with statuses.
- Write multiple bots using the same base.
- Easy usage of ChatGPT.

## Intall
Needs the Python3 module "requests" to run.

`pip3 install requests`

or without pip:

`apt-get install python3-requests`

## Accesstoken
In order to use the bot you need an access-token.

To get the access-token the easiest way is to use this site: https://takahashim.github.io/mastodon-access-token/.

## Command
To run FediBot use following command

`python3 bot.py [-c CONFIG_FILE] [-p PLUGIN_NAME] [-u URL] [-k ACCESSTOKEN]`

You can put PLUGIN_NAME URL and ACCESSTOKEN in the CONFIG_FILE for easy command lining 😉 You can also just put one or two of them. For example place the URL and ACCESSTOKEN in the config file and enter the plugin manually.

## Todo
- Reply to comments.
