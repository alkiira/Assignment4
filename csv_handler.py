import csv
from song import Song
import csv
from song import Song
from artist import Artist

def read_songs_from_csv(file_path):
    songs = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['Title']
            artist_name = row['Artist']
            duration = row['Duration']
            artist = Artist(artist_name)
            song = Song(title, artist, duration)
            songs.append(song)
    return songs