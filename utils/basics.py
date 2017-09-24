import urllib.request
from urllib.parse import quote
import json
import os
import subprocess


# pre: gets an encoded url pointing to a json endpoint
# post: returns a python dic representing the response
def getJson(url):
    print('Calling url: ',url)
    httpResponse = urllib.request.urlopen(url)
    return json.loads(httpResponse.read().decode("utf-8"))


def runCommand(script, args):
    fullCmd = script + ' "' + args + '"' if args else script
    print('executing', fullCmd)
    # TODO make the script execution non-blocking
    subprocess.run(fullCmd,shell=True)
    # pid = subprocess.Popen([sys.executable, fullCmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

