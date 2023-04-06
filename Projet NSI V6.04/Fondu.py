#Test 1

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


#Test 2
def fadeout(color):
    fade_out = pygame.Surface((screen_width, screen_height))
    fade_out = fade_out.convert()
    fade_out.fill(color)
    for i in range(255):
        fade_out.set_alpha(i)
        screen.blit(fade_out, (0, 0))
        pygame.display.update()


def fadein(newbackground):
    fade_in = pygame.Surface((screen_width, screen_height))
    fade_in = fade_in.convert()
    fade_in.fill(newbackground)
    for i in range(255):
        fade_in.set_alpha(255-i)
        screen.blit(fade_in, (0, 0))
        pygame.display.update()

