from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-library-read"
    )
)

songs = sp.current_user_saved_tracks(limit=10)

for item in songs["items"]:
    print(item["track"]["name"])
    