import time
import os, sys
from AsciiAnimations import *
from keyboardListener import *

#import image processor
sys.path.insert(0, 'ImageReader')
from ImageReader import *

clear_command = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_command)

def waitForInput(char):
    user_input = None
    while (user_input != char):
        user_input = input()

#prints given display to screen fast
def printScreen(screen, clear = True):
    if clear: os.system(clear_command)
    for row in screen:
        print(''.join(row),flush=True)
    sys.stdout.flush()
    # print('\033[?25h', end='')

#Adds text to overwrite over main screen with a specific row from most bottom of text being rowIndex from bottom of screen and column from left
def addLinesToSreen(lines, screen, rowIndex=0, colIndex=0, color='\033[m', createArray = True):
    if createArray: newLines = createArrayinArray(lines)
    else: newLines= lines
    for i, row in enumerate(newLines):
        for j, char in enumerate(row):
            screen[len(screen) - (len(newLines)+rowIndex)+i][colIndex+j] = color + char.replace('\033[0m', '') + '\033[0m'
#Use this after addlinestotext to erase a line written on previously
def convert_2d_array_to_empty_strings(array_2d):
    return [[' ' for _ in sublist] for sublist in array_2d]
def createEmptyString(screenList : str):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString

#Moves a character left or right (entity, screen it should be on,row want to be on, column want to be on, how much to move by, color if want)
def check_keys():
    while (not key_listener.is_enter_pressed()):
        key_listener.check_keys()
        time.sleep(0.1)
    keyboard.Controller().release(keyboard.Key.enter)
def moveLeftorRight(entity,fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m', ArrayCreate = True):
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    keyboard.Controller().release(keyboard.Key.enter)
    if ArrayCreate:
        longest_row=len(max(createArrayinArray(entity), key=len))
        howManyRows = len(createArrayinArray(entity))
        emptyString = createEmptyString(entity)
    else: 
        longest_row=len(max(entity, key=len))
        howManyRows = len(entity)
        emptyString = convert_2d_array_to_empty_strings(entity)
    addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color, ArrayCreate)
    printScreen(fullScreen)
    
    while not key_listener.is_enter_pressed():
        if key_listener.is_right_arrow_pressed() and (colIndex+longest_row+stepMoveBy)<=(len(fullScreen[2])-1):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m', createArray=ArrayCreate)
            colIndex += stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_left_arrow_pressed() and (colIndex-stepMoveBy>=5):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            colIndex -= stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_up_arrow_pressed() and (rowIndex+howManyRows+jumpMoveBy)<(len(fullScreen)):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex += jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_down_arrow_pressed() and (rowIndex-jumpMoveBy>0):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex -= jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
    listener.stop()
    del key_listener

#hides the cursor in the begining from screen
print('\033[?25l', end='')


#defining full screens
startScreenArray =createArrayinArray(startScreen)
clearScreenArray= createArrayinArray(clearScreen)

#defining things to add (deprecated)
# creditsArray=createArrayinArray(credits)
# settingsArray = createArrayinArray(settings)
# ManWalkingArray = createArrayinArray(ManWalking)

