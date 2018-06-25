import os
import random

# draw the grid

# draw the player in the grid

# clear the screen and redraw the grid

GRID = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw_grid():


def get_random_location():
    x, y = random.sample(range(5), k = 2)
    return [x, y]

# pick random location for the player, the exit door and the monster
def get_locations():
    door, player, monster = get_random_location(), get_random_location(), get_random_location()
    return door, player, monster

def move_player(player, move):
    if move == 'UP':
        player[1] -= 1
    elif move == 'DOWN':
        player[1] += 1
    elif move == 'LEFT':
        player[0] -= 1
    elif move == 'RIGHT':
        player[0] += 1
    return player

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[1] <= 0:
        del moves[moves.index('UP')]
    if player[1] >= 4:
        del moves[moves.index('DOWN')]
    if player[0] <= 0:
        del moves[moves.index('LEFT')]
    if player[0] >= 4:
        del moves[moves.index('RIGHT')]
    return moves

game_setup = get_locations()
door = None
player = None
monster = None

while door == player or monster == player or door == monster:
    game_setup = get_locations()
    door = game_setup[0]
    player = game_setup[1]
    monster = game_setup[2]

moves = get_moves(player)

while True:
    clear_screen()
    print('Welcome to the Dungeon!')
    print('You\'re currently in room {}'.format(player))
    print('You can move {}.'.format(moves))
    # print('Door {}, Monster {}'.format(door, monster))
    print('Enter \'QUIT\' to quit.')

    # take input for movement
    move = input('> ').upper()

    if move == 'QUIT':
        break
    # move the player, unless invalid move (past edges of grid)
    elif move in moves:
        player = move_player(player, move)
        moves = get_moves(player)
        # check for win or loss
        if player == door:
            print('Win!')
            break
        elif player == monster:
            print('Loss!')
            break
        else:
            continue
    else:
        print('Invalid move!')
        input('Press any key!')
