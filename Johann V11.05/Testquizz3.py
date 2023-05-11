"""Edit text with the keyboard."""
import pygame
from pygame.locals import *
import time


from Quizz import quizz

Noir = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))

reponse_marquee = 'Ici'
font = pygame.font.SysFont(None, 48)
police = font.render(reponse_marquee, True, Noir)
rect = police.get_rect()
rect.bottomleft = (500, 630)
cursor = Rect(rect.topright, (3, rect.height))
question="salut ça va ?"
police_question = font.render(question, True, Noir)
rect2 = police_question.get_rect()
rect2.topleft = (500, 50)


reponse = pygame.image.load("asset_reponse2.png")
rep_rect = reponse.get_rect()
rep_rect.bottomleft = (500, 630)

score = 0
score_texte = font.render(("Score : " + str(score)), True, Noir)
rect3 = police.get_rect()
rect3.midleft= (100, 50)
running = True
background = pygame.transform.scale(pygame.image.load("background_quizz.jpg"),(1280,720))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                if len(reponse_marquee)>0:
                    reponse_marquee = reponse_marquee[:-1]
            else:
                text += event.unicode
            police = font.render(reponse_marquee, True, Noir)
            rect.size=police.get_size()
            cursor.topleft = rect.topright
            if event.key == K_LSHIFT:
                if text == "oui":
                    score+=1
                    screen.blit(score_texte, rect3)

    screen.blit(background, (0,0))
    #screen.blit(question, (300, 50))
    screen.blit(reponse, (420, 590))
    screen.blit(police, rect)
    screen.blit(police_question, rect2)
    screen.blit(score_texte, rect3)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, Noir, cursor)
    pygame.display.update()

pygame.quit()