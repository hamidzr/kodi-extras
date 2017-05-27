#!/usr/bin/python3

from utils.kodiBasics import *
from utils.youtube import *

# configs
PLAYBACK_DURATION = 20
TED_CATEGORY_ID = 9 # get from https://www.ted.com/surpriseme
TED_CHANNEL = 'UCAuUUnT6oDeKwE6v1NGQxug'


tedSurprisesJson = getJson('https://www.ted.com/surpriseme.json?minutes={}&rating_word_id={}'.format(PLAYBACK_DURATION,TED_CATEGORY_ID))
for surprise in tedSurprisesJson['talks']:
    luckyVideoJson = ytSearchChannel(surprise['title'], 1, TED_CHANNEL)
    ytId = luckyVideoJson['items'][0]['id']['videoId']
    playOnKodi('plugin://plugin.video.youtube/?action=play_video&videoid={}'.format(ytId))
    break
