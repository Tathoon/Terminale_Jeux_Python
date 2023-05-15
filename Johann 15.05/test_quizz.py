import pygame
from pygame.locals import *
import time


from Quizz import quizz
from Button import button

Noir = (0, 0, 0)

pygame.init()

reponse_marquee = 'Ici'

test = quizz(reponse_marquee)

valider = button("bouton_valider.png", 120, 120, 200, 300)
valid_rect = valider.image.get_rect()
test.screen.blit(valider.image, valid_rect)

font = pygame.font.SysFont(None, 48)
police = font.render(test.reponse_marquee, True, Noir)
rect = police.get_rect()
rect.bottomleft = (500, 630)
cursor = Rect(rect.topright, (3, rect.height))

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                if len(reponse_marquee)>0:
                    test.reponse_marquee = test.reponse_marquee[:-1]
            else:
                test.reponse_marquee += event.unicode
            police = font.render(test.reponse_marquee, True, Noir)
            rect.size=police.get_size()
            cursor.topleft = rect.topright

    if time.time() % 1 > 0.5:
        pygame.draw.rect(test.screen, Noir, cursor)
    test.update_all()


    while len(test.questionsposees)<test.questionsmax:

        test.choisir_question()
        test.affiche_question()
        test.affiche_reponse()
        if valider.rect.collidepoint(event.pos):
            test.verif_reponse(reponse_marquee)
        test.affiche_score()
        test.update_all()

    pygame.display.update()

pygame.quit()