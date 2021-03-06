import sys, base64
from .basics import *
# init
# TODO provide an option of using config files
KODI_ADDRESS = os.getenv('KODI_ENDPOINT_ADDRESS','http://localhost:8080')
USERNAME = os.getenv('KODI_USERNAME');
PASSWORD = os.getenv('KODI_PASSWORD');


# send a request object to kodi
def requestKodi(kodiReqJson):
    kodiReqJson['jsonrpc'] = '2.0'
    kodiReqJson['id'] = 1
    headers = {'Content-Type': 'application/json'}
    if (PASSWORD != None):
        # add authentication headers
        authByte = bytes('{0}:{1}'.format(USERNAME, PASSWORD), 'utf-8')
        base64string = base64.b64encode(authByte).decode('utf-8')
        headers['Authorization'] = f'Basic {base64string}'
    reqData = json.dumps(kodiReqJson).encode('UTF-8')
    print(f'sending request {kodiReqJson}')
    res = requests.post('{}/jsonrpc'.format(KODI_ADDRESS), data=reqData, headers=headers, timeout=30)
    # res = urllib.request.urlopen(req, timeout=30).read().decode('UTF-8')
    return res.json()


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

def getProperty(name):
    return requestKodi({"method":"Application.GetProperties","params":{"properties":[name]}})['result'][name]
