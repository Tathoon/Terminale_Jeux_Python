import pygame
from random import randint

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

    def __init__(self, screen):

        self.questions = [
        ["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"],
        ["Quelle figure de style consiste à coller deux mots de sens contraires dans une phrase ?", "Quel grand dramaturge est l'auteur de la pièce 'Le Malade Imaginaire ?'", "Quel célèbre écrivain romantique du XVIIIe est Ã  l'origine du receuil 'Les Contemplations' ?", "Dans quel registre figure l'expression de la pitié en littérature ?", "De quel mot français utilisé généralement durant la période moyennageuse provient le terme chaussure ?"],
        ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve français ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
        ["En quelle année s'est produit la très célèbre bataille de Waterloo ?", "En quelle année s'est produite la déclaration d'indépendance des Eu ?", "Quel grand empereur romain a vaincu Vercingétorix en 52 av. J-C ?", "Quel autre nom très célèbre donne-t-on à la traite négrière entre l'Europe, l'Afrique noire et l'Amérique datant du XVIIIe siècle ?" , "En quelle année s'est déroulée la chute du mur de Berlin ?"]]
        self.reponses = [["2008", "33", "Djokovic", "France", "2"],
        ["oxymore", "Molière", "Hugo", "pathétique", "chausse"],
        ["27", "Guatemala", "Indonésie", "Loire", "6"],
        ["1815", "1783", "Jules César", "commerce triangulaire", "1989"]]
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


    def affiche_score(self):
        score_texte = self.police.render("Score: " + str(self.score), 1, (255, 0, 0))
        self.screen.blit(score_texte, (50, 50))

    def partie(self):

        for question in range(self.questionsmax):
            self.choisir_question()
            self.affiche_questions()
            self.affiche_reponses()
            self.verif_reponse()
            pygame.display.flip()
        self.end_quizz()