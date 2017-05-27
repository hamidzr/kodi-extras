#!/usr/bin/python3

# description: simple playback actions for kodi

from utils.kodiBasics import *
# import urllib.request
# from urllib.parse import quote
# import json
# import sys


action = sys.argv[1].lower()
actionMap = {
    'play': {"method":"Player.PlayPause","params":{"playerid":1}},
    'resume': {"method":"Player.PlayPause","params":{"playerid":1}},
    'pause': {"method":"Player.PlayPause","params":{"playerid":1}},
    'stop': {"method":"Player.Stop","params":{"playerid":1}},
    'next': {"method":"Player.GoTo","params":{"playerid":1,"to":"next"}},
    'previous': {"method":"Player.GoTo","params":{"playerid":1,"to":"previous"}},
    'volume low': {"method":"Application.SetVolume","params":{"volume":40}},
    'volume medium': {"method":"Application.SetVolume","params":{"volume":70}},
    'volume high': {"method":"Application.SetVolume","params":{"volume":90}},
    'volume max': {"method":"Application.SetVolume","params":{"volume":100}},
    'volume 9': {"method":"Application.SetVolume","params":{"volume":90}},
    'volume 8': {"method":"Application.SetVolume","params":{"volume":80}},
    'volume 7': {"method":"Application.SetVolume","params":{"volume":70}},
    'volume 6': {"method":"Application.SetVolume","params":{"volume":60}},
    'volume 5': {"method":"Application.SetVolume","params":{"volume":50}},
    'volume nine': {"method":"Application.SetVolume","params":{"volume":90}},
    'volume eight': {"method":"Application.SetVolume","params":{"volume":80}},
    'volume seven': {"method":"Application.SetVolume","params":{"volume":70}},
    'volume six': {"method":"Application.SetVolume","params":{"volume":60}},
    'volume five': {"method":"Application.SetVolume","params":{"volume":50}},
}

# run pass the selected option
print(requestKodi(actionMap[action]))

if action in ['play','resume','next']:
    requestKodi({"method":"GUI.SetFullscreen","params":{"fullscreen":True}})
