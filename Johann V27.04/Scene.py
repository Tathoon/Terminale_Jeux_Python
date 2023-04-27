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


    def verif_reponse(self):

        hauteur=100
        souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()
        if clic[0] == 1: #on vérifie si on fait clic gauche
            if hauteur > souris[1] > hauteur - 50: #on vérifie les coordonnées de la position du curseur
                if self.options[self.question_actuelle][reponse] == self.reponses[self.question_actuelle]:: #on vérifie si la réponse est juste
                    self.score += 1 #on augmente le score
                self.question_actuelle += 1 #on change de question


    def affiche_question(self):

        question_texte = self.police.render(self.choisir_question(), 1, (0, 0, 0))
        questionpos = question_texte.get_rect()
        questionpos.centerx = self.background.get_rect().centerx
        self.screen.blit(question_texte, (questionpos))


    def affiche_reponses(self):
        hauteur = 100
        for reponse in range(len(self.options[self.question_actuelle])):
            reponse_texte = self.police.render(self.options[self.question_actuelle][reponse], 1, (0, 0, 0))
            self.screen.blit(reponse_texte, (100, hauteur))
            hauteur += 50


    def affiche_options(self):
        option1 = button()
        option2 = button()
        option3 = button()
        option4 = button()


    def affiche_score(self):
        score_texte = self.police.render("Score: " + str(self.score), 1, (255, 0, 0))
        self.screen.blit(score_texte, (50, 50))


    def partie_questionnaire(self):
        self.affiche_question()
        self.affiche_options()
        self.affiche_reponses()
        self.verif_reponse()

