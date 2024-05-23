import time
import os, sys
import io
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
# def printScreen(screen, clear = True):
#     if clear: 
#         os.system(clear_command)

#     for row in screen:
#         print(''.join(row),flush=True)
#         sys.stdout.flush()
    # print('\033[?25h', end='')
def printScreen(screen, clear = True):
    # Create an off-screen buffer
    

    buffer = io.StringIO()

    for row in screen:
        # Write to the buffer instead of directly to the screen
        buffer.write(''.join(row) + '\n')

    if clear:
        sys.stdout.write('\033[?25l')
        # Move the cursor to the top of the terminal
        sys.stdout.write('\033[H\033[?25l')

    # Swap the buffer with the screen
    sys.stdout.write(buffer.getvalue())
    sys.stdout.flush()

    # Clear the buffer for the next frame
    buffer.close()

#Adds text to overwrite over main screen with a specific row from most bottom of text being rowIndex from bottom of screen and column from left
def addLinesToSreen(lines, screen, rowIndex=0, colIndex=0, color='\033[m', createArray = True):
    if createArray: newLines = createArrayinArray(lines)
    else: newLines= lines 
    for i, row in enumerate(newLines):
        for j, char in enumerate(row):
            screen[len(screen) - (len(newLines)+rowIndex)+i][colIndex+j] = color + char.replace('\033[0m', '') + '\033[0m'
