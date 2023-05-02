print("Bienvenue au questionnaire à choix multiples !")

# Définition des questions et des options
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "options": ["Paris", "Londres", "Madrid", "Berlin"],
        "reponse": "Paris"
    },
    {
        "question": "Quel est le plus grand fleuve d'Afrique ?",
        "options": ["Nil", "Congo", "Zambèze", "Niger"],
        "reponse": "Nil"
    },
    {
        "question": "Quel est le plus grand désert du monde ?",
        "options": ["Sahara", "Gobi", "Atacama", "Antarctique"],
        "reponse": "Sahara"
    }
]

# Fonction pour poser une question et vérifier la réponse
def poser_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    reponse_utilisateur = input("Votre réponse : ")
    return reponse_utilisateur == question["reponse"]

# Boucle pour poser toutes les questions
score = 0
for question in questions:
    if poser_question(question):
        print("Bonne réponse !")
        score += 1
    else:
        print("Mauvaise réponse...")

# Affichage du score final
print(f"Votre score final est de {score}/{len(questions)}")
