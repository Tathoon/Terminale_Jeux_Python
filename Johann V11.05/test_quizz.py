import pygame
from pygame.locals import *
import time


from Quizz import quizz

Noir = (0, 0, 0)

pygame.init()

reponse_marquee = 'Ici'
font = pygame.font.SysFont(None, 48)
police = font.render(reponse_marquee, True, Noir)
rect = police.get_rect()
rect.bottomleft = (500, 630)
cursor = Rect(rect.topright, (3, rect.height))
question="salut ça va ?"

running = True

test = quizz(font)

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
            if event.key == K_TAB:
                if text == "oui":
                    score+=1
                    screen.blit(score_texte, rect3)

    update_all()
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, Noir, cursor)
    while len(questions_posees)<questions_max:

    test.choisir_question()
    test.affiche_question()
    test.affiche_reponse()
    test.verif_reponse()
    test.affiche_score()
    test.update_all()

    pygame.display.update()

pygame.quit()