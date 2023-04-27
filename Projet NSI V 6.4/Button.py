import pygame

class button:
    """
    Classe qui permet

    ### attributs:
        - bla : blala

    ### méthodes:
        - bla -> blabla
    """

    def __init__(self, chemin,dim_x,dim_y,pos_x,pos_y):
        self.image = pygame.image.load(chemin)
        self.image = pygame.transform.scale(self.image,(dim_x, dim_y))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x,pos_y)