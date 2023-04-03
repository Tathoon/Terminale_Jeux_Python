def fondu(SCREENWIDTH, SCREENHEIGHT):
    fondu = pygame.mainScreen((SCREENWIDTH, SCREENHEIGHT, image_depart, image_transition))
    fondu.fill((0,0,0))
    opacity = 0

    for r in range(0, 300): #Fondu de l'image au fond noir
        opacity += 1
        fondu.set_alpha(opacity)
        screen.blit(image_depart,[0,0])
        screen.blit(fondu, (0,0))
        pygame.display.update()

    for r in range(0, 300): #Fondu du fond noir à une autre image
        opacity -= 1
        fondu.set_alpha(opacity)
        screen.blit(image_transition,[0,0])
        screen.blit(fondu, (0,0))
        pygame.display.update()
