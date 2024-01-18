import time
import os
from AsciiAnimations import *
from keyboardListener import *


clear_command = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_command)

def waitForInput(char):
    user_input = None
    while (user_input != char):
        user_input = input()
#turns text to 2d arrays
def createArrayinArray(text: str):
    rows = text.splitlines()
    # If the first line is empty, skip it
    if rows and not rows[0]:
        rows = rows[1:]
    # If the last line is empty, skip it
    if rows and not rows[-1]:
        rows = rows[:-1]
    newText = [list(row) for row in rows]
    return newText

#prints given display to screen fast
def printScreen(screen, clear = True):
    if clear: os.system(clear_command)
    for row in screen:
        print(''.join(row),flush=True)

#Adds text to overwrite over main screen with a specific row from most bottom of text being rowIndex from bottom of screen and column from left
def addLinesToSreen(lines, screen, rowIndex=0, colIndex=0, color='\033[m'):
    newLines = createArrayinArray(lines)
    for i, row in enumerate(newLines):
        for j, char in enumerate(row):
            screen[len(screen) - (len(newLines)+rowIndex)+i][colIndex+j] = color + char + '\033[0m'
#Use this after addlinestotext to erase a line written on previously
def createEmptyString(screenList : list):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString

#Moves a character left or right (entity, screen it should be on,row want to be on, column want to be on, how much to move by, color if want)

def moveLeftorRight(entity:str,fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m'):
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    keyboard.Controller().release(keyboard.Key.enter)
    longest_row=len(max(createArrayinArray(entity), key=len))
    addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
    printScreen(fullScreen)
    while not key_listener.is_enter_pressed():
        if key_listener.is_right_arrow_pressed() and (colIndex+longest_row)<(len(fullScreen[2])-1):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            colIndex += stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_left_arrow_pressed() and (colIndex>5):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            colIndex -= stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_up_arrow_pressed() and (rowIndex+len(entity.split('\n'))-1)<(len(fullScreen)):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            rowIndex += jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_down_arrow_pressed() and (rowIndex>0):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            rowIndex -= jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
    listener.stop()
    del key_listener

#defining full screens
startScreenArray =createArrayinArray(startScreen)
clearScreenArray= createArrayinArray(clearScreen)

#defining things to add (deprecated)
# creditsArray=createArrayinArray(credits)
# settingsArray = createArrayinArray(settings)
# ManWalkingArray = createArrayinArray(ManWalking)

#initlizes the startscreen
printScreen(startScreenArray)
waitForInput('')

#Add credits to main screen
addLinesToSreen(credits, startScreenArray, 1, 36, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')
#Add settings index to allow users to set their screen size
addLinesToSreen(createEmptyString(credits), startScreenArray, 1, 36, '\033[0m')
addLinesToSreen(settings, startScreenArray, 3, 12, '\033[1;31m')
addLinesToSreen("Press 'Enter' To Continue", startScreenArray, 1, colIndex=8, color='\033[1;31m')
printScreen(startScreenArray)
waitForInput('')


#Charcter appears to move
manCol = 50
# os.system(clear_command)
# print(len(ManWalking.split('\n')), len(createArrayinArray(clearScreen)))
# time.sleep(5)
# lenghtManWalking = len(ManWalking.split('\n')[3])
addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[90m')
# addLinesToSreen(ManWalking, clearScreenArray, rowIndex=0, colIndex=manCol, color='\033[0m')
# printScreen(clearScreenArray)
# print(manCol, lenghtManWalking, len(clearScreenArray[2]))
# time.sleep(5)
moveLeftorRight(ManWalking, clearScreenArray, 1, manCol,stepMoveBy=5,jumpMoveBy=3,color='\033[0m')

clearScreenArray = createArrayinArray(clearScreen)

# addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[90m')
# addLinesToSreen(manTwo, clearScreenArray, rowIndex=10, colIndex=30, color='\033[90m')
# printScreen(clearScreenArray)
# moveLeftorRight(manTwo, clearScreenArray, 10, 30,stepMoveBy=1,jumpMoveBy=1,color='\033[0m')

#charcter moves right


# waitForInput('')


time.sleep(1)

