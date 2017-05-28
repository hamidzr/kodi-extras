from utils.voiceParser import *

COMMANDS = [
    {
        'aliases': ['please set', 'please','go','set'],
        'script': 'python3.6 kodiCrud.py'
    },
    {
        'aliases': ['play music'],
        'script': 'python3.6 playYtTrendingMusic.py'
    },
    {
        'aliases': ['play'],
        'script': 'python3.6 playYtSearch.py 10'
    }
]

listen(COMMANDS);
