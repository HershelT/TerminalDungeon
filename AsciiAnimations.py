import re
reset = "\033[0m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"
background_red = "\033[41m"
background_green = "\033[42m"
background_yellow = "\033[43m"
background_blue = "\033[44m"
background_magenta = "\033[45m"
background_cyan = "\033[46m"
background_white = "\033[47m"
background_bright_black = "\033[100m"
background_bright_red = "\033[101m"
background_bright_green = "\033[102m"
background_bright_yellow = "\033[103m"
background_bright_blue = "\033[104m"
background_bright_magenta = "\033[105m"
background_bright_cyan = "\033[106m"
background_bright_white = "\033[107m"
background_light_blue = "\033[48;5;117m"
ansi_escape = re.compile(r'\033\[\d+m')

colors = {
    #colors
    'w': white, 'r': red, 'g': green, 'b': blue, 
    'y': yellow, 'm': magenta, 'c': cyan, 
    #bright colors
    'W': bright_white, 'R': bright_red, 'G': bright_green, 'B': bright_blue,
    'Y': bright_yellow, 'M': bright_magenta, 'C': bright_cyan, 
    #background colors
    'Wb': background_bright_white, 'Rb': background_bright_red, 'Gb': background_bright_green, 
    'Bb': background_bright_blue, 'Yb': background_bright_yellow, 'Mb': background_bright_magenta,
    'Cb': background_bright_cyan, 'Lb' : background_light_blue,
    
    #reset
    '0' : reset,
              }

#screens
clearScreen = """
     _______________________________________________________________________________________________ 
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |_______________________________________________________________________________________________|
"""
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
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |                                                                                               |
    |_______________________________________________________________________________________________| 
"""

#words to display on screen
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
#movement message
arrowKeysMessage = """Use Arrow Keys to move the Character Around Map"""

#loading Game mechanics
pressEnter="Press 'Enter' To Continue"
loadGame = "Loading Game:"
prepAssets = "Preparing Assets:"
prepGraphics = "Preparing Graphics:"
loadBar = "#"

#Entity animations
ManWalking = """
  ,.,
 (* *) ◙
___|___|
   |   |
  / \  |
"""

heart = """
 ... ...
.........
.........
 .......
  ..... 
"""

characterDesigner = """
        {Cb}Create{0} {Lb}Your Character:
{w}w = white, {r}r = red, {g}g = green,  {b}b = blue,
    {y}y = yellow, {m}m = magenta, {c}c = cyan
"""


testOneByOne=">"
ascii_chars = [
    "☺", "☻", "♥", "♦", "♣", "♠", "•", "◘", "○", 
    "◙", "♂", "♀", "♪", "♫", "☼", "►", "◄", "↕", 
    "‼", "¶", "§", "▬", "↨", "↑", "↓", "→", "←", 
    "∟", "↔", "▲", "▼"
]




#Creating pixel creater
def createArrayinArray(text: str):
    rows = text.splitlines()
    # If the first line is empty, skip it
    if rows and not rows[0]:
        rows = rows[1:]
    # If the last line is empty, skip it
    if rows and not rows[-1]:
        rows = rows[:-1]
    # newText = [list(row) for row in rows]
    # return newText
    newText = []
    current_color = ''
    for line in rows:
        row = []
        segments = re.split(r'(\{.*?\})', line)
        for segment in segments:
            if segment.startswith('{') and segment.endswith('}') and segment[1:-1] in colors:
                current_color = colors[segment[1:-1]]
            else:
                row.extend([current_color + char for char in segment])
        newText.append(row)
    return newText
class PixelDesigner:
    def __init__(self, entity : str) -> None:
        self.entity = entity
        rows = entity.splitlines()
        # If the first line is empty, skip it
        if rows and not rows[0]:
            rows = rows[1:]
        # If the last line is empty, skip it
        if rows and not rows[-1]:
            rows = rows[:-1]
        self.pixelEntity = [list(row) for row in rows]
    def ChangeRow(self, row, rowText, color= "\033[0m"):
        for i in range(0, len(rowText)):
            self.pixelEntity[row][i] = color + rowText[i]
    def setPixelRowCol(self, row, col, pixel):
        self.pixelEntity[row,col] = pixel
    def getEntity(self):
        return self.entity
    def replaceChar(self, char, newChar, color= "\033[0m"):
        for row in range(0, len(self.pixelEntity)):
            for col in range(0, len(self.pixelEntity[row])):
                if self.pixelEntity[row][col] == char:
                    self.pixelEntity[row][col] = color + newChar
    def replaceString(self, string, newString, color= "\033[0m"):
        for i, row in enumerate(self.pixelEntity):
            for j, col in enumerate(row):
                if j+len(string) > len(row): 
                    continue
                result = ""
                for c in range(0, len(string)):
                    result += self.pixelEntity[i][j+c]
                if ansi_escape.sub('', result) == string:
                    for c in range(0, len(string)):
                        self.pixelEntity[i][j+c] = color + newString[c]
                    return True
        else:
            return False           

                # if self.pixelEntity[row][col] == string[0]:
                #     for i in range(0, len(self.pixelEntity[row])):
                #         if col+i >= len(self.pixelEntity[row]):
                #             break
                #         if self.pixelEntity[row][col+i] != string[i]:
                #             if i == len(string)-1:
                #                 for i in range(0, len(string)):
                #                     self.pixelEntity[row][col+i] = color + newString[i]
                #             break                    
    def replaceMultiLineString(self, strings, newStrings, color="\033[0m"):
        if not isinstance(strings, list):
            strings = createArrayinArray(strings)
        if not isinstance(newStrings, list):
            newStrings = createArrayinArray(newStrings)
        
        if len(strings) != len(newStrings):
            return False
        rowsToReplace = []
        count = 0
        for l in range(0, len(strings)):
            for i, row in enumerate(strings):
                for j, col in enumerate(strings[i]):
                    result = []
                    for c in range(0, len(strings[i])):
                        result.append(self.pixelEntity[i][j+c])
                    if result == strings[i]:
                        count+=1
                        rowsToReplace.append(i)
                        continue
                
                if count == len(strings):
                    for n in range(0, len(rowsToReplace)):
                        self.pixelEntity[rowsToReplace[n]] = newStrings[n]
                    return True                    
        # for i in range(len(self.pixelEntity) - len(strings) + 1):
        #     if all(ansi_escape.sub('', ''.join(self.pixelEntity[i + j])) == strings[j] for j in range(len(strings))):
        #         for j in range(len(strings)):
        #             self.pixelEntity[i + j] = color + newStrings[j]
        #         return True
        # return False

    def getPixelizedEntity(self):
        return self.pixelEntity
    
ManWalkingClass = PixelDesigner(ManWalking)  
# ManWalkingClass.replaceMultiLineString("""_|_""", """___""", "\033[33m")
ManWalkingClass.replaceString(",.,", ",.,", "\033[33m")
heartClass = PixelDesigner(heart)
# heartClass.replaceString("..... ", "----- ", background_bright_blue)
heartClass.replaceChar(".", background_bright_red+" ")


