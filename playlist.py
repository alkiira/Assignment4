class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def find_songs_by_artist(self, artist_name):
        return [song for song in self.songs if song.artist.name == artist_name]

    def __str__(self):
        return f"Playlist: {self.name}"

