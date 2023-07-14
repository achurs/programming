#get user token from spotify api
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

#use the client id and secret locally
scope = 'user-library-read'
username = '31yscjus7mxo2ur2toutdepn54dm'
client_id = '9aec64d471bb477c881997739b2565e2'
client_secret = 'b9c33f9b5b014d109b3f85faf6489ffc'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,redirect_uri='http://localhost:8888/callback', scope=scope))


limit = 50
offset = 0
names = []
urls = []
while True:
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    for item in results['items']:
        names.append([item['track']['name']])
        urls.append(item['track']['external_urls']['spotify'])
    offset += limit
    if len(results['items']) < limit:
        break

not_downloaded_names = []
not_downloaded_urls = []
for i in range(len(names)):
    print(names[i])
    try:
        os.system('python -m spotdl ' + urls[i])
    except:
        print("error")
        not_downloaded_names.append(names[i])
        not_downloaded_urls.append(urls[i])

for i in range(len(not_downloaded_names)):
    print(not_downloaded_names[i])

    
