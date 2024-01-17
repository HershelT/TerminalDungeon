import time
import os
import sys
startScreen = """
     _______________________________________________________________________________________________ 
    |                                                                                               |
    |          _____    ______    _______       ____     ____                                       |
    |         |_  __|  | _____|  |   ___ ',    /    \   /    \                                      |
    |           | |    | _____   |  |___|  \  |    _ \_/ _    |   _________                         |
    |           | |    | _____|  |   _     /  |   | |   | |   |  |_________|                        |
    |           | |    | _____   |  | ',  '.  |   | |   | |   |                                     |
    |           |_|    |______|  |__|   |__|  |___| |___| |___|                                     |
    |                         ________     ______      ____     ____     ______                     |
    |                        /  ______|   /  __  \    /    \   /    \   | _____|                    |
    |                       |  |  ____   |  /__\  |  |    _ \_/ _    |  | _____                     |
    |                       |  | |__  |  |  |  |  |  |   | |   | |   |  | _____|                    |
    |                       |  |____/ /  |  |  |  |  |   | |   | |   |  | _____                     |
    |                        \_______/   |__|  |__|  |___| |___| |___|  |______|                    |
    |                                                                                               |
    |                                                                                               |
    |                                  Press "Enter" To Continue                                    |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |_______________________________________________________________________________________________|
"""
credits = """
                                    TERMINAL DUNGEON GAME:     
                                     -CREATED BY-HERSHEL THOMAS
                                     -TESTED BY JACOB THOMAS  
                                     -ART BY Hershel Thomas   
"""
settings = """
            Setting Screen Size Before Playing:
            -Make sure screen size is set to FULL SCREEN            
            -Zoom in or out by pressing down (ctrl) and (+ or -)      
            -Zoom in or out until edge of map ('|') is at the furthest right side of the screen
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

#prints given display to screen fast
def printScreen(screen, clear = True):
    if clear: os.system(clear_command)
    for row in screen:
        print(''.join(row))
#Adds text to overwrite over main screen
def addLinesToSreen(lines, screen, rowIndex, color='\033[m'):
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if j !=4:
                screen[len(screen) - rowIndex+i][j] = color + char + '\033[0m'
                
def createEmptyString(screenList : list):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString
#defining starting arrays
startScreenArray =createArrayinArray(startScreen)
creditsArray=createArrayinArray(credits)
settingsArray = createArrayinArray(settings)

printScreen(startScreenArray)
waitForInput('')

start_row_index = 10  # Replace with the index of the first row you want to copy to
addLinesToSreen(creditsArray, startScreenArray, start_row_index-4, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')

addLinesToSreen(createArrayinArray(createEmptyString(credits)), startScreenArray, start_row_index-4, '\033[0m')
addLinesToSreen(settingsArray, startScreenArray, start_row_index, '\033[1;31m')
addLinesToSreen(["          Press 'Enter' To Continue"], startScreenArray, 2, '\033[1;31m')
printScreen(startScreenArray)
waitForInput('')
time.sleep(1)
