import pygame
import pyscroll
import pytmx
from map import MapManager
from player import Player

class Game:

    def __init__(self):
        #creer la fenetre du jeu

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arène")

        # generer un joueur 
        self.player = Player(640, 607)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        #touche pour deplacement du joueur
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')

    def update(self):
        self.map_manager.update()

    def run(self):
        #boucle du jeu

        clock = pygame.time.Clock()
        
        running = True

        while running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(144)

        pygame.quit()