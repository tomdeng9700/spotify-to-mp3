import os

# pip install python-dotenv
from dotenv import load_dotenv
# pip install spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist_uri = 'https://open.spotify.com/playlist/2B17v6HfMJPIgHcOhMYnSd?si=2008c80328734a4f'
# playlist = sp.playlist_tracks(playlist_uri)

def get_playlist(playlist_uri):
    playlist_uri = 'https://open.spotify.com/playlist/2B17v6HfMJPIgHcOhMYnSd?si=2008c80328734a4f'
    playlist = sp.playlist_tracks(playlist_uri)

    tracks = []
    for track in playlist['items']:
        track_name = track['track']['name']
        artists = [artist['name'] for artist in track['track']['artists']]
        tracks.append((track_name, artists))
        # print(f"Track: {track_name}, Artists: {', '.join(artists)}")

    return tracks