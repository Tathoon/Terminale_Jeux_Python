import pygame
from pygame.locals import *
from random import randint
import time

class quizz:
    """
    Classe correspondant à la 2ème quête / minijeu c'est à dire le Quizz

    ###Attributs :
        - questions : questions sous forme de listes de listes regroupés par domaine
        - reponses : reponses correspondantes aux questions sous forme de listes de listes

    ###Méthodes :
        -affiche_question : affiche la question
        -affiche_options : affiche les différentes possibilités de réponses (Boutons cliquables)
        -affiche_reponse : affiche les différentes possibilités de réponses
        -verif_reponse : vérifier que la réponse sélectionnée soit juste ou fausse
    """

    def __init__(self, font):

        self.questions = [
        ["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"],
        ["Quelle figure de style consiste à coller deux mots de sens contraires dans une phrase ?", "Quel grand dramaturge est l'auteur de la pièce 'Le Malade Imaginaire ?'", "Quel célèbre écrivain romantique du XVIIIe est Ã  l'origine du receuil 'Les Contemplations' ?", "Dans quel registre figure l'expression de la pitié en littérature ?", "De quel mot français utilisé généralement durant la période moyennageuse provient le terme chaussure ?"],
        ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve français ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
        ["En quelle année s'est produit la très célèbre bataille de Waterloo ?", "En quelle année s'est produite la déclaration d'indépendance des Eu ?", "Quel grand empereur romain a vaincu Vercingétorix en 52 av. J-C ?", "Quel autre nom très célèbre donne-t-on à la traite négrière entre l'Europe, l'Afrique noire et l'Amérique datant du XVIIIe siècle ?" , "En quelle année s'est déroulée la chute du mur de Berlin ?"]]
        self.reponses = [["2008", "33", "Djokovic", "France", "2"],
        ["oxymore", "Molière", "Hugo", "pathétique", "chausse"],
        ["27", "Guatemala", "Indonésie", "Loire", "6"],
        ["1815", "1783", "Jules César", "commerce triangulaire", "1989"]]
        self.questionsposees = []
        self.questionsmax = 10
        self.background = pygame.transform.scale(pygame.image.load("background_quizz.jpg"),(1280,720))
        self.screen = pygame.display.set_mode((1280, 720))
        self.score = 0
        self.font = font


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

        if reponse_marquee == self.reponses[domaine][num_question]:
            score+=1


    def affiche_question(self):

        police_question = font.render(question_posee, True, Noir)
        rect2 = police_question.get_rect()
        rect2.topleft = (100, 50)

    def affiche_reponse(self):

        reponse = pygame.image.load("asset_reponse2.png")
        rep_rect = reponse.get_rect()
        rep_rect.bottomleft = (500, 630)


    def affiche_score(self):

        score_texte = self.police.render("Score: " + str(self.score), 1, (255, 0, 0))
        rect3 = police.get_rect()
        rect3.midleft= (100, 50)


    def switch_question(self):
        self.choisir_question()
        screen.blit()


    def update_all(self):
        screen.blit(background, (0,0))
        #screen.blit(question, (300, 50))
        screen.blit(reponse, (420, 590))
        screen.blit(police, rect)
        screen.blit(police_question, rect2)
        screen.blit(score_texte, rect3)


