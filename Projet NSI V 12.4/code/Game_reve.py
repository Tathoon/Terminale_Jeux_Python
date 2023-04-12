import pygame
import pyscroll
import pytmx
from Map import MapManager

class monde_reve:
    def __init__(self, mainScreen):
        self.is_active = True
        # generer un joueur 
        self.player = player_reve(640, 607)
        self.map_manager = MapManager(mainScreen, self.player)

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



class player_reve(pygame.sprite.Sprite):

    def __init__(self,x ,y):
        super().__init__() # verifier super class
        self.sprite_sheet = pygame.image.load('assets_monde_reve/sprites/player_reve.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'up': self.get_image(0, 96),
            'down': self.get_image(0, 0),
            'right': self.get_image(0, 64),
            'left': self.get_image(0, 32),
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 1

    def save_location(self): self.old_position = self.position.copy()

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey((0, 0, 0)) #on enleve le fond noir

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image