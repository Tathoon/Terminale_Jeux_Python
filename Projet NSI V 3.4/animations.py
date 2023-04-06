

def Animations_Persos(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'../sprites/{name}.png')
        self.images = {
        "down" : self.image.get_image(0)
        "up" : self.image.get_image(32)
        "right" : self.image.get_image(64)
        "left" : self.image.get_image(96)
        }
        self.nb_images = 5


    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image


    def get_images(self, y):
    images_animations = []
        for i in range(0, self.nb_images):
            x=i*32
            image = self.get_image(x, y)
            images_animations.append(image)


    def change_animations(self, name):
        self.image = self.images[name]
        self.image.set_colorkey(0, 0, 0)



