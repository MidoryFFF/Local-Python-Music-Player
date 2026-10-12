from audio_player import TrakPlayer

class PlayList:
    def __init__(self):
        self.volume = 50
        self.play_list: list[str] = []

    def add_to_playlist(self, trak_paths):
        if type(trak_paths) == str:
            self.play_list.append(trak_paths)
            return

        for trak_path in trak_paths:
            self.play_list.append(trak_path)

    def get_playlist(self):
        return self.play_list

    def remove_from_playlist_by_index(self, index):
        del self.play_list[id]

    def start_playlist(self):
        for i in self.play_list:
            trak_player = TrakPlayer(i, self.volume / 100)
            trak_player.load_trak()
            trak_player.play_trak()
