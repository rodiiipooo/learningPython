questions = {'Is climate change real?': 'A',
             'Does estrella have a big booty?': 'A',
             'Is rod awesome at chess?': 'A',
             'how many questions are in this quiz?': 'D'}

options = [['A. yes', 'B. no', 'C. maybe', 'D. in hell'],
           ['A. yes', 'B. no', 'C. maybe', 'D. in hell'],
           ['A. yes', 'B. no', 'C. maybe', 'D. in hell'],
           ['A. 1', 'B. 2', 'C. 3', 'D. 4']]

def quizgame():
    while True:
        answers = []
        score = 0
        questionNumber = 1
        for key in questions:
            print('________________________')
            print('QUESTION #'+str(questionNumber))
            print(key)
            for i in options[questionNumber-1]:
                print(i)
            answer = (input('enter (A, B, C, or D): ').upper())
            answers.append(answer)

            if answers[questionNumber-1] == questions.get(key):
                score += 1


            questionNumber += 1
        print('you scored a ' + str(score / len(answers) *100) + '% !')
        playAgain = input('play again? (y/n)')
        if playAgain != 'y':
            break

quizgame()
