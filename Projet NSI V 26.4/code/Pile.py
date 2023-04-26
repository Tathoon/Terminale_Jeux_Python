class pile:

    def __init__(self):

        self.elements = []

    def empiler(self, valeur):

        self.elements.append(valeur)

    def depiler(self):

        if self.taille() == 1:
            return self.tete()
        elif self.elements != []:
            return self.elements.pop()

    def tete(self):
        
        return self.elements[-1]

    def est_vide(self):

        return self.elements == []

    def taille(self):

        return len(self.elements)
