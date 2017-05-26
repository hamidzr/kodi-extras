from utils.voiceParser import *

COMMANDS = [
    {
        'aliases': ['please set', 'please','go','set'],
        'script': 'python3.6 kodiCrud.py'
    },
    {
        'aliases': ['play music'],
        'script': 'python3.6 playMusicTrends.py'
    },
    {
        'aliases': ['play'],
        'script': 'python3.6 playYtSearch.py 5'
    }
]

listen(COMMANDS);
