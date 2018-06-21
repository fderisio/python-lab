def play_again():
    start()


def start():
    user_guesses = 5
    print('I\'m thinking a number between 1-10')
    random_num = random.randint(1, 10)
    print('You have 5 chances')
    while user_guesses > 0:
        guess = int(input('Enter a number:'))
        if guess == random_num:
            print('You win!')
            break
        else:
            user_guesses -= 1
    else:
        print('You lose! The number was:', random_num)
    option = str(input('Would you like to play again(Y/N)?'))
    if option == 'n':
        print('Goodbye!')
    if option == 'y':
        return play_again()


start()
