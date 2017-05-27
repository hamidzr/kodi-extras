import urllib.request
from urllib.parse import quote
import json
import os



# pre: gets an encoded url pointing to a json endpoint
# post: returns a python dic representing the response
def getJson(url):
    print('Calling url: ',url)
    httpResponse = urllib.request.urlopen(url)
    return json.loads(httpResponse.read().decode("utf-8"))
