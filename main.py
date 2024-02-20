from json_handler import read_songs_from_json
from csv_handler import read_songs_from_csv
from playlist import Playlist
from menu import Menu

def main():
    json_songs = read_songs_from_json('songs.json')
    csv_songs = read_songs_from_csv('songs.csv')

    all_songs = json_songs + csv_songs

    playlist = Playlist("My Playlist")

    for song in all_songs:
        playlist.add_song(song)

    menu = Menu(playlist)
    menu.show_menu()

if __name__ == "__main__":
    main()