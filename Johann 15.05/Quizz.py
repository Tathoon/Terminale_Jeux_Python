import pygame
from pygame.locals import *
from random import randint
import time


from Button import button

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
    def __init__(self, reponse_marquee):

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
        self.font = pygame.font.Font("police_score.ttf", 24)
        self.domaine = 0
        self.num_question = 0
        self.question_posee = ""
        self.reponse_marquee = reponse_marquee
        self.valider = button("bouton_valider.png", 12, 12, 200, 300)


    def choisir_question(self):

        self.domaine = randint(0,3)
        self.num_question = randint(0,4)
        self.question_posee = str(self.questions[self.domaine][self.num_question])
        if self.question_posee not in self.questionsposees:
            self.questionsposees.append(self.question_posee)
        else:
            while self.question_posee in self.questionsposees:
                self.domaine = randint(0,3)
                self.num_question = randint(0,4)
                self.question_posee = str(self.questions[self.domaine][self.num_question])
        return self.question_posee


    def verif_reponse(self, reponse_marquee):

        hauteur=100
        souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clic[0] == 1: #on vérifie si on fait clic gauche
                    if hauteur > souris[1] > hauteur - 50: #on vérifie les coordonnées de la position du curseur
                        if self.reponses[self.domaine][self.num_question] in reponse_marquee: #on vérifie si la réponse est juste
                            self.score+=1



    def affiche_question(self):

        police_question = self.font.render(self.question_posee, True, (0,0,0))
        rect2 = police_question.get_rect()
        rect2.topleft = (100, 50)
        self.screen.blit(police_question, rect2)

    def affiche_reponse(self):

        reponse = pygame.image.load("asset_reponse2.png")
        rep_rect = reponse.get_rect()
        rep_rect.bottomleft = (500, 630)
        self.screen.blit(reponse, rep_rect)


    def affiche_score(self):

        score_texte = self.font.render(f"Score: {self.score}", 1, (0,0,0))
        rect3 = score_texte.get_rect()
        rect3.midleft= (100, 50)
        self.screen.blit(score_texte, rect3)


    def update_all(self):
        self.screen.blit(self.valider, (200,300))
        self.screen.blit(background, (0,0))
        self.screen.blit(question, (300, 50))
        self.screen.blit(reponse, (420, 590))
        self.screen.blit(police, rect)
        screen.blit(police_question, rect2)
        screen.blit(score_texte, rect3)


    def update_all(self):
        self.screen.blit(self.background, (0, 0))
        self.affiche_question()
        self.affiche_reponse()
        self.affiche_score()


