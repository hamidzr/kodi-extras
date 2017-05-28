#!/usr/bin/python3

# description: simple playback actions for kodi

from utils.kodiBasics import *


def setVolume(volume):
    print('setting volume to', volume)
    return requestKodi({"method":"Application.SetVolume","params":{"volume":volume}})

def changeVolumeBy(change):
    currentVolume = int(getProperty('volume'))
    return setVolume(currentVolume + change)


action = sys.argv[1].lower()
actionMap = {
    'play': [requestKodi, {"method":"Player.PlayPause","params":{"playerid":1}}],
    'resume': [requestKodi, {"method":"Player.PlayPause","params":{"playerid":1}}],
    'pause': [requestKodi, {"method":"Player.PlayPause","params":{"playerid":1}}],
    'stop': [requestKodi, {"method":"Player.Stop","params":{"playerid":1}}],
    'next': [requestKodi, {"method":"Player.GoTo","params":{"playerid":1,"to":"next"}}],
    'previous': [requestKodi, {"method":"Player.GoTo","params":{"playerid":1,"to":"previous"}}],
    'volume low': [setVolume, 40],
    'volume medium': [setVolume, 70],
    'volume high': [setVolume, 90],
    'volume max': [setVolume, 10],
    'volume 9': [setVolume, 90],
    'volume 8': [setVolume, 80],
    'volume 7': [setVolume, 70],
    'volume 6': [setVolume, 60],
    'volume 5': [setVolume, 50],
    'volume nine': [setVolume, 90],
    'volume eight': [setVolume, 80],
    'volume seven': [setVolume, 70],
    'volume six': [setVolume, 60],
    'volume five': [setVolume, 50],
    'volume up': [changeVolumeBy, +10],
    'volume down': [changeVolumeBy, -10]
}

# run pass the selected option
actionTuple = actionMap[action]
print(actionTuple)
print(actionTuple[0](actionTuple[1]))

# make sure it is playing on full screen
if action in ['play','resume','next']:
    requestKodi({"method":"GUI.SetFullscreen","params":{"fullscreen":True}})
