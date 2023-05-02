class Quizz:
    def __init__(self, questions):
        self.questions = [Question(**q) for q in questions]
        self.question_actuelle = 0
        self.score = 0
        self.reponses = [Reponse(**r) for r in reponses]

    def poser_question(self, surface):
        self.questions[self.question_actuelle].poser(surface)
        pygame.display.flip()

    def verif_reponse(self, reponse_utilisateur):
        if self.questions[self.question_actuelle] == self.reponses[self.question-actuelle]:
            self.score += 1
            return True
        else:
            return False

    def switch_question(self):
        self.question_actuelle += 1
        if self.question_actuelle >= len(self.questions):
            return False
        else:
            return True


quizz = Quizz(questions)

run = False
clock = pygame.time.Clock()
while not run:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_1:
                reponse_utilisateur = quizz.questions[quizz.question_actuelle].options[0]
                if quizz.verif_reponse(reponse_utilisateur):
                    if not quizz.switch_question():
                        run = True


            elif evenement.key == pygame.K_2:
                reponse_utilisateur = quizz.questions[quizz.question]