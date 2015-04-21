import requests
from urllib.parse import urljoin
# import json

# ------- Musixmatch info ---------

root_url = 'http://api.musixmatch.com/ws/1.1/'
api_key = 'e0805332c879c42bc081dcd64f77f540'

# API methods
track_search_method = 'track.search'

# ---------------------------------

class Song:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist    
    def title(self):
        return self._title
    def artist(self):
        return self._artist


def track_search(track_title, artist_name):
    return track_search_method + '?' + 'apikey=' + api_key + '&' + 'q_track=' + track_title.replace(' ', '%20') + '&' + 'q_artist=' + artist_name.replace(' ', '%20') + '&' + 'has_lyrics=1'


# ---------------------------------

tracks = [
    Song("crazy heart", "hank williams")
]

for track in tracks:

    method_url = track_search(track.title(), track.artist())
    request_url = urljoin(root_url, method_url)

    print ("Sending HTTP request to: " + request_url)

    response_json = requests.get(request_url).json()

    print (response_json)
