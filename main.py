from urllib.parse import urljoin
import pdb

import requests

import mm


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


def track_search(title, artist):
    url = mm.generate_url('track_search')    
    payload = {'apikey': mm.api_key(), 'q_track': title, 'q_artist': artist, 'has_lyrics': 1}    
    return requests.get(url, params=payload).json()


def track_lyrics_get(track_id):
    url = mm.generate_url('track_lyrics_get')    
    payload = {'apikey': mm.api_key(), 'track_id': str(track_id)}
    return requests.get(url, params=payload).json()


# ---------------------------------


if __name__ == "__main__":

    tracks = [
        Song("crazy heart", "hank williams")
    ]

    for track in tracks:

        # get json response from MusiXmatch search for track
        response = track_search(track.title, track.artist)

        # pull out track_ids
        track_ids = []
        for each in response['message']['body']['track_list']:
            if each['track']['has_lyrics'] == 1:
                track_ids.append(each['track']['track_id'])


        # get lyrics
        # if len(track_ids) > 0:
        lyrics_all_versions = []
        for trk in track_ids: 
            response = track_lyrics_get(track_ids[0])  # just use the first

            lyrics_all_versions.append(response['message']['body']['lyrics']['lyrics_body'])

        for each in lyrics_all_versions:
            print (each)
            