#initlizes the startscreen
addLinesToSreen(pressEnter, startScreenArray, 8, 36, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')


#Add credits to main screen
addLinesToSreen(credits, startScreenArray, 1, 36, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')


#Add settings index and erase previously written extra writings to allow users to set their screen size
addLinesToSreen(createEmptyString(credits), startScreenArray, 1, 36, '\033[0m')
addLinesToSreen(createEmptyString(pressEnter), startScreenArray, 8, 36, '\033[1m\033[90m')
addLinesToSreen(settings, startScreenArray, 3, 12, '\033[1;31m')
addLinesToSreen("Press {Bb}'Enter'{0} To Continue", startScreenArray, 1, colIndex=8, color='\033[1;31m')
printScreen(startScreenArray)
waitForInput('')

# moveLeftorRight(convertedHuman, clearScreenArray, 1, 5,stepMoveBy=4,jumpMoveBy=1,color='\033[0m',ArrayCreate=False)
# clearScreenArray =createArrayinArray(clearScreen)
def DrawLeftRight(idle, right, left, jump, down, fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m', ArrayCreate = True):
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    keyboard.Controller().release(keyboard.Key.enter)
    if ArrayCreate:
        longest_row=len(max(createArrayinArray(idle), key=len))
        howManyRows = len(createArrayinArray(idle))
        emptyString = createEmptyString(idle)
    else: 
        longest_row=len(max(idle, key=len))
        howManyRows = len(idle)
        emptyString = convert_2d_array_to_empty_strings(idle)
    addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color, ArrayCreate)
    printScreen(fullScreen)
    currentDrawing = idle
    while not key_listener.is_enter_pressed():
        if key_listener.is_right_arrow_pressed() and (colIndex+longest_row+stepMoveBy)<=(len(fullScreen[2])-1):
            if currentDrawing != right and currentDrawing != idle:
                addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                printScreen(fullScreen)
                time.sleep(0.3)
            currentDrawing = right
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m', createArray=ArrayCreate)
            colIndex += stepMoveBy
            addLinesToSreen(currentDrawing, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            
            

        elif key_listener.is_left_arrow_pressed() and (colIndex-stepMoveBy>=5):
            if currentDrawing != left and currentDrawing != idle:
                addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                printScreen(fullScreen)
                time.sleep(0.3)
            currentDrawing = left
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            colIndex -= stepMoveBy
            addLinesToSreen(currentDrawing, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            
            
        elif key_listener.is_up_arrow_pressed() and (rowIndex+howManyRows+jumpMoveBy)<(len(fullScreen)):
            addLinesToSreen(down, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.3)
            addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.3)
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex += jumpMoveBy
            addLinesToSreen(jump, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.3)
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex -= jumpMoveBy
            addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            currentDrawing = idle
        elif key_listener.is_down_arrow_pressed() and currentDrawing != down:# and (rowIndex-jumpMoveBy>0):
            
            addLinesToSreen(down, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            # rowIndex -= jumpMoveBy
            # addLinesToSreen(idle, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            # key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            currentDrawing = down
    listener.stop()
    del key_listener
DrawLeftRight(convertedHumanIdle, convertedHumanWalkRight, convertedHumanWalkLeft, convertedHumanJump, convertedHumanDown, clearScreenArray, 1, 5,stepMoveBy=4,jumpMoveBy=4,color='\033[0m',ArrayCreate=False)



#set charcter position and establish movement
manCol = 50+2
addLinesToSreen(characterDesigner, clearScreenArray, 16, 25, color=bright_blue)
addLinesToSreen("Choose Your {Gb}Hair{0} color, \nPress 'Enter' to go to next body pary", clearScreenArray, 14, 25, color=bright_yellow)
addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False)
addLinesToSreen(convertedHeart, clearScreenArray, 1, 67, color='\033[0m',createArray=False)
# addLinesToSreen(heartClass.getPixelizedEntity(), clearScreenArray, 8, 50, color='\033[0m',createArray=False)

printScreen(clearScreenArray)


user_input = None

#selects hair color
pattern = ",.,"
key_actions = {
    "'r'": lambda: [ManWalkingClass.replaceString(pattern,pattern, red),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'g'": lambda: [ManWalkingClass.replaceString(pattern,pattern, green),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'b'": lambda: [ManWalkingClass.replaceString(pattern,pattern, blue),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'y'": lambda: [ManWalkingClass.replaceString(pattern,pattern, yellow),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'m'": lambda: [ManWalkingClass.replaceString(pattern,pattern, magenta),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'c'": lambda: [ManWalkingClass.replaceString(pattern,pattern, cyan),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'w'": lambda: [ManWalkingClass.replaceString(pattern,pattern, white),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'0'": lambda: [ManWalkingClass.replaceString(pattern,pattern, reset),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 87, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'\\n'": lambda: setattr(key_listener, 'user_input', '')
}
key_listener = MyKeyListener(key_actions)
listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
listener.start()
keyboard.Controller().release(keyboard.Key.enter)

check_keys()
#Selects eye color

pattern = "* *"
addLinesToSreen("Choose Your {Rb}Eyes{0} color      ", clearScreenArray, 15, 25, color=bright_yellow)
printScreen(clearScreenArray)
# while (not key_listener.is_enter_pressed()):
#     key_listener.check_keys()
check_keys()

#Sceptor color
pattern = "◙"
addLinesToSreen("Choose Your {Mb}Sceptor{0} color       ", clearScreenArray, 15, 25, color=bright_yellow)
printScreen(clearScreenArray)
check_keys()

#Shirt color
pattern = "_|_"
addLinesToSreen("Choose Your {Bb}Shirt{0} color     ", clearScreenArray, 15, 25, color=bright_yellow)
printScreen(clearScreenArray)
check_keys()

#Pants color
pattern = "/ \\"
addLinesToSreen("Choose Your {Gb}Shoe{0} color     ", clearScreenArray, 15, 25, color=bright_yellow)
printScreen(clearScreenArray)
check_keys()


listener.stop()
del key_listener

clearScreenArray = createArrayinArray(clearScreen)
addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[90m')
moveLeftorRight(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 1, manCol,stepMoveBy=5,jumpMoveBy=3,color='\033[0m',ArrayCreate=False)
# printScreen(clearScreenArray)
#reset screen
startScreenArray =createArrayinArray(startScreen)
addLinesToSreen(loadGame, startScreenArray, 7, 36, '\033[33m')
sleepTime = 0.3
for i in range(1,40):
    addLinesToSreen(loadGame, startScreenArray, 7, 36, '\033[33m')
    addLinesToSreen(createEmptyString(loadBar), startScreenArray, 4, 25, '\033[0m')
    if i == 10: loadGame = prepAssets;sleepTime=0.2
    elif i == 20: loadGame = prepGraphics; sleepTime=0.1
    addLinesToSreen(loadBar, startScreenArray, 4, 26, '\033[1;31m')
    loadBar += "#"
    printScreen(startScreenArray)
    time.sleep(sleepTime)
addLinesToSreen("Game is Starting!  ", startScreenArray, 7, 36, '\033[33m')
printScreen(startScreenArray)
time.sleep(2)

#reprints cursor
print('\033[?25h', end='')

#debugger to test a one by one charcter for bounding
# clearScreenArray = createArrayinArray(clearScreen)
# addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[33m')
# moveLeftorRight(testOneByOne, clearScreenArray, 10, 30,stepMoveBy=1,jumpMoveBy=1,color='\033[0m')

# debugger to get length of entity and screen
# os.system(clear_command)
# print(len(createArrayinArray(TestOneByOne)), len(createArrayinArray(clearScreen)))
# time.sleep(5)


#charcter moves right


# waitForInput('')




