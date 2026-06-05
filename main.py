from image_analyzer import analyze_image
from spotify_test import get_liked_songs
import json
analysis = analyze_image("testimage.jpeg")

print("Image Analysis:")
print(repr(analysis))

data = json.loads(analysis)
songs = get_liked_songs()

print(f"\nFound {len(songs)} liked songs")
print("\nFirst 5 songs:")
for song in songs[:5]:
    print(f"{song['name']} - {song['artist']}")

print("\nMood detected:", data["mood"])