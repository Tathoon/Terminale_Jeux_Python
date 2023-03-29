"Tableau des questions-Réponses"

Questions=[["En quelle année se sont déroulés les JOs de Pékin ?" , "Combien de sports sont représentés aux JOs ?" , "Qui a gagné le tournoi de Wimbledon en 2014 ?"	, "Qui a gagné la coupe de football de 1998 ?" , "Au basket, combien de point(s) rapporte(nt) un dunk ?"], 
           ["Quelle figure de style consiste à coller deux mots de sens contraires dans une phrase ?", "Quel grand dramaturge est l'auteur de la pièce 'Le Malade Imaginaire ?'", "Quel célèbre écrivain romantique du XVIIIe est Ã  l'origine du receuil 'Les Contemplations' ?", "Dans quel registre figure l'expression de la pitié en littérature ?", "De quel mot français utilisé généralement durant la période moyennageuse provient le terme chaussure ?"],
           ["Combien de pays sont membres de l'UE actuellement ?" , "Quelle est la capitale du Guatemala?"	, "De quel pays Jakarta est-elle la capitale ?", "Quel est le plus long fleuve français ?", "Combien y-a-t-il de continents (hors Antartique) ?"],
           ["En quelle année s'est produit la très célèbre bataille de Waterloo ?", "En quelle année s'est produite la déclaration d'indépendance des Eu ?", "Quel grand empereur romain a vaincu Vercingétorix en 52 av. J-C ?", "Quel autre nom très célèbre donne-t-on à la traite négrière entre l'Europe, l'Afrique noire et l'Amérique datant du XVIIIe siècle ?" , "En quelle année s'est déroulée la chute du mur de Berlin ?"]]

Reponses=[["2008", "33", "Djokovic", "France", "2"], ["oxymore", "Molière", "Hugo", "pathétique", "chausse"], ["27", "Guatemala", "Indonésie", "Loire", "6"], ["1815", "1783", "Jules César", "commerce triangulaire", "1989"]]



"Fonctions"

from random import randint

  
def partie(Questions, Reponses, questions_max):
    nb_bonnes_rep=0
    questions_posees=[]
    for question in range(questions_max):
        domaine=randint(0,3)
        num_question=randint(0,4)
        question_posee=Questions[domaine][num_question]
        if question_posee in questions_posees:
            domaine = randint(0,3)
            num_question=randint(0,4)
            question_posee=Questions[domaine][num_question]
        print(question_posee)
        questions_posees.append(question_posee)
        reponse=input()
        if str(reponse)==str(Reponses[domaine][num_question]) or str(Reponses[domaine][num_question]) in str(reponse):
            nb_bonnes_rep+=1
            print("Bonne Réponse !")
        else:
            print("Mauvaise Réponse !")
    print("Partie Terminée !")
    print("Vous avez",nb_bonnes_rep,"bonnes rÃ©ponses !")

partie(Questions, Reponses, 10)
