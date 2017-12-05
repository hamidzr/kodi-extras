# Voice Control for Kodi and beyond

## Installation
Before getting started with this repo you first need to have a working Kodi installation on you local area network.
I have only tested running this repo on a separate raspberry pi as the one running Kodi but if you can get the mic and audio out configure properly on your raspberry pi OS (eg OSMC) there is no real limitation to have both in one device.

### Install Google Assistant Demo
for current version of voice control to work, you need to:
1. compile python 3.6 from source for raspberry pi
```python
sudo apt update
sudo apt install build-essential -y
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
tar xzvf Python-3.6.1.tgz
cd Python-3.6.1/
./configure
make
sudo make install
```
* takes about 15 minutes on RaspberryPi3

2. have google-assistant-demo installed
https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/

if you want to set audio out to analog: (aux out) `amixer cset numid=3 1`

3. now you should have google assistant setup and running. 
startup your assistant and talk to it. You should see your voice converted into text (from the logs on the raspberry pi). If you attached a speaker you should also be able to hear back answers to yours queries. This step should be fully functional before you can move to the next.

### Install Kodi Extras

- clone the repo to a direcotry: `git clone https://github.com/hamidzr/kodi-extras.git` 
- setup the environment variables. 


### Environment Variables
- YOUTUBE_API: google *how to get youtube api*
- GOOGLE_ASSISTANT_LOCATION ( for the voice control to work )
- KODI_ENDPOINT_ADDRESS eg. http://192.x.y.z:8080
- KODI_USERNAME:if you have https password setup on your kodi you have to set your credentials using this and the next env variable
- KODI_PASSWORD: 

## Running the voice controller
If everything is setup succesfully, from the kodi-extra directory, running `python voiceControl.py` should startup the the program. Now talk to your assistant and ask it to play any video from youtube and also control your media playback.
