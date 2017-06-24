#!/usr/bin/python3

from utils.kodiBasics import *
from utils.youtube import *


clearPlaylist()

urls = []
try:
    searchResultsJson = getYtPlaylist(sys.argv[1])
except Exception as e:
    # default to trending musics
    searchResultsJson = getYtPlaylist('PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth')

for idx, res in enumerate(searchResultsJson['items']):
    id = res['contentDetails']['videoId']
    try:
        print(str(idx+1) + '. ' + res['snippet']['title'])
    except Exception as e:
        print('failed to print name')
    urls.append("plugin://plugin.video.youtube/?action=play_video&videoid={}".format(id))
createPlaylist(urls)
setShuffle(True)
playPlaylist()
