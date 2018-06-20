import random


def hangman():
    words_list = ['car', 'tree', 'bottle', 'academy']
    random_word = list(random.choice(words_list))
    letters = []
    guesses = []
    indexes = []
    errors = 0
    # render guesses blank
    for x in range(0, len(random_word)):
        letters.append('_ ')

    while errors < 5:
        # ask for an answer
        print(''.join(letters))
        user_guess = input('Guess a letter: ')
        guesses.append(guesses)
        if user_guess not in random_word:
            errors += 1
        else:
            for i, letter in enumerate(random_word):
                if user_guess == letter:
                    indexes.append(i)
                    for x in indexes:
                        letters[x] = user_guess
    print(f'You\'ve lost... The word was: {random_word}')


hangman()