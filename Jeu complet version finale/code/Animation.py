import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, path):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'{path}assets_monde_reve/sprites/{name}.png')
        self.animation_index = 0
        self.images = {                      # creer un dictionnaire d'images pour les différentes animations du joueur, chaque clé du dictionnaire représente une direction d'animation (haut, bas, droite, gauche) et est associée à une sous-image de l'attribut "sprite_sheet" obtenue à partir de la méthode "get_image()"
            'up': self.get_images(32),
            'down': self.get_images(0),
            'right': self.get_images(96),
            'left': self.get_images(64),
        }
        self.nb_images = 5
        self.index_anim = 0
        self.clock = 0
        self.speed = 1


    def get_image(self, x, y):
        image = pygame.Surface([16, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 32))
        return image

    def get_images(self, y):
        images_animations = []

        for i in range(0,3):
            x=i*16
            image = self.get_image(x, y)
            images_animations.append(image)

        return images_animations

    def change_animations(self, name):

        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:

            self.animation_index+=1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0