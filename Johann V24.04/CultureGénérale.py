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
        self.options = [[],[],[],[]]
        self.questionsposees = []
        self.questionsmax = 10



    def partie(self.questions, self.reponses, questions_max):

        nb_bonnes_rep=0

        for question in range(self.questionsmax):
            choisir_question(self.questions)
            verif_reponse(self.questions, self.reponses)

        print("Partie Terminée !")
        print("Vous avez",nb_bonnes_rep,"bonnes réponses !")


    def choisir_question(self.questions):

        domaine = randint(0,3)
        num_question = randint(0,4)
        question_posee = self.questions[domaine][num_question]


    def verif_reponse(self.questions, self.reponses):

        self.reponse = input()
        if str(self.reponse)==str(self.reponses[domaine][num_question]) or str(self.reponses[domaine][num_question]) in str(self.reponse):
                nb_bonnes_rep+=1
                print("Bonne Réponse !")

            else:
                print("Mauvaise Réponse !")


    def end_quizz(self.questionsmax):

        if len(self.questionsposees) == self.questionsmax:
        print("Partie Terminée !")
        print("Vous avez",nb_bonnes_rep,"bonnes réponses !")