def getLinesToSreen(lines, screen, rowIndex=0, colIndex=0, color='\033[m', createArray = True) -> list[list[str]]:
    FullList = []
    if createArray: newLines = createArrayinArray(lines)
    else: newLines= lines 
    for i, row in enumerate(newLines):
        newList = []
        for j, char in enumerate(row):
            newList.append(screen[len(screen) - (len(newLines)+rowIndex)+i][colIndex+j])
        FullList.append(newList)
    return FullList
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
def MoveAllDirection(entity,fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m', ArrayCreate = True):
    os.system(clear_command)
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
    os.system(clear_command)


#hides the cursor in the begining from screen
print('\033[?25l', end='')


#defining full screens
startScreenArray =createArrayinArray(WiderStartScreen)
clearScreenArray= createArrayinArray(WiderClearScreen)
fullScreenArray = createArrayinArray(bigScreen)
# print(len(clearScreenArray), len(clearScreenArray[0]))
# time.sleep(5)

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
import threading
import time
# MoveAllDirection(convertedHuman, clearScreenArray, 1, 5,stepMoveBy=4,jumpMoveBy=1,color='\033[0m',ArrayCreate=False)
# clearScreenArray =createArrayinArray(clearScreen)
# def MovePixelEntity(idle, right, left, jump, down, rAttack, lAttack, power, power1, power2, power3, shotRight,shotLeft, fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m', ArrayCreate = False):
def MovePixelEntity(images : list[Pixel], shots : list[Pixel], fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m', ArrayCreate = False):
    os.system(clear_command)
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    keyboard.Controller().release(keyboard.Key.enter)
    longest_row = len(max(images[1].get() , key=len))
    howManyRows = len(images[1].get())
    backgroundPixel = Background.getPixel(0).getColorAtSpot(10,10)
    def getBackgroundPixel(entity : Pixel):
        return entity.getColorAtSpot(0,0)

    humanBackground = getBackgroundPixel(images[0])
    for i in range(len(images)):
        images[i].replacePixels(humanBackground, backgroundPixel)
    for i in range(len(shots)):
        shots[i].replacePixels(humanBackground, backgroundPixel)
    
    def getEmptyString(FullPixel : Pixel):
        empty = FullPixel.getCopy(FullPixel.get())
        empty.replaceAllPixels(backgroundPixel)
        return empty.get()
    emptyString = getEmptyString(images[0])
    addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color, ArrayCreate)
    printScreen(fullScreen)
    currentDrawing = images[0].get()
    moveBy = 0
    while not key_listener.is_enter_pressed():
        if key_listener.is_esc_pressed():
            sys.exit()
        if key_listener.is_right_arrow_pressed() and (colIndex+longest_row+stepMoveBy)<(len(fullScreen[2])-1):
            if currentDrawing != images[1].get() and currentDrawing != images[0].get() and currentDrawing != images[5].get():
                addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m', createArray=ArrayCreate)
                if currentDrawing == images[6].get(): colIndex += moveBy
                addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                emptyString = getEmptyString(images[0])
                printScreen(fullScreen)
                time.sleep(0.3)
            else:
                emptyString = getEmptyString(images[1])
            currentDrawing = images[1].get()
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m', createArray=ArrayCreate)
            colIndex += stepMoveBy
            addLinesToSreen(currentDrawing, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            emptyString = getEmptyString(images[0])
        if key_listener.is_left_arrow_pressed() and (colIndex-stepMoveBy>=5):
            if currentDrawing != images[2].get() and currentDrawing != images[0].get() and currentDrawing != images[6].get():
                addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m', createArray=ArrayCreate)
                if currentDrawing == images[5].get(): colIndex += moveBy
                addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                printScreen(fullScreen)
                emptyString = getEmptyString(images[0])
                time.sleep(0.3)
            else:
                emptyString = getEmptyString(images[0])
            currentDrawing = images[2].get()
            
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            colIndex -= stepMoveBy
            addLinesToSreen(currentDrawing, fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            emptyString = getEmptyString(images[2])

        if key_listener.is_up_arrow_pressed() and (rowIndex+howManyRows+jumpMoveBy)<(len(fullScreen)):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            if currentDrawing == images[5].get(): colIndex += moveBy
            addLinesToSreen(images[3].get(), fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.3)
            addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.15)
            emptyString = getEmptyString(images[0])
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex += jumpMoveBy
            addLinesToSreen(images[4].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
            printScreen(fullScreen)
            time.sleep(0.3)
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            rowIndex -= jumpMoveBy
            addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            currentDrawing = images[0].get()
        if key_listener.is_down_arrow_pressed() and currentDrawing != images[3].get():# and (rowIndex-jumpMoveBy>0):
            addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            if currentDrawing == images[4].get(): colIndex += moveBy
            addLinesToSreen(images[3].get(), fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
            # rowIndex -= jumpMoveBy
            # addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
            # key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
            currentDrawing = images[3].get()
            emptyString = getEmptyString(images[4])
        if key_listener.is_space_pressed():
            if currentDrawing == images[1].get():
                addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                addLinesToSreen(images[5].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                printScreen(fullScreen)
                currentDrawing = images[5].get()
            if currentDrawing == images[2].get():
                if colIndex - 2 >= 5:
                    addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                    colIndex -= 2
                    addLinesToSreen(images[6].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                    printScreen(fullScreen)
                    currentDrawing = images[6].get()

            if currentDrawing == images[5].get() or currentDrawing == images[6].get():
                    if currentDrawing == images[5].get():
                        shot = shots[0].get()
                        shotLen = (len(shot[0]))
                        newCol = colIndex + shotLen + 2
                        emptyShot = getEmptyString(shots[0])
                    else:
                        shot = shots[1].get()
                        shotLen = -(len(shot[1]))
                        newCol = colIndex - len(shot[1]) 
                        emptyShot = getEmptyString(shots[1])
                    newRow = rowIndex + int(len(shot))
                    
                    try:
                        while (newCol + abs(shotLen)) < (len(fullScreen[2])-1) and newCol - abs(shotLen) >= 5:
                            addLinesToSreen(shot, fullScreen, newRow, newCol, color,ArrayCreate)
                            printScreen(fullScreen)
                            time.sleep(0.15)
                            addLinesToSreen(emptyShot, fullScreen, newRow, newCol, color='\033[0m',createArray=ArrayCreate)
                            newCol += shotLen
                        printScreen(fullScreen)
                        # addLinesToSreen(emptyShot, fullScreen, newRow, newCol, color='\033[0m',createArray=ArrayCreate)
                    except:
                        printScreen(fullScreen)
                        continue
            
            elif currentDrawing == images[0].get():
                try:
                    moveBy = abs(int((len(images[7].get()[0])-(len(images[0].get()[0])))/2))
                    if colIndex-moveBy>=5 and (colIndex+len(images[7].get()[0])-moveBy)<=(len(fullScreen[2])-1):
                        
                        colIndex -= moveBy
                        addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                        addLinesToSreen(images[7].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                        printScreen(fullScreen)
                        time.sleep(0.2)
                        addLinesToSreen(images[8].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                        printScreen(fullScreen)
                        time.sleep(0.2)
                        addLinesToSreen(images[9].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                        printScreen(fullScreen)
                        time.sleep(0.2)
                        addLinesToSreen(images[10].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                        printScreen(fullScreen)
                        emptyString = getEmptyString(images[10])
                        time.sleep(0.4)
                        addLinesToSreen(emptyString, fullScreen, rowIndex, colIndex, color='\033[0m',createArray=ArrayCreate)
                        colIndex += moveBy
                        addLinesToSreen(images[0].get(), fullScreen, rowIndex, colIndex, color,ArrayCreate)
                        printScreen(fullScreen)
                        
                        currentDrawing = images[0].get()
                        emptyString = getEmptyString(images[0])

                except:
                    continue
    listener.stop()
    del key_listener
    os.system(clear_command)
# MovePixelEntity(convertedZarnDog, convertedZarnDog, convertedZarnDog, convertedZarnDog, convertedZarnDog, clearScreenArray, 1, 5,stepMoveBy=3,jumpMoveBy=4,color='\033[0m',ArrayCreate=False)
addLinesToSreen(Background.getPixelArray(0), clearScreenArray, 0, 4, color='\033[0m',createArray=False)
addLinesToSreen(Health.getPixelArray(0), clearScreenArray, (len(clearScreenArray)-len(Health.getPixelArray(0))-1), 7, color='\033[0m',createArray=False)
addLinesToSreen(Health.getPixelArray(2), clearScreenArray, (len(clearScreenArray)-len(Health.getPixelArray(1))-1), 7+len(Health.getPixelArray(0)[0])+1, color='\033[0m',createArray=False)
MovePixelEntity(Human.getAnsciiList(), Bullet.getAnsciiList(), clearScreenArray, 1, 5,stepMoveBy=3,jumpMoveBy=4,color='\033[0m',ArrayCreate=False )
clearScreenArray = createArrayinArray(WiderClearScreen)

#set charcter position and establish movement
manCol = 50+2
os.system(clear_command)
addLinesToSreen(characterDesigner, clearScreenArray, 16, 25, color=bright_blue)
addLinesToSreen("Choose Your {Gb}Hair{0} color\nPress 'Tab' to advance to next body pary", clearScreenArray, 14, 25, color=bright_yellow)
addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False)
addLinesToSreen(Heart.getPixelArray(0), clearScreenArray, 1, 67, color='\033[0m',createArray=False)
# addLinesToSreen(heartClass.getPixelizedEntity(), clearScreenArray, 8, 50, color='\033[0m',createArray=False)

printScreen(clearScreenArray)


user_input = None
def characterSelection(patternList : list):
    SelectedValue = 0
    keyboard.Controller().release(keyboard.Key.enter)
    while (not key_listener.is_enter_pressed()):
        if key_listener.is_tab_pressed():
            SelectedValue += 1
            if SelectedValue > 4: 
                SelectedValue = 0
            addLinesToSreen(f"Choose Your {patternList[SelectedValue][0]} color      ", clearScreenArray, 15, 25, color=bright_yellow)
            characterSelection.pattern = patternList[SelectedValue][1]
            printScreen(clearScreenArray)
        key_listener.keys_pressed.discard(all)
        key_listener.check_keys()
        time.sleep(0.15)

    
#selects hair color
characterSelection.pattern = ",.,"
key_actions = {
    "'r'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, red),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'g'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, green),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'b'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, blue),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'y'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, yellow),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'m'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, magenta),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'c'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, cyan),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'w'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, white),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'0'": lambda: [ManWalkingClass.replaceString(characterSelection.pattern,characterSelection.pattern, reset),addLinesToSreen(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 7, 40, color='\033[0m',createArray=False),key_listener.keys_pressed.discard(all),printScreen(clearScreenArray)],
    "'\\n'": lambda: setattr(key_listener, 'user_input', '')
}

#patterns for charcter selection
patternList = [
    ["{Gb}Hair{0}" , ",.,"],
    ["{Rb}Eyes{0}" , "* *"],
    ["{Mb}Sceptor{0}" , "◙"],
    ["{Bb}Shirt{0}" , "_|_"],
    ["{Gb}Shoe{0}" , "/ \\"],
]
#Create the character selection screen
key_listener = MyKeyListener(key_actions)
listener = keyboard.Listener(
        on_press=key_listener.on_press,
    on_release=key_listener.on_release)
listener.start()
characterSelection(patternList)
listener.stop()
del key_listener


clearScreenArray = createArrayinArray(WiderClearScreen)
addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[90m')
MoveAllDirection(ManWalkingClass.getPixelizedEntity(), clearScreenArray, 1, manCol,stepMoveBy=5,jumpMoveBy=3,color='\033[0m',ArrayCreate=False)
# printScreen(clearScreenArray)
#reset screen
startScreenArray =createArrayinArray(WiderStartScreen)
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
# clearScreenArray = createArrayinArray(WiderClearScreen)
# addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[33m')
# MoveAllDirection(testOneByOne, clearScreenArray, 10, 30,stepMoveBy=1,jumpMoveBy=1,color='\033[0m')

# debugger to get length of entity and screen
# os.system(clear_command)
# print(len(createArrayinArray(TestOneByOne)), len(createArrayinArray(WiderClearScreen)))
# time.sleep(5)


#charcter moves right


# waitForInput('')




