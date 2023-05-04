import pygame
from random import randint
from Scene import scene
from Button import button


class quizz:
    """
    Classe correspondant à la 2ème quête / minijeu c'est à dire le Quizz
    ###Attributs :
        --> Score : nombre de bonnes réponses du joueur
    ###Méthodes :
        -affiche_question : affiche la question
        -affiche_options : affiche les différentes possibilités de réponses (Boutons cliquables)
        -affiche_reponse : affiche les différentes possibilités de réponses
        -verif_reponse : vérifier que la réponse sélectionnée soit juste ou fausse
    """

    def __init__(self):

        self.color = (0, 0, 0)
        self.screen = pygame.display.set_mode((1280, 720))
        self.text = 'Entrez votre réponse'
        self.font = pygame.font.SysFont(None, 48)
        self.img = font.render(text, True, Noir)
        self.rect = img.get_rect()
        self.rect.topleft = (500, 630)
        self.cursor = Rect(rect.topright, (3, rect.height))
        self.background = pygame.transform.scale(pygame.image.load("background_quizz.jpg"),(1280,720))
        self.score = 0



    def affiche_question(self):
