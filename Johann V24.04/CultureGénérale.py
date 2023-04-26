class Quizz:

    def __init__():




        self.question = question
        self.questions = [
            ["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"],
           ["Quelle figure de style consiste à coller deux mots de sens contraires dans une phrase ?", "Quel grand dramaturge est l'auteur de la pièce 'Le Malade Imaginaire ?'", "Quel célèbre écrivain romantique du XVIIIe est Ã  l'origine du receuil 'Les Contemplations' ?", "Dans quel registre figure l'expression de la pitié en littérature ?", "De quel mot français utilisé généralement durant la période moyennageuse provient le terme chaussure ?"],
           ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve français ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
           ["En quelle année s'est produit la très célèbre bataille de Waterloo ?", "En quelle année s'est produite la déclaration d'indépendance des Eu ?", "Quel grand empereur romain a vaincu Vercingétorix en 52 av. J-C ?", "Quel autre nom très célèbre donne-t-on à la traite négrière entre l'Europe, l'Afrique noire et l'Amérique datant du XVIIIe siècle ?" , "En quelle année s'est déroulée la chute du mur de Berlin ?"]]

        self.reponse = reponse
        self.reponses = [["2008", "33", "Djokovic", "France", "2"],
        ["oxymore", "Molière", "Hugo", "pathétique", "chausse"],
        ["27", "Guatemala", "Indonésie", "Loire", "6"],
        ["1815", "1783", "Jules César", "commerce triangulaire", "1989"]]
        self.questionsposees = []
        self.questionsmax = 10
        self.ap = pygame.screen(screen.get_size)
        self.ap = pygame.image.load("quizz.png").convert()
        self.score = 0
        self.question_actuelle = 0



    def choisir_question(self):

        domaine = randint(0,3)
        num_question = randint(0,4)
        question_posee = self.questions[domaine][num_question]


    def verif_reponse(self):

        self.reponse = input()
        if str(self.reponse)==str(self.reponses[domaine][num_question]) or str(self.reponses[domaine][num_question]) in str(self.reponse):
                nb_bonnes_rep+=1
                print("Bonne Réponse !")

            else:
                print("Mauvaise Réponse !")

        y=100
        souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()
        if clic[0] == 1: #on vérifie si on fait clic gauche
        if y > souris[1] > y - 50: #on vérifie les coordonnées de la position du curseur
                if self.reponse[self.question_actuelle][0] == self.reponses[question_actuelle]: #on vérifie si la réponse est juste
                    self.score += 1 #on augmente le score
                self.question_actuelle += 1 #on change de question


    def affiche_questions(self):

        police = pygame.font.Font(None, taille_police)
        question_texte = police.render(questions[question_actuelle], True, (0, 0, 0))
        ecran.blit(question_texte, (50, 50))


    def affiche_reponses(self):
        y = 100
        for reponse in reponses[question_actuelle]:
            reponse_texte = police.render(reponse, True, (0, 0, 0))
            ecran.blit(reponse_texte, (100, y))
            y += 50


    def affiche_score(self):
        self.score = police.render("Score: " + str(self.score), True, (255, 0, 0))
        self.screen.blit(self.score, (50, 50))


    def end_quizz(self):

        if len(self.questionsposees) == self.questionsmax:
        print("Partie Terminée !")
        print("Vous avez",nb_bonnes_rep,"bonnes réponses !")


    def partie(self):

        for question in range(self.questionsmax):
            choisir_question()
            affiche_questions()
            affiche_reponses()
            verif_reponse()
            affiche_score()
        end_quizz()
