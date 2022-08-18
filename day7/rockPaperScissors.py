from modules import space
import random as rand

while True:
    choices = ['rock','paper', 'scissors']

    computer = rand.choice(choices)
    player = None
    while player not in choices:
        player = input('rock, paper, or scissors? ').lower()

    space(20)
    computerPoints = 0
    playerPoints = 0

    if player == computer:
        print('tie')
    elif player == 'rock':
        if computer == 'scissors':
            print('player won!')
            playerPoints += 1
        else:
            print('computer won!')
            computerPoints += 1
    elif player == 'scissors':
        if computer == 'paper':
            print('player won!')
            playerPoints += 1
        else:
            print('computer won!')
            computerPoints += 1
    elif player == 'paper':
        if computer == 'rock':
            print('player won!')
            playerPoints += 1
        else:
            print('computer won!')
            computerPoints += 1


    print('player chose: '+player)
    print('computer chose: '+computer)

    print('player: ' + str(playerPoints) + ' points')
    print('computer: ' + str(computerPoints) + ' points')

    playAgain = input('would you like to play again? (yes/no): ').lower()

    if playAgain == 'no':
        break
print('bye!')


