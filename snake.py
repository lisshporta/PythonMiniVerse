# if used in a Windows operating system, switch from os.system('clear') to os.system('cls')
# pip install pytimedinput
# pip install colorama
# python3 snake.py

from pytimedinput import timedInput
from random import randint
import os
from colorama import Fore, init

def print_field():
    snake_length = len(snake_body)
    for cell in CELLS:
        if cell in snake_body:
            if cell == snake_body[0]:  # Snake head
                print(Fore.GREEN + 'O', end='')
                snake_length -= 1
            else:  # Snake body
                print(Fore.GREEN + 'o', end='')
                snake_length -= 1
        elif cell == apple_pos:
            print(Fore.RED + 'a', end='')
        elif cell[1] in (0, FIELD_HEIGHT - 1) or cell[0] in (0, FIELD_WIDTH - 1):
            print(Fore.CYAN + '#', end='')
        else:
            print(' ', end='')

        if cell[0] == FIELD_WIDTH - 1:
            print('')

def update_snake():
	global eaten
	new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
	snake_body.insert(0,new_head)
	if not eaten:
		snake_body.pop(-1)
	eaten = False

def apple_collision():
	global apple_pos, eaten

	if snake_body[0] == apple_pos:
		apple_pos = place_apple()
		eaten = True

def place_apple():
	col = randint(1,FIELD_WIDTH - 2)
	row = randint(1,FIELD_HEIGHT - 2)
	while (col, row) in snake_body:
		col = randint(1,FIELD_WIDTH - 2)
		row = randint(1,FIELD_HEIGHT - 2)
	return (col,row)

init(autoreset=True)

# settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col,row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]

# snake
snake_body = [
    (5,FIELD_HEIGHT // 2),
    (4,FIELD_HEIGHT // 2),
    (3,FIELD_HEIGHT // 2)]
DIRECTIONS = {'left':(-1,0),'right': (1,0),'up': (0,-1),'down': (0,1)}
direction = DIRECTIONS['right']
eaten = False
apple_pos = place_apple()

# difficulty levels
DIFFICULTY_LEVELS = {
    1: 0.3,
    2: 0.2,
    3: 0.1,
    4: 0.05
}

# get difficulty level
while True:
    try:
        difficulty = int(input("Select difficulty level (1-4): "))
        if difficulty in DIFFICULTY_LEVELS:
            break
        else:
            print("Invalid difficulty level. Please select a level from 1 to 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

timeout = DIFFICULTY_LEVELS[difficulty]

while True:
    # clear field
    os.system('clear')

    # draw field
    print_field()

    # get input
    txt, _ = timedInput('', timeout=timeout)
    match txt:
        case 'w':
            direction = DIRECTIONS['up']
        case 'a':
            direction = DIRECTIONS['left']
        case 's':
            direction = DIRECTIONS['down']
        case 'd':
            direction = DIRECTIONS['right']
        case 'q':
            os.system('clear')
            break

    # update game
    update_snake()
    apple_collision()

    # check death
    if snake_body[0][1] in (0, FIELD_HEIGHT - 1) or \
       snake_body[0][0] in (0,FIELD_WIDTH - 1) or \
       snake_body[0] in snake_body[1:]:
        os.system('clear')
        break

print(f"The length of the snake was: {len(snake_body)}")
