import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, x1:int, y1:int, up:int, down:int, right:int, left:int, begincut:int, cut:int, nbcut:int):
        
        """ 
            name -> Nom du Sprite
            x1 -> Taille x du sprite en pixels
            y1 -> Taille y du sprite en pixels
            up -> Coordonnees y du sprite par rapport aux autres sprites (ici on veut la coordonnee y ou le sprite regarde vers le haut)
            down -> Coordonnees y du sprite par rapport aux autres sprites (ici on veut la coordonnee y ou le sprite regarde vers le bas)
            right -> Coordonnees y du sprite par rapport aux autres sprites (ici on veut la coordonnee y ou le sprite regarde vers la droite)
            left -> Coordonnees y du sprite par rapport aux autrse sprites (ici on veut la coordonnee y ou le sprite regarde vers la gauche)
            begincut -> Defini où on commence à couper l'image (donc pour les animations : soit up, down, right ou left)
            cut -> Defini où on finit de couper l'image (donc pour les animations : soit up, down, right ou left)
            nbcut -> Defini le nombre de fois ou on coupe l'image (donc pour les animations : soit up, down, right ou left)
        """

        super().__init__()
        self.sprite_sheet = pygame.image.load(f'assets_monde_reve\sprites\{name}.png')
        self.animation_index = 0
        self.images = {
            'up': self.get_images(up, x1, y1, begincut, cut, nbcut),
            'down': self.get_images(down, x1, y1, begincut, cut, nbcut),
            'right': self.get_images(right, x1, y1, begincut, cut, nbcut),
            'left': self.get_images(left, x1, y1, begincut, cut, nbcut),
        }
        self.nb_images = 3
        self.index_anim = 0
        self.clock = 0
        self.speed = 1


    def get_image(self, x, y, x1, y1):
        image = pygame.Surface([x1, y1])
        image.blit(self.sprite_sheet, (0, 0), (x, y, x1, y1))
        return image

    def get_images(self, y, x1, y1, begincut, cut, nbcut):
        images_animations = []

        for i in range(begincut, cut):
            x=i*nbcut
            image = self.get_image(x, y, x1, y1)
            images_animations.append(image)

        return images_animations

    def change_animations(self, name):

        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 4

        if self.clock >= 100:

            self.animation_index+=1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0