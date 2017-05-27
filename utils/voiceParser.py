#!/usr/bin/python3.6

# description: this script takes a commands map defined below listens for aliases utilizing google assistant sdk
# and runs the corresponding script with given arguments*
# argument is what is left of the recognized sentence after alias is removed

import time
import re
import subprocess
import os

# init
LOG_LOCATION='googleAssistant.log'
GOOGLE_ASSISTANT_LOCATION= os.getenv('GOOGLE_ASSISTANT_LOCATION', '/home/pi/env/bin/google-assistant-demo' )

COMMANDS = [
    {
        'aliases': ['please set', 'please','go','set'],
        'script': 'python3.6 kodiCrud.py'
    },
    {
        'aliases': ['play music'],
        'script': 'python3.6 playMusicTrends.py'
    },
    {
        'aliases': ['play'],
        'script': 'python3.6 playYtSearch.py 5'
    }

]


def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# alias is the phrase to listen for
# script: script location and running with predefined args if any
def matchCommands(sentence, aliases, script):
    # if regexes are defined here they are compiled on every call
    for alias in aliases:
        print('checking for alias',alias)
        cmdRe = re.compile("{} ?(.*)".format(alias)) # TODO make this case insensitive r""i
        try:
            args = cmdRe.search(sentence).group(1)
            print('running', alias, 'detected with args',args)
            runCommand(script, args)
            return True
        except Exception:
            print('.',end='')
    return False


def runCommand(script, args):
    fullCmd = script + ' "' + args + '"'
    print('calling', fullCmd)
    subprocess.run(fullCmd,shell=True)

# commands map to run any arbitray script with dynamic with voice entered arguments
# sort aliases by most restrictive first.
def listen(commandsMap):
    out = subprocess.run(["pgrep", "google-ass"], stdout=subprocess.PIPE).stdout
    if len(out) == 0:
        subprocess.run(GOOGLE_ASSISTANT_LOCATION+' &', shell=True)
        out = subprocess.run(["pgrep", "google-ass"], stdout=subprocess.PIPE).stdout
    pid = re.compile(r"\d+").search(str(out)).group()
    cmd = "/usr/bin/strace -p{} -s9999 -o {} &".format(pid,LOG_LOCATION)
    print(cmd)
    print('run the above command manually for now')
    subprocess.Popen(cmd,shell=True)
    logfile = open(LOG_LOCATION,"r")
    print('opened',LOG_LOCATION)
    time.sleep(1)
    loglines = follow(logfile)
    # regex to get the sentence detected by googleAss
    speech = re.compile(r"\: ('|\\\")(.*)('|\\\")\}")
    for line in loglines:
        try:
            sentence = speech.search(line).group(2)
            print('user said:',sentence)
            for entry in commandsMap:
                # if a cmd is detected don't check for other commands
                if matchCommands(sentence, entry['aliases'], entry['script']):
                    break
        except Exception:
            print('.',end='')
