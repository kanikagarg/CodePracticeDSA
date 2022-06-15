class Song:
	song_id = ""
	song_name = ""
	composer = ""
	file = ""

    def __init__(self, song_id,song_name, composer, file) -> None:
        self.song_id = song_id
        self.song_name = song_name
        self.composer = composer
        self.file = file
    
    def get_file(self):
        return self.file

    def get_composer(self):
        return self.composer

    def get_song_id(self):
        return self.song_id

class Playlist:
    # List of songs
    list = []

    # Name for the playlist
    list_name = ""

    def __init__(self, name) -> None:
        self.name = name

    def get_playlist(name):
        playlist = Playlist(name)
        return playlist

    def add_song(self,song : Song):
        list.append(song)
        
    def remove_song(self, song : Song):
        list.remove(song)

    def play_songs(self):
        # Logic for playing songs
        return list

    def stop(self):
        # Logic for stopping the songs
        return list

    def resume(self):
        # Logic for resume the songs play
        return list

    def pause(self):
        # Logic for pause the song playing
        return list

    def play_previous(self):
        # Logic for running song, previous to the current playing song from the list
        self.play_songs

    def play_next(self):
        # Logic for running song, next to the current playing song in the list
        self.play_songs
