import time
import os
import sys
startScreen = """
 _______________________________________________________________________________________________
|                                                                                               |123
|                                                                                               |123
|          _____    ______    _______       ____     ____                                       |123
|         |_  __|  | _____|  |   ___ ',    /    \   /    \                                      |123
|           | |    | _____   |  |___|  \  |    _ \_/ _    |   _________                         |123
|           | |    | _____|  |   _     /  |   | |   | |   |  |_________|                        |123
|           | |    | _____   |  | ',  '.  |   | |   | |   |                                     |123
|           |_|    |______|  |__|   |__|  |___| |___| |___|                                     |123
|                                                                                               |123
|                                                                                               |123
|                         ________     ______      ____     ____     ______                     |123
|                        /  ______|   /  __  \    /    \   /    \   | _____|                    |123
|                       |  |  ____   |  /__\  |  |    _ \_/ _    |  | _____                     |123
|                       |  | |__  |  |  |  |  |  |   | |   | |   |  | _____|                    |123
|                       |  |____/ /  |  |  |  |  |   | |   | |   |  | _____                     |123
|                        \_______/   |__|  |__|  |___| |___| |___|  |______|                    |123
|                                                                                               |123
|                                                                                               |123
|                                  Press "Enter" To Continue                                    |123
|                                                                                               |123
|                                                                                               |123
|                                                                                               |123
|                                                                                               |123
|                                                                                               |123
|                                                                                               |123
|_______________________________________________________________________________________________|123
"""
credits = """
        TERMINAL DUNGEON GAME:     
         -CREATED BY-HERSHEL THOMAS
         -TESTED BY JACOB THOMAS  
         -ART BY Hershel Thomas   
"""
settings = """
        SETTINGS Before Playing:
        -Make Sure Screen size is correct size and set to full screen width and height 
        -Can enlarge the screen using zoom (ctrl - or +)       
        -enlarge or decrease screen size until number '3' 
        -is at the furthest right side of the screen
        -type in '/clear' at any point during game play to reset screen if messy
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
            if j !=0:
                screen[len(screen) - rowIndex+i][j] = color + char + '\033[0m'
                
def createEmptyString(screenList : list):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString

printScreen(startScreenArray)
waitForInput('')



os.system(clear_command)
num_rows = len(startScreenArray)
num_cols = len(startScreenArray[0])

start_row_index = 10  # Replace with the index of the first row you want to copy to
addLinesToSreen(creditsArray, startScreenArray, start_row_index, '\033[1m\033[90m')

printScreen(startScreenArray)
waitForInput('')
settingsArray = createArrayinArray(settings)

addLinesToSreen(createArrayinArray(createEmptyString(credits)), startScreenArray, start_row_index, '\033[0m')
addLinesToSreen(settingsArray, startScreenArray, start_row_index, '\033[1;31m')
addLinesToSreen(["    Press 'Enter' To Continue"], startScreenArray, 2, '\033[1;31m')
os.system(clear_command)    
printScreen(startScreenArray)
waitForInput('')
os.system(clear_command)

printScreen(startScreenArray)
time.sleep(1)
