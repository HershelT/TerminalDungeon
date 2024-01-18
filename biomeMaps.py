#from Data import *
#Maps for Biomes
#Make a system that can create a map of any height 
# But can also place walls in specific spots
from breakableItems import *

buildList = []
class world: #Allows automatic adding of terrain to environment without manuel
    def __init__(self):
        self.world = []
    def addToWorld(self, terrain):
        self.world.append(terrain)
    def getWorld(self): #Can make different worlds with same system
        return self.world
PythonAdventure = world() 
#add ability so using setMap you put in what world you wnat biome screated in
#this allows person to have overworlds and underworlds
class setMap:#add location on map (n, n, e, e)
    def __init__(self, name, cord1, cord2, cord3, cord4, floorColor = ''): 
        #Add a floor color that can be set in init or changed later to make that the base floor color on map
        
        self.name = name
        self.length = cord2-cord1
        self.width = cord4-cord3
        self.mapType = [['\033[31m' + " " + '\033[39m']*self.width for i in range(self.length)]
        self.cord1 = cord1
        self.cord2 = cord2
        self.cord3 = cord3
        self.cord4 = cord4
        self.objects : dict = {}
        self.floorColor = floorColor
        PythonAdventure.addToWorld(self)
    def setStuffPos(self, row, col, stuff):
        self.mapType[row][col] = stuff
    def setObj(self, row, col, stuff:KeyBlocks):
        self.objects[str(row) + "," + str(col)] = stuff
        self.mapType[row][col] = stuff.getLook()
    def setFloorColor(self, color):
        self.floorColor = color
    def deleteObject(self,row,col):
        self.objects.pop(str(row) + "," + str(col))
    def getObj(self, row, col):
        return self.objects[str(row) + "," + str(col)]
    def getStuffPos(self, row, col):
        return self.mapType[row][col]
    def getMap(self):
        return self.mapType
    def getLength(self): #get rid of length and make caluclation
        return self.length
    def getWidth(self):
        return self.width 
    def getName(self):
        return self.name      
    def getFloorColor(self):
        return self.floorColor
    def getCordinate(self):
        return [self.cord1, self.cord2, self.cord3, self.cord4]     
mapMeadows = setMap("Meadows",20, 30, -10, 0) #(TO DO) problem with display and movement.userImage
mapVolcano = setMap("Volcano",20, 30, 0, 10)
mapCliffs = setMap("Cliffs",20, 30, 10, 20)
#customize each thing with walls and trees and stuff
mapLavaPlains = setMap("Lava Plains",10, 20, -10, 0)
mapIcePlains = setMap("Ice Plains",10, 20, 0, 5, "\033[0;30;47m") #Stuff from half maps gets displatyed in meadpws
mapFrostedPlains = setMap("Frosted Plains",10, 20, 5, 10, "\033[0;30;47m")
mapWaterPlains = setMap("Water Plains",10, 20, 10, 20, "\033[0;38;5;206;48;5;57m")

mapWaterloo = setMap("Waterloo",0, 10, -10, 0, "\033[0;36;44m")
mapGreenland = setMap("Greenland",0, 10, 0, 10, "\033[0;30;46m")
mapPineForest = setMap("Pine Forest", 0, 10, 10, 20, "\033[0;30;43m") 
LowerBound = 0
UpperBound = 30
EasternBound = -10
WesternBound = 20        
#Chacrters to use: ※ Ω ₡ Ⅲ Ⅷ Ⅱ [░-Change to walls or path][

# mapGreenland.setStuffPos(3,5,"🪨")
# mapGreenland.setStuffPos(6,8, "\033[32m※\033[0m")
# mapGreenland.setStuffPos(6,8, "\033[32m※\033[0m")




#Assigns number to texture
#USe A MEthod to fetch what each one is
def loadingMap(map : setMap, mapPulledFrom : list):
    row = 0
    col = 0
    for r in mapPulledFrom:
        col = 0
        for c in r:
            if c == " " or c == "P":
                map.setStuffPos(row,col,(map.getFloorColor()+" "))
            else:
                block = itemToNumber[int(c)]
                #checks if i want to place an object with a property or just a block
                if isinstance(block, KeyBlocks):
                    map.setObj(row,col,block)
                else:
                    map.setStuffPos(row,col,block)
                
            col += 1
        row += 1


