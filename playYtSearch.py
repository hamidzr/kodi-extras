#!/usr/bin/python3

from utils.kodiBasics import *
from utils.youtube import *

itemCount = int(sys.argv[1]) # number of results to add for each search query

for query in sys.argv[2:]:
    # search youtube and create a list of urls
    searchResultsJson = ytSearch(query);
    urls = []
    for idx, res in enumerate(searchResultsJson['items']):
        id = res['id']['videoId']
        if idx < itemCount:
        	print(str(idx+1) + '. ' + res['snippet']['title'])
        	urls.append("plugin://plugin.video.youtube/?action=play_video&videoid={}".format(id))
        else:
        	break
    clearPlaylist()
    createPlaylist(urls)
setShuffle(False)
playPlaylist()
