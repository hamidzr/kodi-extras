from .basics import *

YOUTUBE_API= os.environ['YOUTUBE_API']

# pre: gets a keyword
# post: returns the resutlts it's search (in yt)
def ytSearch(keyword,results=10):
    keyword = quote(keyword)
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={}&order=relevance&q={}&type=video&key={}".format(results, keyword, YOUTUBE_API)
    return getJson(url)


def getYtPlaylist(id='PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth'):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults=25&playlistId={}&key={}'.format(id, YOUTUBE_API)
    return getJson(url)


def ytSearchChannel(keyword, results, channelId):
    keyword = quote(keyword)
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&maxResults={}&order=relevance&q={}&safeSearch=strict&type=video&key={}".format(channelId, results, keyword, YOUTUBE_API)
    return getJson(url)
