import pygame
#couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)


#police
police = pygame.font.Font(None, taille_police)

#variables
question_actuelle = 0
score = 0

    # Affiche la question
    ecran.fill(BLANC)
    question_texte = police.render(questions[question_actuelle], True, NOIR)
    ecran.blit(question_texte, (50, 50))

    # Affiche les réponses
    y = 100
    for reponse in reponses[question_actuelle]:
        reponse_texte = police.render(reponse, True, NOIR)
        ecran.blit(reponse_texte, (100, y))
        y += 50

    # Vérifie la réponse 
    souris = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()
    if clic[0] == 1:
        if y > souris[1] > y - 50:
            if reponses[question_actuelle][0] == "Paris":
                score += 1
            question_actuelle += 1

    # Affiche le score
    score_texte = police.render("Score: " + str(score), True, ROUGE)
    ecran.blit(score_texte, (50, hauteur - 50))

    pygame.display.flip()