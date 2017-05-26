#!/usr/bin/python3

from utils.kodiBasics import *
from utils.youtube import *
# import urllib.request
# from urllib.parse import quote
# from utils.basics import *
# import json
# import sys


clearPlaylist()

urls = []
try:
    searchResultsJson = getYtPlaylist(sys.argv[1])
except Exception as e:
	pass
searchResultsJson = getYtPlaylist()
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
