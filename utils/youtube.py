from .basics import *

YOUTUBE_API= os.environ['YOUTUBE_API']

# pre: gets a keyword
# post: returns the resutlts it's search (in yt)
def ytSearch(keyword,limit=10):
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={}&order=relevance&q={}&type=video&key={}".format(limit, keyword, YOUTUBE_API)
    return getJson(url)


def getYtPlaylist(playlistId, limit=25):
    print('getting playlist https://www.youtube.com/playlist?list={}'.format(playlistId))
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults={}&playlistId={}&key={}'.format(limit, playlistId, YOUTUBE_API)
    return getJson(url)

# search for videos in a specific channel
def ytSearchChannel(keyword, limit, channelId):
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&maxResults={}&order=relevance&q={}&safeSearch=strict&type=video&key={}".format(channelId, limit, keyword, YOUTUBE_API)
    return getJson(url)

def ytSearchPlaylists(keyword, limit=10):
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={}&order=relevance&q={}&type=playlist&key={}".format(limit, keyword, YOUTUBE_API)
    return getJson(url)['items']
