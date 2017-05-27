import sys
from .basics import *
# init
# TODO provide an option of using config files
KODI_ADDRESS = os.getenv('KODI_ENDPOINT_ADDRESS','http://localhost:8080')



# send a request object to kodi
def requestKodi(kodiReqJson):
    kodiReqJson['jsonrpc'] = '2.0'
    kodiReqJson['id'] = 1
    req = urllib.request.Request(url='{}/jsonrpc'.format(KODI_ADDRESS), method='POST')
    req.add_header('Content-Type','application/json')
    req.data = json.dumps(kodiReqJson).encode('UTF-8')
    res = urllib.request.urlopen(req, timeout=30).read().decode('UTF-8')
    res = json.loads(res)
    return res


# pre: a kodi friendly uri (plugin or internet)
def playOnKodi(uri):
    return requestKodi({"jsonrpc":"2.0","id":"1","method":"Player.Open","params":{"item":{"file":uri}}})
    requestKodi({"method":"GUI.SetFullscreen","params":{"fullscreen":True}})

def clearPlaylist(id=1):
    requestKodi({"method":"Player.Stop","params":{"playerid":1}})
    return requestKodi({"method":"Playlist.Clear","params":{"playlistid":1}})

# queues up a list of urls
def createPlaylist(urls):
    filesArr = []
    for url in urls:
        filesArr.append({"file": url})
    return requestKodi({"method":"Playlist.Add","params":{"playlistid":1, "item":filesArr}})

def playPlaylist(id=1):
    # play the playlist
    requestKodi({"method":"Player.Open","params":{"item":{"playlistid":1},"options":{"repeat":"all"}}})
    requestKodi({"method":"GUI.SetFullscreen","params":{"fullscreen":True}})

def setShuffle(shuffle):
    # shuffle the playlist
    return requestKodi({"method":"Player.SetShuffle", "params":{"playerid":1,"shuffle":shuffle}})
