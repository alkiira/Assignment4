from artist import Artist
from song import Song


class Menu:
    def __init__(self, playlist):
        self.playlist = playlist

    def add_song(self, song):
        self.playlist.add_song(song)
        print(f"Added '{song.title}' to the playlist.")

    def delete_song(self, song):
        if song in self.playlist.songs:
            self.playlist.remove_song(song)
            print(f"Deleted '{song.title}' from the playlist.")
        else:
            print("Song not found in the playlist.")

    def display_playlist(self):
        print("Playlist:")
        for song in self.playlist.songs:
            print(song)

    def search_songs_by_artist(self, artist_name):
        songs_by_artist = self.playlist.find_songs_by_artist(artist_name)
        if songs_by_artist:
            print(f"Songs by {artist_name}:")
            for song in songs_by_artist:
                print(song)
        else:
            print(f"No songs found by {artist_name}.")

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Song")
            print("2. Delete Song")
            print("3. Search Songs by Artist")
            print("4. Display Playlist")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter song title: ")
                artist_name = input("Enter artist name: ")
                duration = input("Enter song duration: ")
                artist = Artist(artist_name)
                song = Song(title, artist, duration)
                self.add_song(song)
            elif choice == "2":
                title = input("Enter title of the song to delete: ")
                song_to_delete = next((song for song in self.playlist.songs if song.title == title), None)
                if song_to_delete:
                    self.delete_song(song_to_delete)
                else:
                    print("Song not found in the playlist.")
            elif choice == "3":
                artist_name = input("Enter artist name to search songs: ")
                self.search_songs_by_artist(artist_name)
            elif choice == "4":
                self.display_playlist()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")