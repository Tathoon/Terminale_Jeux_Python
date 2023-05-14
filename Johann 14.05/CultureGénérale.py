import pygame
from random import randint
from Scene import scene
from Button import button


class quizz:
    """
    Classe correspondant à la 2ème quête / minijeu c'est à dire le Quizz
    ###Attributs :
        --> Pas d'attributs : la classe ne regroupe que les méthodes nécessaires au bon déroulement du questionnaire
    ###Méthodes :
        -affiche_question : affiche la question
        -affiche_options : affiche les différentes possibilités de réponses (Boutons cliquables)
        -affiche_reponse : affiche les différentes possibilités de réponses
        -verif_reponse : vérifier que la réponse sélectionnée soit juste ou fausse
    """

    def __init__(self):
        self.score = 0


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
        A = button(None, dim_x, dim_y, pos_x, pos_y)
        B = button(None, dim_x, dim_y, pos_x, pos_y)
        C = button(None, dim_x, dim_y, pos_x, pos_y)
        D = button(None, dim_x, dim_y, pos_x, pos_y)


    def affiche_score(self):
        score_texte = self.police.render("Score: " + str(self.score), 1, (255, 0, 0))
        self.screen.blit(score_texte, (50, 50))

    def switch_scene(self):
        A = button(None, dim_x, dim_y, pos_x, pos_y)
        B = button(None, dim_x, dim_y, pos_x, pos_y)
        C = button(None, dim_x, dim_y, pos_x, pos_y)
        D = button(None, dim_x, dim_y, pos_x, pos_y)
        for event in pygame.event.get(): # verifie si le joueur quite le jeu et si oui on arrete la boucle
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if A is pressed() or if B is pressed() or if C is pressed() or if D is pressed():
                            index+=1
                            Scene_actu = liste_question[index]



    def partie(self):
        questions = []
        Question1 = Scene()
        Question2 = Scene()
        Question3 = Scene()
        Question4 = Scene()
        Question5 = Scene()
        Question6 = Scene()
        Question7 = Scene()
        Question8 = Scene()
        Question9 = Scene()
        Question10 = Scene()
        liste_question = [Question1 ,Question2 ,Question3 ,Question4 ,Question5 ,Question6 ,Question7 ,Question8 ,Question9 ,Question10]
        index=0
        Scene_actu = liste_question[index]
        self.switch_scene()