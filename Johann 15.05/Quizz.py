import pygame
from pygame.locals import *
import time

from Fonctions import *
from Button import button

Noir = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((1280, 720))

questions = [
        ["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"],
        ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve français ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
        ["En quelle année s'est produit la très célèbre bataille de Waterloo ?", "En quelle année s'est produite la déclaration d'indépendance des Eu ?", "Quel grand empereur romain a vaincu Vercingétorix en 52 av. J-C ?", "Quel autre nom très célèbre donne-t-on à la traite négrière entre l'Europe, l'Afrique noire et l'Amérique datant du XVIIIe siècle ?" , "En quelle année s'est déroulée la chute du mur de Berlin ?"]]




reponses = [["2008", "33", "Djokovic", "France", "2"],
            ["27", "Guatemala", "Indonésie", "Loire", "6"],
            ["1815", "1776", "Jules César", "commerce triangulaire", "1989"]]

questionsposees = []
questionsmax = 10

reponse_marquee = 'Ici'
font = pygame.font.SysFont(None, 48)
police = font.render(reponse_marquee, True, Noir)
rect = police.get_rect()
rect.bottomleft = (500, 630)
cursor = Rect(rect.topright, (3, rect.height))

domaine = randint(0,2)
num_question = randint(0,4)
question_posee = str(questions[domaine][num_question])
if question_posee not in questionsposees:
    questionsposees.append(question_posee)
else:
    while question_posee in questionsposees:
        domaine = randint(0,3)
        num_question = randint(0,4)
        question_posee = str(questions[domaine][num_question])


police_question = font.render(question_posee, True, Noir)
rect2 = police_question.get_rect()
rect2.topleft = (400, 50)


reponse = pygame.image.load("asset_reponse2.png")
rep_rect = reponse.get_rect()
rep_rect.bottomleft = (500, 630)

score = 0

valider = button("valider.png", 120, 120, 200, 300)
valid_rect = valider.image.get_rect()
screen.blit(valider.image, (200,300))

running = True
background = pygame.transform.scale(pygame.image.load("background_quizz.jpg"),(1280,720))

while running:
    screen.blit(background, (0,0))
    screen.blit(reponse, (420, 590))
    screen.blit(police, rect)
    screen.blit(police_question, rect2)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                if len(reponse_marquee)>0:
                    reponse_marquee = reponse_marquee[:-1]

            else:
                reponse_marquee += event.unicode
            police = font.render(reponse_marquee, True, Noir)
            rect.size=police.get_size()
            cursor.topleft = rect.topright

        # Vérifier si la réponse est correcte
        if reponse_marquee.lower() == reponses[domaine][num_question].lower():

            score+=1
            domaine = randint(0,2)
            num_question = randint(0,4)
            question_posee = str(questions[domaine][num_question])
            if question_posee not in questionsposees:
                questionsposees.append(question_posee)

            screen.blit(police_question, rect2)

            reponse_marquee = "Ici"

    affiche_score(font, screen, score)

    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, Noir, cursor)
    pygame.display.update()

pygame.quit()