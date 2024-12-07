import pygame

def fadeout(image, fade_color, speed, mainScreen):
    # Créer une surface du même taille que l'écran pour le fondu
    fade_surf = pygame.Surface((mainScreen.get_width(), mainScreen.get_height()))
    # Convertir la surface en un format approprié pour l'affichage
    fade_surf = fade_surf.convert_alpha()
    # Remplir la surface avec la couleur de fondu
    fade_surf.fill(fade_color)
    # Boucle pour ajuster l'opacité de la surface de fondu
    for alpha in range(0, 255, speed):
        # Ajuster l'opacité de la surface de fondu
        fade_surf.set_alpha(alpha)
        # Afficher l'image actuelle à l'écran
        mainScreen.blit(image, (0, 0))
        # Afficher la surface de fondu sur l'image actuelle
        mainScreen.blit(fade_surf, (0, 0))
        # Mettre à jour l'affichage
        pygame.display.update()
        # Attendre un court moment avant la prochaine étape du fondu
        pygame.time.wait(5)

# Fonction de fondu entrant
def fadein(image, fade_color, speed, mainScreen):
    # Créer une surface du même taille que l'écran pour le fondu
    fade_surf = pygame.Surface((mainScreen.get_width(), mainScreen.get_height()))
    # Convertir la surface en un format approprié pour l'affichage
    fade_surf = fade_surf.convert_alpha()
    # Remplir la surface avec la couleur de fondu
    fade_surf.fill(fade_color)
    # Boucle pour ajuster l'opacité de la surface de fondu
    for alpha in range(255, -1, -speed):
        # Ajuster l'opacité de la surface de fondu
        fade_surf.set_alpha(alpha)
        # Afficher l'image actuelle à l'écran
        mainScreen.blit(image, (0, 0))
        # Afficher la surface de fondu sur l'image actuelle
        mainScreen.blit(fade_surf, (0, 0))
        # Mettre à jour l'affichage
        pygame.display.update()
        # Attendre un court moment avant la prochaine étape du fondu
        pygame.time.wait(5)

def change_image_with_transition(actu_image, new_image, fade_color, speed, mainScreen):
    # Faire un fondu sortant de l'image actuelle
    fadeout(actu_image, fade_color, speed, mainScreen)
    # Faire un fondu entrant de la nouvelle image
    fadein(new_image, fade_color, speed, mainScreen)