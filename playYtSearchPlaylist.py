#!/usr/bin/env python3

from utils.kodiBasics import *
from utils.youtube import *

# search youtube and create a list of urls
searchResultsJson = ytSearchPlaylists(sys.argv[1]);

# queue the first playlist that comesup
for idx, res in enumerate(searchResultsJson):
    id = res['id']['playlistId']
    print(str(idx+1) + '. ' + res['snippet']['title'])
    runCommand('env python3 playYtPlaylist.py',"{}".format(id))
    break
