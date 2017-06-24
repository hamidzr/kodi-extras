from utils.voiceParser import *

COMMANDS = [
    {
        'aliases': ['please set', 'pls set', 'please','pls', 'go','set'],
        'script': 'python3.6 kodiCrud.py'
    },
    {
        'aliases': ['play music'],
        'script': 'python3.6 playYtPlaylist.py'
    },
    {
        'aliases': ['play'],
        'script': 'python3.6 playYtSearch.py 10'
    }
]

listen(COMMANDS);
