class SoundDesign:

    def __init__(self):
        self.musics = {
        "Accueil" : "music_accueil.mp3"
        "Menu": "music_menu.mp3"
        "Quetes" : "music_quetes.mp3"
        }


    def load_music(self, name)
        mixer.music.load(self.musics[name])

    def music_volume(self, volume)
        mixer.set_volume(volume)

    def play_song(self, name)
        mixer.music.play(-1)