import pygame
from pygame import *

class soundDesign:

    def __init__(self):
        self.musics = {
        "intro" : "musiques/mus_intro.mp3",
        "menu_quetes" : "musiques/mus_menu_quete.mp3",
        "quete1" : "musiques/mus_quete1.mp3",
        "quete2" : "musiques/mus_quete2.mp3",
        "quete3" : "musiques/mus_quete3.mp3"
        }

    def play_music(self, name, volume):
        self.load_music(name)
        self.music_volume(volume)
        self.play_song()

    def load_music(self, name):
        mixer.music.load(self.musics[name]) # Import avec le chemin

    def music_volume(self, volume):
        mixer.music.set_volume(volume) # Gestion du volume

    def play_song(self):
        mixer.music.play(-1) # Mis en route de la musique. La valeur -1 permet de la jouer en continu