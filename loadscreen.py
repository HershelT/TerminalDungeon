import time
import os
from termcolor import colored
startScreen = """
                                                                                                |
                                                                                                |
           _____    ______    _______       ____     ____                                       |
          |_  __|  | _____|  |   ___ ',    /    \   /    \                                      |
            | |    | _____   |  |___|  \  |    _ \_/ _    |   _________                         |
            | |    | _____|  |   _     /  |   | |   | |   |  |_________|                        |
            | |    | _____   |  | ',  '.  |   | |   | |   |                                     |
            |_|    |______|  |__|   |__|  |___| |___| |___|                                     |
                                                                                                |
                                                                                                |
                             ________      ______      ____     ____     ______                 |
                            |  ____  \    /  __  \    /    \   /    \   | _____|                |
                            | |____|  |  |  /__\  |  |    _ \_/ _    |  | _____                 |
                            |  ______/   |   __   |  |   | |   | |   |  | _____|                |
                            |  _____.-.  |  |  |  |  |   | |   | |   |  | _____                 |
                            |________/   |__|  |__|  |___| |___| |___|  |______|                |
                                                                                                |
                                                                                                |
                                                                                                |
                                                                                                |
                                                                                                |\033[1m\033[90m
                                    Press "Enter" To Continue                                   \033[0m|
                                                                                                |
                                                                                                |
                                                                                                |
                                                                                                |
"""
credits = """     
        CREATED BY-HERSHEL THOMAS
        TESTED BY JACOB THOMAS  
        ART BY Hershel Thomas   
"""

os.system('cls')
def waitForInput(char):
    user_input = None
    while (user_input != char):
        user_input = input()
row_index_to_color_red = 3

startScreenArray = startScreen.splitlines()
startScreenArray = [list(row) for row in startScreenArray]

creditsArray=credits.splitlines()
creditsArray = [list(row) for row in credits.splitlines()]

for row in startScreenArray:
    print(''.join(row))
waitForInput('')
os.system('cls')
num_rows = len(startScreenArray)
num_cols = len(startScreenArray[0])
start_row_index = num_rows - 5  # Replace with the index of the first row you want to copy to
def addLinesToSreen(lines, screen, rowIndex, color):
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            screen[rowIndex + i][j] = color + char + '\033[0m'
addLinesToSreen(creditsArray, startScreenArray, start_row_index, '\033[1m\033[90m')
for i,row in enumerate(startScreenArray):
    print(''.join(row))
waitForInput('')
time.sleep(1)

import adventureGame
# adventureGame.main()




































# import shutil

# terminal_width, _ = shutil.get_terminal_size()

# welcome_message = "Welcome to the game"
# giant_string = welcome_message.center(terminal_width)

# print(giant_string)
# #Make it so i can create a function that can display any message to any area of the board

# import curses
# import random
# import time
# import curses

# import curses

# def main(stdscr):
#     # Set up the screen
#     curses.curs_set(0)
#     # stdscr.nodelay(1)
#     stdscr.timeout(100)

#     # Define the array map
#     array_map = [
#         ['.', '.', '#', '.', '.'],
#         ['.', '#', '.', '#', '.'],
#         ['#', '.', '.', '.', '#'],
#         ['.', '#', '.', '#', '.'],
#         ['.', '.', '#', '.', '.'],
#     ]
#     # Print the array map
#     for i in range(len(array_map)):
#         for j in range(len(array_map[i])):
#             stdscr.addch(i, j, array_map[i][j])
#     # Define the character's initial position
#     x, y = 0, 0

#     while True:
#         # Erase the character at the old position
#         stdscr.addch(x, y, ' ')

#         # Get user input
#         key = stdscr.getch()

#         # Update the character's position based on the key
#         if key == ord('a') and x > 0:
#             y -= 1
#         elif key == ord('d') and x < len(array_map) - 1:
#             y += 1
#         elif key == ord('s') and y > 0:
#             x -= 1
#         elif key == ord('w') and y < len(array_map[0]) - 1:
#             x += 1

#         # Draw the character at the new position
#         stdscr.addch(x, y, '@')

#         # Refresh the screen
#         stdscr.refresh()

# curses.wrapper(main)
# # def main(stdscr):
# #     # Set up the screen
# #     curses.curs_set(0)
# #     stdscr.nodelay(1)
# #     stdscr.timeout(100)

# #     sh, sw = stdscr.getmaxyx()
# #     w = curses.newwin(sh, sw, 0, 0)

# #     # Set up the bird
# #     bird = '^'
# #     bx, by = sh // 2, sw // 4

# #     # Set up the pipes
# #     pipe_height = 3
# #     pipe_width = 3
# #     pipe_gap = 7
# #     pipe_pos = sw - 10

# #     # Set getch to non-blocking mode
# #     w.nodelay(True)

# #     while True:
# #         # Erase the bird at the old position
# #         w.addch(bx, by, ' ')

# #         # Draw the pipes
# #         if pipe_pos + pipe_width < 0:
# #             pipe_pos = sw - 10
# #             pipe_height = random.randint(3, sh // 2)  # Randomly determine the height of the pipes
# #         else:
# #             pipe_pos -= 1

# #         for i in range(pipe_height):
# #             if i < sh and pipe_pos < sw and pipe_pos >= 0:  # Check if the pipe is within the screen
# #                 w.addch(i, pipe_pos, '#')
# #             if sh - i - 1 < sh and pipe_pos < sw and pipe_pos >= 0:  # Check if the pipe is within the screen
# #                 w.addch(sh - i - 1, pipe_pos, '#')

# #         # Check for collision
# #         if bx in [0, sh - 1] or w.inch(bx, by + 1) != ord(' '):
# #             break

# #         # Move the bird
# #         key = w.getch()
# #         if key != -1 and key == ord('w'):
# #             bx = max(0, bx - 2)  # Move up faster, but don't go off the screen
# #         else:
# #             bx = min(sh - 1, bx + 1)  # Fall down automatically, but don't go off the screen

# #         # Draw the bird at the new position
# #         if bx < sh and by < sw:  # Check if the bird is within the screen
# #             w.addch(bx, by, bird)

# #         # Refresh the screen
# #         w.refresh()

# #         # Slow down the game
# #         time.sleep(0.1)

# curses.wrapper(main)