from song_profiler import profile_batch

songs = [
    {
        "name": "505",
        "artist": "Arctic Monkeys"
    },
    {
        "name": "Yellow",
        "artist": "Coldplay"
    },
    {
        "name": "Ditto",
        "artist": "NewJeans"
    }
]

result = profile_batch(songs)

print(result)