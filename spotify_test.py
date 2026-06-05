from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()
def get_liked_songs():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope="user-library-read"
        )
    )
    song=[]
    songs = sp.current_user_saved_tracks(limit=50)

    for item in songs["items"]:
        track=item["track"]
        song.append(
            {
                "id":track["id"],
                "name":track["name"],
                "artist":track["artists"][0]["name"]
            }
        )
    return song

    
