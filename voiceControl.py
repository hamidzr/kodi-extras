from utils.voiceParser import *

COMMANDS = [
    {
        'aliases': ['please set', 'pls set', 'please','pls', 'go','set'],
        'script': 'python3.6 kodiCrud.py',
        'hasArgs': True
    },
    {
        'aliases': ['music','play music'],
        'script': 'python3.6 playYtPlaylist.py'
    },
    {
        'aliases': ['next','skip'],
        'script': 'python3.6 kodiCrud.py next'
    },
    {
        'aliases': ['pause'],
        'script': 'python3.6 kodiCrud.py pause'
    },
    {
        'aliases': ['play'],
        'script': 'python3.6 playYtSearch.py 10',
        'hasArgs': True
    }
]

listen(COMMANDS);
