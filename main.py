from urllib.parse import urljoin

import requests
# import json

import mm


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


def track_search(title, artist):
    url = mm.generate_url('track_search')    
    
    payload = {'apikey': mm.api_key(), 'q_track': title, 'q_artist': artist }
    
    return requests.get(url, params=payload).json()


# ---------------------------------


if __name__ == "__main__":

    tracks = [
        Song("crazy heart", "hank williams")
    ]

    for track in tracks:

        jdata = track_search(track.title, track.artist)

        print (jdata)
