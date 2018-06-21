import random

def game():
    board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
             (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
    user_active = True
    player = random.randint(0, 5), random.randint(0, 5)
    door = random.randint(0, 5), random.randint(0, 5)
    monster = random.randint(0, 5), random.randint(0, 5)
    print(player, door, monster)

    while user_active:
        board[board.index(player)] = 'Player'
        print(board)
        move = input('Enter your new position (num,num): ').split(',')
        print(move)
        # if board[board.index(move)] == door:
        #     print('You won!')
        # if board[board.index(move)] == monster:
        #     print('The monster is there! You\'ve lost!')
        # board[board.index(move)] = 'Player'
        # print(board)

game()
# draw the grid
# pick the random location for the player
# pick the random location for the exit door
# pick the random location for the monster
# draw player in the grid
# take input for movement
# move player
# check for win/loss
# clear the screen and redraw the grid

