from utils.voiceParser import *

COMMANDS = [
    {
        'aliases': ['please set', 'pls set', 'please','pls', 'go','set'],
        'script': 'env python3 kodiCrud.py',
        'hasArgs': True
    },
    {
        'aliases': ['music','play music'],
        'script': 'env python3 playYtPlaylist.py'
    },
    {
        'aliases': ['play playlist', 'search playlist'],
        'script': 'env python3 playYtSearchPlaylist.py',
        'hasArgs': True
    },


    {
        'aliases': ['play'],
        'script': 'env python3 playYtSearch.py 10',
        'hasArgs': True
    },
    {
        'aliases': ['next','skip'],
        'script': 'env python3 kodiCrud.py next'
    },
    {
        'aliases': ['pause'],
        'script': 'env python3 kodiCrud.py pause'
    }
]

listen(COMMANDS);
