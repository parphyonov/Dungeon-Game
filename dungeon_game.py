import os
import random
import time

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

# def draw_grid():

def get_random_location():
    x, y = random.sample(range(5), k = 2)
    return [x, y]

# pick random location for the player, the exit door and the monster
def get_locations():
    # door, player, monster = get_random_location(), get_random_location(), get_random_location()
    # return door, player, monster
    return random.sample(GRID, 3)

def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'UP':
        y -= 1
    elif move == 'DOWN':
        y += 1
    # player = x, y
    # return player
    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if x <= 0:
        moves.remove('LEFT')
    if x >= 4:
        moves.remove('RIGHT')
    if y <= 0:
        moves.remove('UP')
    if y >= 4:
        moves.remove('DOWN')
    return moves

# game_setup = get_locations()
# door = list(game_setup[0])
# player = list(game_setup[1])
# monster = list(game_setup[2])

# while door == player or monster == player or door == monster:
#     game_setup = get_locations()
#     door = game_setup[0]
#     player = game_setup[1]
#     monster = game_setup[2]

def draw_map(player):
    print(' _' * 5)
    tile = '|{}'
    for cell in GRID:
        x, y = cell
        if x < 4:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end = line_end)


def game_loop():
    door, player, monster = get_locations()
    while True:
        valid_moves = get_moves(player)
        draw_map(player)
        print('You\'re currently in room {}'.format(player))
        print('You can move {}.'.format(', '.join(valid_moves).lower()))
        # print('Door {}, Monster {}'.format(door, monster))
        print('Enter \'QUIT\' to quit.')

        # take input for movement
        move = input('> ').upper()

        if move == 'QUIT':
            break
        # move the player, unless invalid move (past edges of grid)
        elif move in valid_moves:
            player = move_player(player, move)
            clear_screen()
            # check for win or loss
            if player == door:
                print('Win!')
                time.sleep(3)
                clear_screen()
                break
            elif player == monster:
                print('Loss!')
                time.sleep(3)
                clear_screen()
                break
            else:
                continue
        else:
            input('Invalid move!')
        clear_screen()


clear_screen()
print('Welcome to the Dungeon!')
input('Press \'RETURN\' to start!')
clear_screen()
game_loop()
