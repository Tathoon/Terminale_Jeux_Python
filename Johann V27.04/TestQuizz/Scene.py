import pygame
from random import randint

from Button import button

class scene:
    """
    scene qui correspond à une question posée
    ###Attributs :
        -question : question posée
        -reponse : réponse correspondante à la question
        -options : les différentes propositions de réponses à la question
        -background : arrière-plan (toujours le même quelque soit la question
        -screen : écran sur lequel est affiché le questionnaire
        -police : police d'écriture
     ###Méthodes :
        -affiche_question : affiche la question
        -affiche_options : affiche les différentes possibilités de réponses (Boutons cliquables)
        -affiche_reponse : affiche les différentes possibilités de réponses
        -verif_reponse : vérifier que la réponse sélectionnée soit juste ou fausse
        -partie_questionnaire : déroulement du jeu pour une seule scène dont les méthodes proviennent directement de la classe quizz
    """

    def __init__(self, screen, question, reponse, options, background, coordonnees_rep):
        self.question = question
        self.reponse = reponse
        self.options = options
        self.background = background
        self.screen = screen
        self.police = pygame.font.Font(None, 16)
        self.coordonnees_reponse = coordonnees_rep
