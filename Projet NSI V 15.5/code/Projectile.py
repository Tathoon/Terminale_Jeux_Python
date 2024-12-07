import pygame

class projectile(pygame.sprite.Sprite):

    def __init__(self, pnj):
        super().__init__()
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("Projet NSI V 15.5/assets/projectile/bombe.png"),(85,85))
        self.rect = self.image.get_rect()
        self.rect.x = pnj.type.rect.x + 120
        self.rect.y = pnj.type.rect.y + 120
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) # considère l'image par son centre pour une rotation plus réaliste

    def remove(self, pnj):
        pnj.all_projectiles.remove(self)

    def move(self, mainScreen, pnj):
        self.rect.x += self.speed
        self.rotate()

        # verifier si le projectile entre en collision avec un monstre
        for monster in pnj.check_collision(self, pnj.all_monster):
            monster.damage(pnj, mainScreen)
            self.remove(pnj)

        # verifier si le projectiles n'est plus sur l'écran
        if self.rect.x > mainScreen.get_width():
            self.remove(pnj)