blankMap = [
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "],
     [" ", " "," "," "," "," "," "," "," "," "]
]
#basically a tileSet For terminal
itemToNumber =  {
    0 : "\033[37m¤\033[0m", # Stone Block/Boulder
    1 : "\033[1;32mΨ\033[0m", # Tree
    2 : "🪦", #Graveyard
    3 : "\033[38;2;218;165;32mⅡ\033[0m", #Wood Wall
    4 : KeyBlocks("\033[1;33m∏\033[0m", "\033[1;33mWood Gate\033[0m", "Wood Key", "You need a Wooden Key to open - Wood Gate","\033[1;33m"), # locked Wood Door
    5 : "\033[90mΩ\033[0m", # Iron Ore deposit
    6 : '\033[31m▓\033[39m', #portal
    7 : KeyBlocks("\033[38;5;54m∏\033[0m", "\033[38;5;54mBoss Gate\033[0m", "Boss Key", "You need a Boss Key to open - Boss Gate", "\033[38;5;54m"),
    8: "\033[34mΩ\033[0m", #Diamond Ore Deposit
    9: "\033[47m \033[0m", #Unbreakbale Wall
    10:"🌳"

}
#create maps and write a program that cycles through setting position of map to that if spot not empty
#Create a list with blocks and there (DONEEE)
  
GreenlandMap = [
     ["9", "9","9","9","7","9","9","9","9","9"],
     ["9", "1","1","1"," ","0","0","0"," ","9"],
     ["9", "1","1","1"," ","0","0","0"," ","9"],
     ["9", "1","1"," "," "," "," ","0"," ","9"],
     ["4", " "," "," "," "," "," "," "," ","4"],
     ["9", " "," "," ","P"," "," "," "," ","9"],
     ["9", " ","5"," "," "," "," "," "," ","9"],
     ["9", " ","5","5"," "," ","8","8"," ","9"],
     ["9", "5","5","5"," ","8","8","8","8","9"],
     ["9", "9","9","9","9","9","9","9","9","9"]
]
#MapForGreenland
PineForestMap = [
     ["0", "0"," ","5","1"," "," ","8"," "," "],
     ["0", "5"," ","1","1"," ","1","1"," "," "],
     [" ", " ","1"," "," ","0","1"," ","0","0"],
     [" ", "1","1"," "," ","8","1"," ","0"," "],
     [" ", "8","0"," "," "," "," "," "," "," "],
     [" ", "0","0"," "," "," ","1","1","5"," "],
     [" ", "1","1"," "," "," ","1","5","8"," "],
     [" ", "8","1"," "," ","5"," "," "," "," "],
     ["0", " "," "," ","5","5","5"," "," ","5"],
     ["0", "0"," "," "," "," ","5"," ","5","5"]
]



#Maybe make this do things in the main map thing
loadingMap(mapGreenland, GreenlandMap)
loadingMap(mapPineForest, PineForestMap)
# mapGreenland.setStuffPos(0,0, "🪨")


# mapGreenland.setObj(5, 6, WoodDoor)
# print(mapGreenland.getObj(5, 6).getKeyLevel())

buildList = PythonAdventure.getWorld() #list of all terrain on world
#System of classes of worlds allow me to have different world or planets. Will allow me to get to different world

# blockedItems = ["※", "Ω", "₡", "Ⅲ", "Ⅷ", "Ⅱ", "\033[32m※\033[0m","\033[38;2;218;165;32m" + "Ⅱ" + "\033[0m", "🪨", "|", "🪦"]
#[mapMeadows, mapVolcano, mapCliffs, mapLavaPlains, mapIcePlains, mapFrostedPlains, mapWaterPlains, mapWaterloo, mapGreenland, mapPineForest]
#Call.biMap fixes prolem
