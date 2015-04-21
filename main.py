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
    """A struct for song."""
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist    
    def title(self):
        return self._title
    def artist(self):
        return self._artist


def track_search(title, artist):
    url = urljoin(root_url, track_search_method)
    payload = {'apikey': api_key, 'q_track': title, 'q_artist': artist }

    return requests.get(url, params=payload).json()


# ---------------------------------

tracks = [
    Song("crazy heart", "hank williams")
]

for track in tracks:

    jdata = track_search(track.title(), track.artist())

    print (jdata)
