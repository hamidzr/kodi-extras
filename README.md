set environment variables:
- YOUTUBE_API
- GOOGLE_ASSISTANT_LOCATION ( for the voice control to work )
- KODI_ENDPOINT_ADDRESS eg. http://192.x.y.z:8080


for current version of voice control to work, you need to:
1. compile python 3.6 from source for raspberry pi
```python
sudo apt update
sudo apt install build-essential
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
