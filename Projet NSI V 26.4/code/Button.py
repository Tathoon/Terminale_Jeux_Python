import pygame

class button:
    """
    Classe qui permet de créer un bouton visuel

    ### attributs:
        - image : image visuelle du bouton adapté au dimension de la fenêtre

    ### méthodes:
        - Pas de méthodes -> Classe ne servant qu'à la création d'objet button
    """

    def __init__(self, chemin, dim_x, dim_y, pos_x, pos_y):
        self.image = pygame.image.load(chemin)
        self.image = pygame.transform.scale(self.image,(dim_x, dim_y))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

class descriptions:
    def __init__(self, chemin, dim_x, dim_y, pos_x, pos_y):
        self.image = pygame.image.load(chemin)
        self.image = pygame.transform.scale(self.image,(dim_x, dim_y))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)