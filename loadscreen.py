import time
import os
import sys
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
                          ________     ______      ____     ____     ______                     |
                         /  ______|   /  __  \    /    \   /    \   | _____|                    |
                        |  |  ____   |  /__\  |  |    _ \_/ _    |  | _____                     |
                        |  | |__  |  |  |  |  |  |   | |   | |   |  | _____|                    |
                        |  |____/ /  |  |  |  |  |   | |   | |   |  | _____                     |
                         \_______/   |__|  |__|  |___| |___| |___|  |______|                    |
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
        TERMINAL DUNGEON GAME:     
         -CREATED BY-HERSHEL THOMAS
         -TESTED BY JACOB THOMAS  
         -ART BY Hershel Thomas   

"""

GameLoading = """
                         Game Loading
        ██████╗░░█████╗░██████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░

"""
clear_command = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_command)
def waitForInput(char):
    user_input = None
    while (user_input != char):
        user_input = input()
row_index_to_color_red = 3

def createArrayinArray(text: str):
    # text = text.splitlines()
    text = [list(row) for row in text.splitlines()]
    return text
#turns text to 2d arrays
startScreenArray =createArrayinArray(startScreen)
creditsArray=createArrayinArray(credits)

#prints given display to screen fast
def printScreen(screen):
    for row in screen:
        print(''.join(row))
#Adds text to overwrite over main screen
def addLinesToSreen(lines, screen, rowIndex, color='\033[m'):
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            screen[rowIndex + i][j] = color + char + '\033[0m'
def createEmptyString(screenList : list):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString

printScreen(startScreenArray)
waitForInput('')



os.system(clear_command)
num_rows = len(startScreenArray)
num_cols = len(startScreenArray[0])

start_row_index = num_rows - 5  # Replace with the index of the first row you want to copy to
addLinesToSreen(creditsArray, startScreenArray, start_row_index, '\033[1m\033[90m')

printScreen(startScreenArray)
waitForInput('')
addLinesToSreen(createArrayinArray(createEmptyString(credits)), startScreenArray, start_row_index, '\033[0m')

os.system(clear_command)
printScreen(startScreenArray)
time.sleep(1)
