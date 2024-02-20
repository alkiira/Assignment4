import json
from song import Song
from artist import Artist


def read_songs_from_json(file_path):
    songs = []
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            title = item['title']
            artist_name = item['artist']
            duration = item['duration']
            artist = Artist(artist_name)
            song = Song(title, artist, duration)
            songs.append(song)
    return songs
