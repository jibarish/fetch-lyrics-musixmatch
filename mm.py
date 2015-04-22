from urllib.parse import urljoin

# ------- MusiXmatch API ---------

_root_url = 'http://api.musixmatch.com/ws/1.1/'

_api_key = 'e0805332c879c42bc081dcd64f77f540'

# API Methods
_methods = {
    'track_search' : 'track.search'    
}

# Public
def generate_url(method_name):
    return urljoin(_root_url, _methods[method_name])

def api_key():
    return _api_key