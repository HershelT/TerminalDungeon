#from Data import *
#Maps for Biomes
#Make a system that can create a map of any height 
# But can also place walls in specific spots
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
    def __init__(self, name, cord1, cord2, cord3, cord4):
        self.name = name
        self.length = cord2-cord1
        self.width = cord4-cord3
        self.mapType = [['\033[31m' + "*" + '\033[39m']*self.width for i in range(self.length)]
        self.cord1 = cord1
        self.cord2 = cord2
        self.cord3 = cord3
        self.cord4 = cord4
        PythonAdventure.addToWorld(self)
    def setStuffPos(self, row, col, stuff):
        self.mapType[row][col] = stuff
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
    def getCordinate(self):
        return [self.cord1, self.cord2, self.cord3, self.cord4]     
mapMeadows = setMap("Meadows",20, 30, -10, 0) #(TO DO) problem with display and movement.userImage
mapVolcano = setMap("Volcano",20, 30, 0, 10)
mapCliffs = setMap("Cliffs",20, 30, 10, 20)
#customize each thing with walls and trees and stuff
mapLavaPlains = setMap("Lava Plains",10, 20, -10, 0)
mapIcePlains = setMap("Ice Plains",10, 20, 0, 5) #Stuff from half maps gets displatyed in meadpws
mapFrostedPlains = setMap("Frosted Plains",10, 20, 5, 10)
mapWaterPlains = setMap("Water Plains",10, 20, 10, 20)

mapWaterloo = setMap("Waterloo",0, 10, -10, 0)
mapGreenland = setMap("Greenland",0, 10, 0, 10)
mapPineForest = setMap("Pine Forest", 0, 10, 10, 20)         
#Chacrters to use: ※ Ω ₡ Ⅲ Ⅷ Ⅱ [░-Change to walls or path][
mapGreenland.setStuffPos(2, 5, "░")
mapGreenland.setStuffPos(1, 6, "🪦")
mapWaterloo.setStuffPos(1, 7, "Ⅱ")

buildList = PythonAdventure.getWorld() #list of all terrain on world
#System of classes of worlds allow me to have different world or planets. Will allow me to get to different world

blockedItems = ["※", "Ω", "₡", "Ⅲ", "Ⅷ", "Ⅱ", "🪨", "|", "🪦"]
#[mapMeadows, mapVolcano, mapCliffs, mapLavaPlains, mapIcePlains, mapFrostedPlains, mapWaterPlains, mapWaterloo, mapGreenland, mapPineForest]
#Call.biMap fixes prolem
