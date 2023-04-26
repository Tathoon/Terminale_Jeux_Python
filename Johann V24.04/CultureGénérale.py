import pygame
from random import randint

class Quizz:

    def __init__(self, screen):

        self.questions = [
            ["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"]]
        self.reponses = [["2008", "33", "Djokovic", "France", "2"]]
        self.options = []
        self.questionsposees = []
        self.questionsmax = 10
        self.screen = screen
        self.background = pygame.image.load("quizz.png").convert()
        self.score = 0
        self.question_actuelle = 0
        self.police = pygame.font.Font(None, 16)


    def choisir_question(self):

        domaine = randint(0,3)
        num_question = randint(0,4)
        question_posee = str(self.questions[domaine][num_question])
        if question_posee not in self.questionsposees:
            self.questionsposees.append(question_posee)
        else:
            while question_posee in self.questionsposees:
                domaine = randint(0,3)
                num_question = randint(0,4)
                question_posee = str(self.questions[domaine][num_question])
        return question_posee


    def verif_reponse(self):

        hauteur=100
        souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()
        if clic[0] == 1: #on vérifie si on fait clic gauche
            if hauteur > souris[1] > hauteur - 50: #on vérifie les coordonnées de la position du curseur
                if self.options[self.question_actuelle][reponse] == self.reponses[self.question_actuelle]:: #on vérifie si la réponse est juste
                    self.score += 1 #on augmente le score
                self.question_actuelle += 1 #on change de question


    def affiche_questions(self):

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


    def affiche_score(self):
        score_texte = self.police.render("Score: " + str(self.score), 1, (255, 0, 0))
        self.screen.blit(score_texte, (50, 50))


    def end_quizz(self):

        if len(self.questionsposees) == self.questionsmax:
            self.affiche_score()

    def partie(self):

        for question in range(self.questionsmax):
            self.choisir_question()
            self.affiche_questions()
            self.affiche_reponses()
            self.verif_reponse()
            pygame.display.flip()
        self.end_quizz()

