"""Edit text with the keyboard."""
import pygame
from pygame.locals import *
import time

Noir = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))

text = 'Entrez votre réponse '
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, Noir)
rect = img.get_rect()
rect.topleft = (500, 630)
cursor = Rect(rect.topright, (3, rect.height))
reponse = pygame.image.load("asset_reponse2.png")
rep_rect = reponse.get_rect()
rep_rect.topleft = (500, 630)
question = pygame.image.load("asset_question.png")
rep_quest = question.get_rect()
rep_quest.topleft = (50, 50)


running = True
background = pygame.transform.scale(pygame.image.load("background_quizz.jpg"),(1280,720))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, Noir)
            rect.size=img.get_size()
            cursor.topleft = rect.topright


    screen.blit(background, (0,0))
    screen.blit(question, rect)
    screen.blit(reponse, (420, 590))
    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, Noir, cursor)
    pygame.display.update()

pygame.quit()
"""
    def affiche_score(self):
        score_texte = self.police.render("Score: " + str(self.score), True, (255, 0, 0))
        self.screen.blit(score_texte, (50, 50))

"""