import traceback
from typing import Any
from termcolor import colored
# from json import load
# import turtle; from tkinter import *; 
from Data import *; from itemsList import *; from storyAdventure import *; from monsterList import *
import random; import os; import time; import copy;
from gameNounsandWords import *; import string; from animationDepartment import *;
from breakableItems import *
#import keyboard is deprecated so i use pynupt in order to make it cross platform
import sys; from colorama import init; from colorama import Fore, Back, Style

def mapErase(i=1):
        print("\033[?25l", end="", flush=True)
        print("\033[F"*40,flush=True)
        print("\n"*6,flush=True)#Amount of lines i could have max
        print("\033[?25h", end="", flush=True)
def erases(i):
    for x in range(0, i):
        #sys.stdout.write("\033[A")
        print("\033[?25l", end="", flush=True)
        sys.stdout.write("\033[A\033[K")
        sys.stdout.flush()
        print("\033[?25h", end="", flush=True)
        sys.stdout.flush()
        #print("\033[A",' '*115,"\033[A")      #Need to change randomy deending on size of screen
def objectOfCurrentBiome(): #doesnt work yet
    for bObject in buildList:
        if User["Current Biome"] == bObject.getName():
            return bObject
def loadMap(biome = False):
    if biome == False: biome = Call.biMap
    
    # multiply = 2.8
    # if User["Health"] >= 100: multiply = 1.7 #size of line on top
    # elif User["Health"] >= 10: multiply = 1.8
    # else: multiply = 2.0
    # if itemBuffs[1][User['Wearing']][0] < 10: multiply -= 0.4
    # elif itemBuffs[1][User['Wearing']][0] < 100: multiply -= 0.65
    # else: multiply -= 0.8
    # if int(itemBuffs[2][User['Main Hand']][0]) < 10: multiply -= 0.2
    # elif int(itemBuffs[2][User['Main Hand']][0]) < 100: multiply -= 0.3
    # else: multiply -= 0.5
    print("\033[?25l", end="", flush=True)
    lengthC = 0;counterM = 0; rowCount = 0
    ends = "\033[0m"; starts = " "*65; lineMark = "\033[94m|\033[K\033[0m" #2.8 is distance without health display(f"\033[31m{User['Health']}|{User['Max Health']}\033[94m__\033[90mP:{monsterAttacks.armor}|{itemBuffs[1][User['Wearing']][0]}\033[94m__\033[35mD:{takeItem.mainhand}"
    print(" "*63,"\033[94m","_"*(int(biome.getWidth()*1.2)) + "\33[0m", "\033[K", flush= True)
    color = biome.getFloorColor()
    for row in biome.getMap():
        if lengthC > biome.getLength(): break
        row_str = starts
        for col in row:
            counterM += 1
            if counterM > biome.getWidth() - 1: 
                
                if rowCount == 0: ends +=  f"\033[94m|\033[0m \033[31mHealth:"
                elif rowCount == 1: ends +=  f"\033[94m|\033[0m \033[31m({User['Health']}|{User['Max Health']})"
                elif rowCount == 2: ends +=  f"\033[94m|\033[0m \033[90mArmor:"
                elif rowCount == 3: ends +=  f"\033[94m|\033[0m \033[90m{monsterAttacks.armor}|{itemBuffs[1][User['Wearing']][0]}"
                elif rowCount == 4: ends += f"\033[94m|\033[0m \033[35mDamage:"
                elif rowCount == 5: ends += f"\033[94m|\033[0m \033[35m{takeItem.mainhand}"
                elif rowCount == 6: ends += f"\033[94m|\033[0m \033[92m{User['Main Hand']}"
                elif rowCount == 7: ends += f"\033[94m|\033[0m \033[92m{User['Wearing']}"
                elif rowCount == 8: ends += f"\033[94m|\033[0m \033[033mLvL: {User['LVL']}"
                else: ends = "\033[94m|\033[0m "
                # elif row == 2: ends +=  f"\033[94m__\033[90mP:{monsterAttacks.armor}|{itemBuffs[1][User['Wearing']][0]}"
                # elif row == 4: ends += f"\033[94m__\033[35mD:{takeItem.mainhand}" #change for when map is different sizes
            if counterM > biome.getWidth(): break
            row_str += f'{lineMark}{color}{col}\033[0m'
            # print(f'{starts}{lineMark}{color}{col}\033[0m',end = f"{ends}\033[0m\033[K", flush= True); 
            starts = f"{color}"; lineMark = ""
        print(row_str+ends + "\033[0m\033[K", flush= True)
        counterM = 0; ends = "\033[0m"; starts = " "*65; lineMark = "\033[94m|\033[0m"
        lengthC+=1; rowCount += 1
    print(" "*63,"\033[94m","\033[94m\u203e"*(int(biome.getWidth()*1.2)) + "\033[0m", "\033[K", flush= True)
    # print(" "*64,f" \033[033mLvL: {User['LVL']}", "\33[94m\u203e"*(int(Call.biMap.getWidth()*2.1)),end = "\33[0m\033[K", flush= True)
    print("\033[?25h", end="",flush=True)
    mapErase(12)
def getNumberInSentence(sentence):
    newInt = 0 #Only gets numbers in sentence/string and ignores non numbers
    for num in sentence:
        for x in range(0, 10):
            if str(x) == num:
                newInt = newInt*10 + x
    return newInt
def help():
#Maybe make it so jeffery says help
    help.ran = True
    os.system('cls')
    print("-"*56)
    print("""Do to the indcredible work of Hershel Thomas, the game now allows you to naturally
talk to the game as if it was a normal conversation. The game looks for key words and phrases in order
to run the game. For example you can write 'n' to move north or you can write something along the lines of
'I want to move forward' or 'take a step north'. Therese are just a few examples of sentences you can do
Play around with what you can and cannot do. Its awesome!
----------------------------------------------------------------------------------------------------
You can pick up items, drop items, attack monsters, shoot arrows, check your inventory, hold weapons and wear cloths
animate the mouth of Jeffery at the top, look at your current quest or main storyline adventure.
craft items, check in the recipe book, check a certain crafting recipe for an item by saying
'recipe' and the name of the item in the same sentence. ('n', 'e', 's', 'w') for shorthand movement without sentences
get the users location and item info. Just remeber you can use sentences to test out which ones work and which ones dont
to get what you want, check how many monsters have been killed, or what biome you are in
most importantly exit the game with 'exit'""")
def anys(choice ,inputCase: list):
    wordle = inputCase
    if any(word in choice for word in wordle): return True

def location():
    print("Biome: {}".format(User["Current Biome"]))
    print("Location: ")
    print(f"North: {space[0]}:{Movement.spotN}")
    print(f"East: {space[1]}:{Movement.spotE}")

def lookAhead(objOrBlock : bool = False):
    #looks ahead one spot depending on direction of player
    directionN = Movement.spotN;directionE = Movement.spotE; overColor=Call.biMap.getFloorColor()
    # floor = '\033[31m' + "*" + '\033[39m'
    if Movement.userImage == "▼" :newAdd = 1
    elif Movement.userImage == "▲":newAdd = -1
    if Movement.userImage == "◄" :newAdd = -1
    elif Movement.userImage == "►":newAdd = 1
    if Movement.userImage == "▼"or Movement.userImage == "▲":
        directionN += newAdd
    else:
        directionE += newAdd
    try:
        # if objOrBlock == True: 
        # else:
        if directionN < Call.biMap.getLength() and directionN >= 0 and directionE >=0 and directionE < Call.biMap.getWidth():
            try:
                objectAtSpot = Call.biMap.getObj(directionN,directionE)
            except:
                objectAtSpot = Call.biMap.getStuffPos(directionN,directionE)
        else:
            objectAtSpot=False

    except:
        objectAtSpot = False
    #returns an array of[northernLocation,EasternLocation,ObjectAtSpot]
    return [directionN,directionE,objectAtSpot]
    #(commented out code moves for formatting)
    #Gets the object at the spot one ahead
    # space[0] = directionN
    # space[1] = directionE
    # #tests if user went to new biome (Maybe fix for speed but not noticable but probably using more ram)
    # biome = Call.biMap
    # newBiome = testForNewEnv()
    # print("Debuging 1")
    # time.sleep(1)
    # objectAtSpot = newBiome.getStuffPos(directionN%newBiome.length,directionE)
    # print("Debuging 2")
    # time.sleep(1)
    # space[0],space[1] = Movement.spotN,Movement.spotE
    # if biome != newBiome:
    #     return [directionN,directionE,objectAtSpot]
    # else:
    #     return [directionN,directionE,objectAtSpot]
    # # Movement.pre = biome.getStuffPos(space[0],space[1])




# def MovementTwo():
#     direct = words["direction"]; t = Input.choice; BoundryLine = ""
#     if (("move" or "step" in t) and any(word in t.lower() for word in direct[7: 9])) or "w" == t.lower(): BoundryLine = "West"; Movement.userImage = "◄"#ᐊ▲►▼◄◀֎֎֎֎
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[0:2])) or "n" == t.lower(): BoundryLine = "North"; Movement.userImage = "▲"#ᐃ▲/3456
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[2:4])) or "e" == t.lower(): BoundryLine = "East"; Movement.userImage = "►"#ᐅ☻        elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower(): t = "s"; Movement.userImage = "▼"#ᐁ ▼▼◄
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower():  BoundryLine = "South"; Movement.userImage = "▼"#ᐁ ▼▼◄
#     moving = lookAhead()
#     if (((moving[0]< 0) or (moving[0] >= 30)) or ((moving[1] < -10) or (moving[1] >= 20))):
#         print("WERWERRWE")
#         time.sleep(2)
#         Call.biMap.setStuffPos(space[0],space[1], Movement.userImage)
#         mapErase(1);loadMap()
#         print("The " + BoundryLine + "ern Boundry Line blocks your path")
#     elif moving[2] in blockedItems:
#         Call.biMap.setStuffPos(space[0],space[1], Movement.userImage)
#         mapErase(1);loadMap()
#         print(f"A ({moving[2]}) blocks your path") #Add To display name as well using itemDrops[ (23/22/2023)]
#     else:
#         #Sets previous spot before moving to what you were standing on
#         Call.biMap.setStuffPos(space[0], space[1], Movement.pre)
#         #updates user space
#         space[0] = moving[0]
#         space[1] = moving[1]

#         # Movement.spotN = moving[0]
#         # Movement.spotE = moving[1]
#         #tests if user went to new biome (Maybe fix for speed but not noticable but probably using more ram)
#         biome = testForNewEnv() #might be problem here with what biome it is
#         n = (space[0]) % biome.getLength()
#         e = (space[1]) % biome.getWidth()
#         #(TO DO-Done) Game charces when going to different sized maps like froxen lakes
#         #I believe problem is that the caluclualtion is off because my location is past 15 for second 5
#         #width map and needs to compensate but figure out
#         Movement.spotN = ((biome.getLength()-1) - n)
#         Movement.spotE = e
#         north,east = Movement.spotN, Movement.spotE
#         # biome = testForNewEnv()
#         print(f"{moving[0]},{north} : {moving[1]},{east}")
#         time.sleep(2)
#         Movement.pre = biome.getStuffPos(north,east) #gets place before user steps there
#         biome.setStuffPos(north,east, Movement.userImage) #Updates user position
#         #Goes through game loop
#         loadMap()
#         findEnv()
#         findMonster()
#         findItem()
# def movementAddition():
#     Call.biMap.setStuffPos(Movement.spotN, Movement.spotE, Movement.pre)
#     biome = testForNewEnv() #might be problem here with what biome it is
#     n = (space[0]) % biome.getLength()
#     e = (space[1]) % biome.getWidth()
#     #(TO DO-Done(12/22/2023)) Game charces when going to different sized maps like froxen lakes
#     #I believe problem is that the caluclualtion is off because my location is past 15 for second 5
#     #width map and needs to compensate but figure out
#     Movement.spotN = (biome.getLength()-1) - n
#     Movement.spotE = e
#     north = Movement.spotN
#     east = Movement.spotE
#     Movement.pre = biome.getStuffPos(north, east)
#     #(newProblem is droped items get displayed in all places) - fixeD(12/22/2023)
#     biome.setStuffPos(north, east, Movement.userImage) #(Problem might be here when putting charcter on meadows)
#     loadMap()
#     findEnv()
#     findMonster()
#     findItem()
def Movement():
    direct = words["direction"]; t = Input.choice; 
    BoundryLine = ""; increment = [0,0]
    if (("move" or "step" in t) and any(word in t.lower() for word in direct[7: 9])) or "w" == t.lower():increment[1]-= 1;  BoundryLine = "West"; Movement.userImage = "◄"#ᐊ▲►▼◄◀֎֎֎֎
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[0:2])) or "n" == t.lower(): increment[0]+= 1; BoundryLine = "North"; Movement.userImage = "▲"#ᐃ▲/3456
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[2:4])) or "e" == t.lower(): increment[1]+= 1; BoundryLine = "East"; Movement.userImage = "►"#ᐅ☻        elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower(): t = "s"; Movement.userImage = "▼"#ᐁ ▼▼◄
    elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower(): increment[0]-= 1;  BoundryLine = "South"; Movement.userImage = "▼"#ᐁ ▼▼◄
    elif t == "start": Movement.userImage = "▲"; Call.biMap.setStuffPos(Movement.spotN, Movement.spotE, Movement.userImage);mapErase(1);loadMap(); return False
    SpotAhead = lookAhead()
    if (((space[0] + increment[0] < LowerBound) or (space[0] + increment[0] >= UpperBound)) or ((space[1] +increment[1] < EasternBound) or (space[1] + increment[1] >= WesternBound))):
        Call.biMap.setStuffPos(Movement.spotN, Movement.spotE, Movement.userImage)
        mapErase(1);loadMap()
        print(colored("The " + BoundryLine + "ern Boundry Line blocks your path","light_green"))
        return False
    elif (SpotAhead[2] == False):
        Call.biMap.setStuffPos(Movement.spotN,Movement.spotE, Movement.pre)
        space[0] += increment[0]
        Movement.spotN += -increment[0]
        space[1] += increment[1]
        Movement.spotE += increment[1]
        for bObject in buildList:
            bound = bObject.getCordinate()
            if space[0] >= bound[0] and space[0] < bound[1] and space[1] >= bound[2] and space[1] < bound[3]:
                if bObject.getStuffPos(Movement.spotN % (bObject.getLength()),space[1] % bObject.getWidth()) in blockedItems:
                    blockingObject = bObject.getStuffPos(Movement.spotN % (bObject.getLength()),space[1] % bObject.getWidth())
                    space[0] -= increment[0]
                    space[1] -= increment[1]
                    Movement.spotN -= -increment[0]
                    Movement.spotE -= increment[1]
                    Call.biMap.setStuffPos(Movement.spotN,Movement.spotE, Movement.userImage)
                    mapErase(1);loadMap()
                    print(f"{blockingObject}", colored(f"Blocks Your path On {BoundryLine}ern Side","light_green"))
                    return False
                display1 = User["Current Biome"]; User["Current Biome"] = bObject.getName()
                display2 = "Entered Biome: {}".format(User["Current Biome"])
                Call.biMap = bObject
                scatterItem("item", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                scatterItem("monster", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                Movement.spotN = Movement.spotN % (Call.biMap.getLength())
                Movement.spotE = space[1] % Call.biMap.getWidth()
                Movement.pre = Call.biMap.getStuffPos(Movement.spotN,Movement.spotE)
                Call.biMap.setStuffPos(Movement.spotN,Movement.spotE, Movement.userImage)
                mapErase(1);loadMap()
                print(colored(f"--------------\nLeaving Biome: {display1}\n{display2}\n--------------","light_yellow"))
                #Make a for loop to spawn monsters from old adventures if decide to use that ma=echanic (will be  lot of monsters but can change that)
                #Can also make a loop to give each place a new random amount of monsters, super eas
                if (not User["Current Biome"] in User["Biomes Discovered"]):
                    User["Biomes Discovered"].append(User["Current Biome"])
                    print(colored(f"New Biome Discovered!","light_yellow"))
                findMonster()
                findItem()
                return False
        print("Game is broken")
        time.sleep(10)
    elif SpotAhead[2] in blockedItems:
        Call.biMap.setStuffPos(Movement.spotN,Movement.spotE,Movement.userImage)
        mapErase(1);loadMap()
        print(f"{SpotAhead[2]}", colored("Blocks Your path","light_green"))
        return False
    else:
        # objectInFront = lookAhead(True)
        if isinstance(SpotAhead[2], KeyBlocks):
            # passingRequirment = objectInFront.getKeyLevel()
            Call.biMap.setStuffPos(Movement.spotN,Movement.spotE, Movement.userImage)
            mapErase(1);loadMap()
            print(f"{SpotAhead[2].getLook()}",colored(f"Blocks Your Path\n{SpotAhead[2].getMessage()}","light_green"))
            return False
        else:
            Call.biMap.setStuffPos(Movement.spotN,Movement.spotE,Movement.pre)
            space[0] += increment[0]
            Movement.spotN += -increment[0]
            space[1] += increment[1]
            Movement.spotE += increment[1]
            Movement.pre = SpotAhead[2]
            Call.biMap.setStuffPos(Movement.spotN,Movement.spotE,Movement.userImage)
            mapErase(1);loadMap()
            findMonster()
            findItem()
        

    # if (Movement.spotN + increment[0] < 0 or Movement.spotN + increment[0] >= 10) or (Movement.spotE + increment[1] < 0 or Movement.spotE + increment[1] >= Call.biMap.length()):
    #     space[0], Movement.spotN += increment[0]
    #     space[1], Movement.spotE += increment[1]
    #     findEnv()
    #     Movement.spotN = (Call.biMap.length()-1) % Movement.spotN
    #     Movement.spotE = (Call.biMap.length()-1) % Movement.spotE
        




# def MovementThree():
#     inc = 0
#     direct = words["direction"]; t = Input.choice #have to check if they said move
#     #Fix boundry as boundry gets larger
#     if (("move" or "step" in t) and any(word in t.lower() for word in direct[7: 9])) or "w" == t.lower(): inc-= 1; space[1] -= 1; t = "west"; Movement.userImage = "◄"#ᐊ▲►▼◄◀֎֎֎֎
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[0:2])) or "n" == t.lower(): inc+= 1; space[0] += 1; t = "north"; Movement.userImage = "▲"#ᐃ▲/3456
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[2:4])) or "e" == t.lower(): inc+= 1; space[1] += 1; t = "east"; Movement.userImage = "►"#ᐅ☻
#     elif (("move" or "step" in t) and any(word in t.lower() for word in direct[4:7])) or "s" == t.lower(): inc-= 1; space[0] -= 1; t = "south"; Movement.userImage = "▼"#ᐁ ▼▼◄
#     elif t == "start": Movement.userImage = "▲"
#     #(TO DO) Make world randomyl generate biomes with items located in
#     bMap = Call.biMap.getMap()
#     leMap = Call.biMap.getLength()
#     wiMap = Call.biMap.getWidth()
#     #bootleg checking to see if is gate
#     try:
#         objectInFront: KeyBlocks = Call.biMap.getObj((leMap-1)-((space[0]) % leMap),space[1] % wiMap)
#         if objectInFront.getIsBlocking():
#             passingRequirment = objectInFront.getKeyLevel()
#             message = objectInFront.getMessage()
#             look = objectInFront.getLook()

#             if t == "north": space[0] -= 1
#             elif t == "south": space[0] += 1
#             elif t == "east": space[1] -= 1
#             elif t == "west": space[1] += 1
            
#             Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap,space[1] % wiMap, Movement.userImage)
#             mapErase(1);loadMap()
#             print(f"{look} Blocks your Path\033[0m\n{message}")
#             return False
#     except:
#         if ((space[0]< 0) or (space[0] >= 30)) or ((space[1] < -10) or (space[1] >= 20)):
#             if t == "north": space[0] -= 1
#             elif t == "south": space[0] += 1
#             elif t == "east": space[1] -= 1
#             elif t == "west": space[1] += 1
#             Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap, space[1] % wiMap, Movement.userImage)
#             mapErase(1);loadMap()
#             print(f"Cannot go past boundry on {t}ern side")
#             return False
#         # elif bMap[(leMap-1)-(space[0]) % leMap][space[1] % wiMap] in blockedItems:
        
#         elif Movement.spotN + inc < 0 or Movement.spotE >= 10:
#             print("Hey")
#             # movementAddition()
#             return False
#         elif bMap[(leMap-1)-(space[0]) % leMap][space[1] % wiMap] in blockedItems:
#             if t == "north": space[0] -= 1
#             elif t == "south": space[0] += 1
#             elif t == "east": space[1] -= 1 #Change maps to use object maps (Done mostly)
#             elif t == "west": space[1] += 1
#             Call.biMap.setStuffPos((leMap-1)-(space[0]) % leMap,space[1] % wiMap, Movement.userImage)
#             mapErase(1);loadMap()
#             try:
#                 itemInFront = lookAhead()
#                 print(f"\033[32mA \033[31m{itemDrops[itemInFront[2]][2]}\033[32m:{itemInFront[2]}\033[32m Blocks your Path\033[0m")
#                 return False
#             except:
#                 movementAddition()
#                 return False
#         movementAddition()
        #Huge Bug where if there is item all the way to left on same row
        #Then i cannot move to next biome because it thinks that is blocking it
        #Problem with calculation




        # Call.biMap.setStuffPos(Movement.spotN, Movement.spotE, Movement.pre)
        # biome = testForNewEnv() #might be problem here with what biome it is
        # n = (space[0]) % biome.getLength()
        # e = (space[1]) % biome.getWidth()
        # #(TO DO-Done(12/22/2023)) Game charces when going to different sized maps like froxen lakes
        # #I believe problem is that the caluclualtion is off because my location is past 15 for second 5
        # #width map and needs to compensate but figure out
        # Movement.spotN = (biome.getLength()-1) - n
        # Movement.spotE = e
        # north = Movement.spotN
        # east = Movement.spotE
        # Movement.pre = biome.getStuffPos(north, east)
        # #(newProblem is droped items get displayed in all places) - fixeD(12/22/2023)
        # biome.setStuffPos(north, east, Movement.userImage) #(Problem might be here when putting charcter on meadows)
        # loadMap()
        # findEnv()
        # findMonster()
        # findItem()


        #working on building so doesnt drop (TO DO 12/22/2023)
        #(OLD CODE COMMENTED OUT AND MOVED)
        #Add checks to check if chacrter is on special block or wall
        #USE LOOK AHEAD FUNCTION (12/22/2023)
        #Checks if new positon is unicode value then trigger that specific command for that unicode value
        #can make dictionaries where it is named after the unicode value
        #dont run certain things if that happens make it so it returns at the end:
        # n = (space[0]) % leMap
        # e = space[1] % wiMap
        # Movement.spotN = (leMap-1) - n
        # Movement.spotE = e
        # try: Call.biMap.setStuffPos(Movement.saveN, Movement.saveE, Movement.pre) (deprecated 12/22/2023)
        # except: 1 == 1
        #change for whatever was the previous spot
        #Works but cannot see user because map doesnt reload.
        #cannot make it reload because texts gets overwritten

def shoot():
    #(TO DO) - Make it so different weapons can shoot faster so change time speed
     #shooting mechanic for arrows later
                            #add if statement to see if location touches a monster
    try:
        isArrow = "nothing"
        for item in User["Inventory"]:
            if "arrow" in item.lower():
                isArrow = item
                break
        if isArrow == "nothing": print("No Arrows or Range weapons in inventory"); return False
        mapErase(1)
        leMap = Call.biMap.getLength()
        wiMap = Call.biMap.getWidth()
        directionN = Movement.spotN;directionE = Movement.spotE
        firstTry = True;minusNorth = directionN;minusEast = directionE
        counter = 0
        #would have to change for different size room
        #Make it so it only checks when you have arrows
        #(TO DO) - Make Cleaner and condense
        if Movement.userImage == "▼" :newAdd = 1;compare = directionN < leMap; test = compare
        elif Movement.userImage == "▲":newAdd = -1;compare = directionN > 0; test = compare
        if Movement.userImage == "◄" :newAdd = -1;compare = directionE > 1; test = compare
        elif Movement.userImage == "►":newAdd = 1;compare = directionE < (wiMap-1); test = compare
        while compare:
            if Movement.userImage == "▼"or Movement.userImage == "▲":
                directionN += newAdd;minusNorth = directionN - newAdd
            else:
                directionE += newAdd;minusEast = directionE - newAdd
            if firstTry == False:
                Call.biMap.setStuffPos(minusNorth, minusEast, shoot.pre)
                # map[minusNorth][minusEast] = shoot.pre   (Deprecated not needed 12/22/2023)
            shoot.pre = Call.biMap.getStuffPos(directionN, directionE)
            if shoot.pre in blockedItems: #tests if wall is in the way Should add test for if object like gate in way
                break
            Call.biMap.setStuffPos(directionN,directionE, "֎")
            firstTry = False
            if Movement.userImage == "▼": compare = directionN < (leMap-1)
            elif Movement.userImage == "▲": compare = directionN > 0
            if Movement.userImage == "◄" : compare = directionE > 0
            elif Movement.userImage == "►": compare = directionE < (wiMap-1)
            loadMap()
            time.sleep(0.2)
            counter+=1
        if test:
            Call.biMap.setStuffPos(directionN,directionE, shoot.pre)
        else: print("Shot can't leave biome"); return False
        if counter>0: 
            User["Inventory"].remove(isArrow)
            if isArrow not in User["Inventory"]: 
                User["Main Hand"] = ""
        else: print("Shot cant shoot through walls"); return False #Maybe make certaub utens shoot through different walls
        mapErase(1);loadMap()
    except:
        print("Cant Shoot there")
def teleport():
    try:
        tp = [space[0], space[1]] #cordinate at spot
        tpStr = Input.choice[11:-1]
        #sets spots and movement to new cordinate
        for x in range(0, 2):
            space[x] = int(tpStr.partition(',')[x*2])
        mapErase(1)
        Movement()
        print(f"teleporting...{space}")
        # Movement.spotN,Movement.spotE = space[0],space[1]
        # if lookAhead != False:
        #     Call.biMap.setStuffPos(tp[0],tp[1], Movement.pre)
        #     #checks if going to neew biome and changes and loads chacrter accordingly
        #     biome = testForNewEnv()
        #     Movement.pre = biome.getStuffPos(Movement.spotN,Movement.spotE)
        #     biome.setStuffPos(space[0],space[1], Movement.userImage)

        #      #gets place before user steps there

        #     # mapErase(1)
        #     loadMap()
        #     findEnv()
        #     findMonster()
        #     findItem()
        #     print(f"teleporting...{space}")
        # else:
        #     Movement.spotN = space[0]
        #     Movement.spotE = space[1]
        #     print("Cant teleport out of bounds")

    except:
        print("Command Input wrong")
def specItemInfo(item):
    br = False
    for rows in itemInfo:
        for elem in rows:
            if elem in item:
                print(item + rows[elem])
                br = True
                break
        if br:
            break
def dice(start, limit):
    roll = random.randint(start, limit)
    return roll
def attackMonster(mon):
    buff = 0; roll = 0; attackMonster.cL = 0; listI = itemBuffs[2]
    if User["Main Hand"] != "":
        for lists in itemBuffs[2]:
            if User["Main Hand"] == lists:
                listB = listI[lists]
                listBuff = listB[0]
                buff = int(listBuff)
                break
    roll = dice(1, 6); totalDG = roll + buff
    time.sleep(0.35)
    print(colored("<------>|User is Attacking|<------>", "light_cyan"))
    time.sleep(0.5)
    print(colored(f"Rolled: {roll} on a d6", "dark_grey"))
    if buff != 0:
        time.sleep(0.5)
        print(colored(f'{User["Main Hand"]} additional damage: {buff}', "dark_grey"))
        attackMonster.cL = 1
    time.sleep(0.5)
    print(colored(f"Total Damage: \033[94m{totalDG}\033[0m", "dark_grey"))
    findMonster.HP -= totalDG
    time.sleep(0.5)
    # print(f"----{mon}----\n-> Health: {findMonster.HP} <-")
    return totalDG
def monsterAttacks(mon):
    roll = dice(1, 6); totalDG = roll + findMonster.DG
    usingArmor = "User"
    if monsterAttacks.armor > 0: 
        monsterAttacks.armor -= totalDG
        usingArmor = "Armor"
        if monsterAttacks.armor < 0: monsterAttacks.armor = 0
    else:
    # totalDG -= itemBuffs[1][User['Wearing']][0]
        if totalDG < 0: totalDG = 0
        else: User["Health"] -= totalDG
    #User is invulnerable when wearin higher level armor, I want user to go through armor first and then health
    loadMap()#Displays before actual event
    time.sleep(0.35)
    print(colored(f"<------>|{mon} is Attacking|<------>", "light_magenta"))
    time.sleep(0.5)
    print(colored(f"{mon} Rolled: {roll} on a d6", "dark_grey"))
    time.sleep(0.5)
    print(colored(f'{mon} additional damage: {totalDG} [{findMonster.DG}+{roll}]', "dark_grey"))
    time.sleep(0.5)
    print(colored(f"Total Damage Towards {usingArmor}: \033[31m{totalDG}\033[0m", "dark_grey"))
    
    
    return totalDG


    #Make it so armor takes away damage from weapons, but if armor causes weapon to do no damage make it
    #so the person always does 1 damage
def findMonster():
    findMonster.list = []; findMonster.HP = 0; findMonster.DG = 0; attack = " "; findMonster.yes = False
    try: #Checks if position equals a pos of item alos checks if pick up command is used and pos is right
        for monster in monstersClear:
            if space == monstersClear[monster]:
                findMonster.yes = True
                #erases(30); animation(Call.level, True, True, False) #FIx tests to make it so it prints and you can still see it

                if "-" in monster: monsterN = monster.rpartition('-')[0]
                else: monsterN = monster
                findMonster.list = monMDandHP[monsterN]
                findMonster.HP = findMonster.list[1]
                findMonster.DG = findMonster.list[0]
                findMonster.damageMonster = 0 
                findMonster.damageUser = 0
                
                rewM = findMonster.list
                print(colored(f'-------------------\nA wild {monsterN} appeard: \n <---->|Combat Mode|<---->',"dark_grey"))
                while findMonster.HP > 0:
                    if attack != "":time.sleep(0.5)
                    print(colored(f"---------User----------\n   -> Health: {User['Health']} | {User['Max Health']} <-\n   -> Armor Protection: {monsterAttacks.armor} | {itemBuffs[1][User['Wearing']][0]}\n   -> Damage Dealt To \033[94mMonster\033[0m\033[31m: {findMonster.damageUser} <-\033[0m", "red"))
                    print(colored(f"---------{monsterN}----------\n   -> Health: {findMonster.HP} | {monMDandHP[monsterN][1]} <-\n   -> Damage Dealt To \033[31mUser\033[0m\033[94m: {findMonster.damageMonster} <-\033[0m", "light_blue"))
                    if attack != "": time.sleep(0.25)
                    attack = input("Attack or Flee? (a/f) \n->");
                    while attack == "":#Gets rid of stupid enter thing changing look(1/4/2024)
                        print('         \033[F                      \033[F', end='')
                        attack = input("Attack or Flee? (a/f) \n->");
                    erases(1)
                    # print("\033[K")
                
                    mapErase(1)
                    loadMap()
                    if "attack" in attack.lower() or "a" == attack:
                        #erases(cLine); cLine = 0
                        # print(f"You choose to attack the {monsterN}"); cLine +=1
                        findMonster.damageUser = attackMonster(monsterN)
                        
                        print(colored((f"---------User----------\n   -> Health: {User['Health']} | {User['Max Health']} <-\n   -> Armor Protection: {monsterAttacks.armor} | {itemBuffs[1][User['Wearing']][0]}\n   -> Damage To \033[94mMonster\033[0m\033[31m: {findMonster.damageUser} <-\033[0m"), "red"))
                        print(colored((f"---------{monsterN}----------\n   -> Health: {findMonster.HP} | {monMDandHP[monsterN][1]} <-\n   -> Damage Dealt To \033[31mUser\033[0m\033[94m: {findMonster.damageMonster} <-\033[0m"), "light_blue"))
                        if findMonster.HP <= 0: break
                        time.sleep(0.5)
                        #(DO) wait for user to input enter to move on to next line of code
                        input("Press Enter to continue fight...")
                        mapErase(1)
                        loadMap()
                        findMonster.damageMonster = monsterAttacks(monsterN) #Finally making combat system
                       
                        #choose betwene armor increasing health or preventing more damage
                    elif "flee" in attack or "f" == attack: #(TO DO): Make it so when you flee you lose damage
                        #erases(2)
                        monsterAttacks.armor = itemBuffs[1][User['Wearing']][0] #Maybe make it so fleeing doesnt replenish armor
                        mapErase(1)
                        loadMap()
                        print("-Fleeing Combat Like a COWARD-\n")
                        return 0 #Make it so when you flee you lose health #and when enemy attacks chance not to hit anf you too/
                    elif anys(attack, words["hand"]):
                        item = checkItemInfo(attack)
                        print('Mainhand: ')
                        if attack == "mainhand" or attack == "mainhand ":
                            print(f'{User["Main Hand"]}')
                        else: mainhand("MH", item)
                    elif anys(attack, words["wear"]):
                        wear = checkItemInfo(attack)
                        print("Wearing: ")
                        if attack == "equip " or attack == "wear" or attack == "wear ":
                            print(f'{User["Wearing"]}')
                        else: mainhand("Wear", wear)
                    elif anys(attack, words["consume"]):
                        food = checkItemInfo(attack)
                        if attack == "consume " or attack == "eat " or attack == "consume" or attack == "eat":
                            print(colored('Choose something to eat!',"light_red"))
                        else:
                            consume(food)
                            # mapErase()
                            # loadMap()
                    elif "/kill" in attack: findMonster.HP = -1
                    
                #Add a return if health is below or equal to 0
                mapErase(1)
                # print(colored((f"---------User----------\n   -> Health: {User['Health']} | {User['Max Health']} <-\n   -> Damage To \033[94mMonster\033[0m\033[31m: {findMonster.damageUser} <-\033[0m"), "red"))
                # print(colored((f"---------{monsterN}----------\n   -> Health: {findMonster.HP} | {monMDandHP[monsterN][1]} <-\n   -> Damage To \033[31mUser\033[0m\033[94m: {findMonster.damageMonster} <-\033[0m"), "light_blue"))
                # loadMap()
                # mapErase(1)
                dropA = []
                # if dropProb >= (10 - rewM[4]):
                dropArr = rewM[3]
                itemArr = rewM[2]
                counter = 0
                for item in itemArr:
                    dropMinMax = dropArr[counter]
                    dropAmount = dice(int(dropMinMax[0]), int(dropMinMax[1]))# + rewM[4]
                    for it in range(dropAmount):
                        dropA.append(item)
                        User["Inventory"].append(item)
                        User["InventoryCollected"].append(item)
                    counter += 1
                #print(dropAmount)Change dnyamix where there is no probability drop count
                #But there is more items that can drop from monster Problem is individual
                #items should have higher drop chance if they are from bosses or lower level items
                #Make it so it can drop a random item from each list or a certain amounts of items from each list
                                            #It chooses randomly which items are dropped and stuff can add another drop percantage for each item
                if dropA != []:
                    sortDrop = sortItemCount(dropA, "")
                    sortDrop = " ".join(sortDrop)
                else: sortDrop = "Nothing"
                #else: sortDrop = Nothing
                time.sleep(0.5)
                erases(30)
                print("<-","-"*40,"->")
                changeMessage(f"""#--|Congrats on defeating {monsterN}|--\n${monsterN} Dropped: \n$->{sortDrop}""")
                animation("Spokesman", True, False, (f"    \033[90mKilled {monsterN}: \033[94m({findMonster.HP} | {monMDandHP[monsterN][1]})\033[0m"))
                Call.level = "Spokesman"; Call.thing = True; Call.message = f"    \033[90mKilled {monsterN}:\033[0m \033[94m({findMonster.HP} | {monMDandHP[monsterN][1]})\033[0m"#could add this in changeMessage board
                User["Monsters Killed"].append(monsterN)
                monstersClear.pop(monster)
                monsterAttacks.armor = itemBuffs[1][User['Wearing']][0]
                mapErase(1)
                loadMap()
                return 0
    except:
        return 0
def consume(food):
    if food in itemBuffs[3]:
        if food in User["Inventory"]:
            if User["Health"] == User["Max Health"]: 
                print(colored(f"Health already full!, Can't eat {food}", "light_red")) 
            else: 
                User["Inventory"].remove(food)
                # User["InventoryCollected"].remove(food)
                User["Health"] += itemBuffs[3][food][0]
                if User["Health"] > User["Max Health"]: User["Health"] = User["Max Health"]
                mapErase(1);loadMap()
                print(colored(f"Consumed {food} and gained {itemBuffs[3][food][0]} health","light_blue"))
                return 0
        else: print("Item not in inventory")
    else: print("Item not in game")
    

def mainhand(type,item):
    ch = 0
    if type == "MH": ch = 2
    if type == "Wear": ch = 1
    if item in User["Inventory"] and item != User["Main Hand"] and item != User["Wearing"]:
        for obj in itemInfo[ch]:
            if item == obj and ch == 2:
                User["Main Hand"] = item
                takeItem.mainhand = int(itemBuffs[2][User['Main Hand']][0])
                mapErase(1);loadMap()
                print(f'Putting {item} in Main Hand')
                return 0
            elif item == obj and ch == 1:
                User["Wearing"] = item
                monsterAttacks.armor = itemBuffs[1][User['Wearing']][0]
                mapErase(1);loadMap()
                print(f'Equipping {item} on Body')
                return 0
    if item == User["Main Hand"] and ch == 2: print(f'{item} already in mainhand')
    elif item in User["Wearing"] and ch == 1: print(f"Already wearing {item}")
    elif checkItemInfo(item) == "nothing": print("Item not in game")
    elif item not in User["Inventory"]: print(f"Dont have {item} in inventory")
    elif ch == 1: print(f"Can't equip {item}")
    elif ch == 2: print(f"Can't put {item} in Mainhand")



def findItem(): #cut it into multiple definitions so its easier with new noun system
    #Checks if location has item, then puts item in inventory and deletes item from dictionary and biome items
    #if findItem.skip == True and findItem.c != True: erases(3)
    #Checks if position equals a pos of item alos checks if pick up command is used and pos is right
    try:
        for items in itemLoc:
            drops = list(itemLoc[items])
            if space == itemLoc[items] or space == drops[0]:
                if "DROP" in items: itemN = items.rpartition("DROP")[0]
                if "-" in items: itemN = items.rpartition('-')[0]
                else: itemN = items
                if takeItem.s:

                    #if findEnv.yes == False and findMonster.yes == False: erases(30); animation(Call.level, True, True, False)
                    #else: print(f"\n ")
                    print(f"Unbelievable, you come across a {itemN}! (Pick it up)")
                #map[9-(space[0]%10)][space[1]%10] = itemN[0]

                return items
        return "False"
    except:
        return "False"
def takeItem():
    takeItem.s, Call.erase, findItem.era  = False, False, 0
    wF, ch, item = words["itemFind"], Input.choice, findItem()
    #Make alternate for describing (DONE)
    gridI = gridItems[User["Current Biome"]]
    if "-" in item: itemN = item.rpartition('-')[0]
    else: itemN = item
    if "DROP" in item: itemN = itemN.rpartition('DROP')[2]
    if item != "False" and anys(ch.lower() ,wF[3:]):
        User["Inventory"].append(itemN); User["InventoryCollected"].append(itemN)
        itemLoc.pop(item)
        #Fix for later if armor becomes array
        gridIt = list(gridI[0]); gridNum = list(gridI[1])
        for x in range(0, len(gridI[0])):
            if gridIt[x] == item:
                break
        gridNum[x] = (gridNum[x] - 1)
        if gridNum[x] == 0:
            gridNum.pop(x)
            gridIt.pop(x);
        if item in itemDrop:
            itemDrop.pop(item)
        gridItems[User["Current Biome"]] = [gridIt, gridNum]
        specItemInfo(itemN)
        findItem.ItemMemory = itemN; findItem.era = 3
        # if Movement.pre == "D" and itemIsDroped:
        #     n = (space[0]) % 10; e = space[1] % 10
        #     map[9-n][e] = Movement.userImage
        itemIsDroped = False
        for drop in itemDrop:
            listDrop = itemDrop[drop]
            if space == listDrop[0]:
                Movement.pre = drop[0]
                itemIsDroped = True
                break
            #12/31 (Have error were map gets rid of door if item spawns under it)
        if itemIsDroped == False:
            Movement.pre = '\033[31m' + " " + '\033[39m'
        mapErase(1);loadMap()
        print(f"-------PICKING UP--------\n{itemN} added to your inventory!")
        # dropItem.count -= 1
    elif item != "False": specItemInfo(itemN)
    elif anys(ch.lower(), wF[3:]): print("Nothing to pick up Man!")
    else: print("Nothing to describe over here Dude!")
    takeItem.s = True
def scatterItem(t, envir, nS, nE, eS, eE, scatter : bool):
    try:
        if "monster" in t:
            monstersClear.clear(); t = monstersClear;
            if storyLevel.level >= len(storyNum):
                gridI = monsters[storyNum[len(storyNum) - 1]]
            else: gridI = monsters[storyNum[storyLevel.level]]

        elif "item" in t:
            t = itemLoc
            if scatter == True:
                itemLoc.clear();
                gridI = gridItems[envir]
        if scatter == True:
            itemArray = [];itemCounter = 1; stepCounter = 0;
            itemMultipliyer = gridI[1];
            for item in gridI[0]:
                itemCounter = 1
                for x in range(0, itemMultipliyer[stepCounter]):
                    newItem = (f'{item}-{itemCounter}')
                    itemCounter += 1
                    itemArray.append(newItem)
                stepCounter += 1
            for items in itemArray:
                t[items] = [random.randint(nS,nE - 1), random.randint(eS,eE - 1)]
        if t == itemLoc:
            for drops in itemDrop:
                spot = itemDrop[drops]
                spotList = spot[0]
                if User["Current Biome"] in spot[1]:
                    sizes = Call.biMap
                    leMap = sizes.getLength()
                    wiMap = sizes.getWidth()
                    itemLoc[drops] = spot[0]
                    n = (spotList[0]) % leMap
                    e = spotList[1] % wiMap
                    # if "Wall" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"\033[38;2;218;165;32m" + "Ⅱ" + "\033[0m")
                    #                                            #Add mechanic to destory walls. Make it so instead
                    # elif "Door" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"∏") #OF checking with each name make an array with all the names
                    #                                         #then make it so theres another array or in same 2d array it has picyure to place down
                    # elif "Crafting Table" in drops: Call.biMap.setStuffPos((leMap-1)-n,e,"🪵")
                    Call.biMap.setStuffPos((leMap-1)-n,e,str(drops[0]))
                    if spotList == space:
                        Movement.pre = str(drops[0])

    except:
        print("Did not run")
        time.sleep(5.5)
        return 0
def testForNewEnv():
    counter = 0
    for bObject in buildList:
        bounds = bObject.getCordinate()
        if not User["Current Biome"] == bObject.getName():
            if space[0] >= bounds[0] and space[0] < bounds[1] and space[1] >= bounds[2] and space[1] < bounds[3]:
                return buildList[counter]
        counter+=1
    return [Call.biMap, False]

def findEnv():
    findEnv.yes = False; counter = 0
    for bObject in buildList:
        bound = bObject.getCordinate()
        if not User["Current Biome"] == bObject.getName():
            if space[0] >= bound[0] and space[0] < bound[1] and space[1] >= bound[2] and space[1] < bound[3]:
            #Trying to make boundry lines for each qaudrant
            #Cehcks boundries for each environment location (Can save memory later by doing onyl whats touching)
                display1 = User["Current Biome"]; User["Current Biome"] = bObject.getName()
                display2 = "Entered Biome: {}".format(User["Current Biome"])
                Call.biMap = bObject
                scatterItem("item", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                scatterItem("monster", User["Current Biome"], bound[0], bound[1], bound[2], bound[3], True)
                mapErase(1);loadMap()
                print(f"--------------\nLeaving Biome: {display1}\n{display2}\n--------------")
                #Make a for loop to spawn monsters from old adventures if decide to use that ma=echanic (will be  lot of monsters but can change that)
                #Can also make a loop to give each place a new random amount of monsters, super eas
                #also need to make a thing to place stuff on map
                if (not User["Current Biome"] in User["Biomes Discovered"]):
                    User["Biomes Discovered"].append(User["Current Biome"])
                    print(f"New Biome Discovered!")
                #print(f'Monsters for Story: {s} are roaming across the land')
                arrB = [bound[0], bound[1], bound[2], bound[3]]
                return arrB
        counter +=1
    return False
def itemDesc():
    #Prints out the description of items that are only in the inventory
    c = 0; t = 0; cInv = User["Inventory"][:]
    print("."*8)
    for i in itemInfo:
        for j in i:
            if j in cInv:
                print(j + itemInfo[c][j])
                t = 0
                while t < len(cInv):
                    if cInv[t] == j:
                        cInv.remove(j)
                    t += 1
        c += 1
    print("."*8)
def arrayChecker(OG, inThis: list, lengths: list): #checks if array contains other elements by sorting them through magic
                              #use  with len function to make sure you  use apprpriate one
                              #Doesnt matter order

    sortedItems = []
    itemIndex, count = OG, 0
    thing = inThis.copy()
    for item in OG:
        if item in itemIndex[count] and item in thing:
            sortedItems.append(item)
            thing.remove(item)
            count += 1
    if sortedItems == OG and len(OG) == len(lengths): return True
    else: return False
def craftItem(create, inp): #can Change the whole dynamic where you type in the thing you want
                       #and then it checks if you have those items in your inventory
                       #and therfore dont need to write down all items
                       #leaves room for guessing and fun, but tedious if recipes are large
                       #Can add something to display recipee book for objects
    cho = Input.choice; buildTypes = itemCraft; name = "CRAFT"
    if anys(cho.lower(), words["craft"]): buildTypes = itemCraft;
    elif anys(cho.lower(), words["smelt"]): buildTypes = itemCook; name = "SMELT"
    if inp == False:
        creUp = string.capwords(create)
        arrCraft = creUp.split(", ")
    userInv = False; ItemArray = False; sortedItems = False
    for i in buildTypes:
        itemCount = sortItemCount(buildTypes[i], "add")
        if inp == False:
            ItemArray = arrayChecker(itemCount, arrCraft, arrCraft)
            sortedItems = arrayChecker(itemCount, User["Inventory"], arrCraft)
        elif create == i:
            userInv = arrayChecker(itemCount, User["Inventory"], itemCount)
        if (ItemArray == True and sortedItems == True) or userInv == True:# Tests if arrays match up and then gets rid of items and creates new
            for ele in itemCount:
                User["Inventory"].remove(ele)
            times = buildTypes[i]; itemList = []; tTwo = times[2]
            for x in range(tTwo[0]):
                User["Inventory"].append(i)
                User["InventoryCollected"].append(i)
                itemList.append(i)
            countItemList = sortItemCount(itemList, "None")
            print(f"|          |--[{name}ING]--|           |\n|          .............              |")
            time.sleep(0.3)
            print(f"|          [{name}ED:]                 |")
            print(f"|       {countItemList} |")
            findItem.ItemMemory = i
            return 0
        elif ItemArray: #TO DO(Problem is for cooking you have to say final product now what you want to put in, like if i say cook iron axe, it will say cant smelt it, you have to say smelt iron ore)
                        #change for singal smelts or add new book for smelting
            print("Do not have required items in inventory for {}".format(i))
            return 0
    if inp == True:
        if create in buildTypes:
            print(colored(f"Don't have enough items in inventory for {create}","light_red"))
            craftRecipe(create)
            print(colored(f"You only have:","light_red"))
            needs = []; listUI = list(User["Inventory"])
            craftItems = sortItemCount(buildTypes[create], "add")
            setUser = set(User["Inventory"])
            for i in craftItems:
                if i in setUser:
                    needs.append(f"{i} ({listUI.count(i)})")
                    setUser.remove(i)
            if needs == []: needs = "No Items"
            print(colored(f"->{needs}", "light_red"))
        else: print(f"Non craftable recipe for {create}")
    else: print("Not a craftable recipe!")
def craftRecipe(craftable): #Describes crafting recipee for whatever you put down
    cho = Input.choice; name = "Building"; buildT = itemCraft
    if craftable in itemCook: buildT = itemCook; names = "smelt for"; name = "smelt"
    elif craftable in itemCraft: buildT = itemCraft; name = "craft"; names = "craft"
    for ele in buildT:
        if craftable == ele:
            print(colored(f'To {names} {ele} You will need: \n{sortItemCount(buildT[ele], "count")}',"dark_grey"))
            return 0
    print(colored(f"Non {name}able item","light_red")) # Can write code to figure out which one        if its not in game or just not cratfable
def recipeBook(type): #make it so you can change to different recipe book and journals
    page = 1; sR = 0; eR = 4; lineDraw = True; erase = True; t = 0; cLine = 0
    if "Cook" in type: types= itemCook
    elif "Craft" in type: types = itemCraft
    elif "Item Locate" in type: types = itemLoc
    else: types = type
    print("")#Make a checker to see if it is a book in game
    keys = list(types)
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    while True:
        if erase:
            erases(cLine+1);cLine = 0
        if lineDraw and erase:
            print(" \n----------------------: Arrow keys to move left and right");cLine+=1
        if lineDraw:
            print("Page {}".format(page));cLine+=1
        lineDraw = False
        try:
            if erase:
                for x in range(sR, eR-1):

                    if "Item Locate" not in type:#FIX TO MAKE ANY BOOK
                        multType = types[keys[x]]
                        tTwo = multType[2]

                        print((f'({tTwo})'),keys[x], ": ",sortItemCount(types[keys[x]], "count")); cLine += 1
                    else:
                        print(keys[x], ":", types[keys[x]]); cLine += 1
                t = 0
        except: t = 1
        if erase: print("---------------------: Press 'Enter' to leave book \n  "); cLine+=2
        erase = True
        
        
        if key_listener.is_right_arrow_pressed():
            keyboard.Controller().release(keyboard.Key.right)
            if  t == 0: sR = eR-1; eR += 3; page+=1; lineDraw = True
            else: erase = False
        elif key_listener.is_left_arrow_pressed():
            keyboard.Controller().release(keyboard.Key.left)
            if sR - 3 > -1: eR -= 3; sR -= 3; page-=1; lineDraw = True
            else: erase = False
        elif key_listener.is_enter_pressed():
            input(" ")
            if (key_listener.is_enter_pressed()): erases(1)
            listener.stop()
            del key_listener
            return 0
        else: erase = False
    # listener.stop()

def breakItem():
    NorthEastAndObjectAtSpot = lookAhead()
    if User["Main Hand"] == "":
        print("Need to hold something to break")
        return False
    if NorthEastAndObjectAtSpot[2] != False and NorthEastAndObjectAtSpot[2] in itemDrops and not isinstance(NorthEastAndObjectAtSpot[2], KeyBlocks):
        # add ability to check for material and give user item broken or drop it
        #destroy item and grab it (TO-DO)
        floor = '\033[31m' + " " + '\033[39m'
        directionN = NorthEastAndObjectAtSpot[0]
        directionE = NorthEastAndObjectAtSpot[1]
        objectAtSpot = NorthEastAndObjectAtSpot[2]
        if objectAtSpot == floor:
            print("Nothing to break")
        else:
            ItemBlockChecker = heirarchyCheck(objectAtSpot,itemBuffs[2][User['Main Hand']][1])
            if  ItemBlockChecker[0] == False:
                print(colored(f"Not holding correct tool to break : \033[39m{objectAtSpot}","cyan"))
                print(colored(f"Need tool level of \033[31m{ItemBlockChecker[1]}\033[96m or higher","light_cyan"))
                print(colored(f"Current tool level is \033[31m{itemBuffs[2][User['Main Hand']][1]}", "light_cyan"))
                return False
            Call.biMap.setStuffPos(directionN,directionE, floor)
            mapErase(1);loadMap()
            print("Broke " + objectAtSpot)
            destroyedObject = getItemList(objectAtSpot)
            items = destroyedObject[0]
            countOfItems = destroyedObject[1]
            lists = [items,countOfItems]
           #Goes through list and adds item counts and items to inv
            for item in items:
                for x in range(countOfItems[items.index(item)]):
                    User["Inventory"].append(item)
                    User["InventoryCollected"].append(item)
            #Get the item and amount in nice to read string
            sorts = sortItemCount(lists, "count")
            print("And collected: ")
            print(sorts)
    else:
        print("Cant break there")

def build(item):
    if item == "nothing":
        print("Not a buildable item in the game")
        return False
    elif item not in User["Inventory"]:
        print("Item not in Inventory")
        return False
    else:
        for key in itemDrops.keys():
            if item == itemDrops[key][2]:
                Call.biMap.setStuffPos(Movement.spotN, Movement.spotE, key)
                loadMap()
                print(f"Building {item} on {space}")
                User["Inventory"].remove(item)
                Movement.pre = Call.biMap.getStuffPos(Movement.spotN, Movement.spotE)
                return True
        print(f"Cant Place {item}")
        return False

def dropItem(said):
    it = checkItemInfo(said)
    if it == "nothing":
        print("item does not exist")
        return False
    elif it not in User["Inventory"]:
        print("Item not in Inventory")
        return False
    if it in User["Main Hand"]: User["Main Hand"] = "";takeItem.mainhand = int(itemBuffs[2][User['Main Hand']][0])
    elif it in User["Wearing"]: User["Wearing"] = "";monsterAttacks.armor = itemBuffs[1][User['Wearing']][0];
    gridList = gridItems[User["Current Biome"]]
    gridItem = gridList[0]; gridNum = gridList[1]
    User["Inventory"].remove(it)
    it = (f'{it}-DROP{dropItem.count}')
    dropItem.count += 1
    itemDrop[it] = [[space[0], space[1]],[User["Current Biome"]]]

    gridItems[User["Current Biome"]] = [gridItem, gridNum]
     #(TO DO) Change to use bi map so now i keep track on whatever biome I am on
        #for ele in text:
    bound = Call.biMap.getCordinate()
    # if space[0] >= bound[0] and space[0] < bound[1] and space[1] >= bound[2] and space[1] < bound[3]:
    scatterItem("item", User["Current Biome"], bound[0],bound[1],bound[2],bound[3], False)
    mapErase(1);loadMap()
    leMap = Call.biMap.getLength()
    wiMap = Call.biMap.getWidth()

    # if "Wall" in it: Movement.pre = "\033[38;2;218;165;32m" + "Ⅱ" + "\033[0m"
    #  #Add mechanic to destory walls (░♀▒▓█▄▀▐▌)
    #                                     #DO the array thing so each specialty item has a special object font,
    #                                     #like walls and doors and EVEN ANY ITem has its unique texture
    # elif "Door" in it: Movement.pre = "∏"
    # elif "Crafting Table" in it: Movement.pre = "🪵"
    Movement.pre = it[0]
    n = (space[0]) % leMap
    e = space[1] % wiMap
    Call.biMap.setStuffPos((leMap-1)-n,e, Movement.userImage) #(Fixed) Fix so correct letter is displayed when you pick up
    print(f"~~~Dropping {it.rpartition('-')[0].rpartition('DROP')[0]} at [{space[0]}, {space[1]}]~~~")
    return True
def addItem(item, num :int):
    x = 0; item = string.capwords(item)
    while x < len(itemInfo):
        for list in itemInfo[x]:
            if item == list:
                for x in range(0, num):
                    User["Inventory"].append(item)
                    User["InventoryCollected"].append(item)
                print("Adding {} to your inventory {} times".format(item, str(num)))
                findItem.ItemMemory = item
                return 0
        x += 1
    print("Not an item in the game")
def Info():
    print(f'Health: {User["Health"]}')
    print(f'Current Biome: \n{User["Current Biome"]}')
def invLoc():
    Inventory1 = copy.deepcopy(Inventory)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(colored(f'Main Hand: ({User["Main Hand"]}) \nWearing: ({User["Wearing"]})',"light_green"))
    for i in User["Inventory"]: #Can just do this when retrieve item so it doesnt have to use space
        CT = 0
        for j in Inventory:
            if (test0 := (i in itemInfo[CT] and i) or
                        (i.rpartition("-")[0] in itemInfo[CT] and i.rpartition("-")[0])):
                if test0 in itemInfo[CT]:
                    Inventory1[j].append(test0)
                    break
            CT+=1
    arrJ = []; sortU = []
    for name in Inventory: arrJ.append(name)
    for x in range(0, len(arrJ)): #fix to use itemCountSort()
        sortU = []
        for item in Inventory1[arrJ[x]]:
            itemC = (f'{item} ({Inventory1[arrJ[x]].count(item)})')
            if itemC not in sortU:
                sortU.append(itemC)
        print(f'{arrJ[x]}: {sortU}')
    print("\033[m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def storyAdv(): #Prints out story for levek you Are on


    lev = storyLevel.level
    if lev >= len(storyNum):
        Call.level = "Spokesman"; Call.message = f"    Completed all levels"
        changeMessage(f"""#You Rock!!!\n$Lets Celebrate!!!!\n$Have a slice of cake""")
        animation("Spokesman", True, False, Call.message)
        return True
    else:
        print(f'To complete Story: {storyNum[lev]}')
        storyList(story[storyNum[lev]] , False, 0,0,0,0,0, True)
        return False
def storyLevel(check): #Sets what level you are on. Pops all other Stories so youi only can do one Need to make deep copy
    storyLevel.skip = False
    try:
        if check == True:
            storyLevel.level += 1
            User["LVL"]=storyLevel.level
            if storyLevel.level < len(storyNum):
                Call.level = storyNum[storyLevel.level];
                animation(storyNum[storyLevel.level], True, False, False)
                if storyLevel.level == 1: User["Max Health"] += 20; User["Health"] = User["Max Health"]
                time.sleep(0.3)
                bA = User["Current Biome"]
                for bObject in buildList:
                    #for ele in text:
                        bA = bObject.getCordinate()
                        if User["Current Biome"] == bObject.getName():
                            
                            scatterItem("monster", storyNum[storyLevel.level], bA[0], bA[1], bA[2], bA[3], True)
                            time.sleep(0.3)
                            mapErase(1)
                            loadMap()
                            mapErase(1)
                            print(f"----Starting Adventure: {Call.level}----\n|\\/Ferocious new Monsters Roam the Land\\/|")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input("")
                input("")
                print("\r\033[A", " "*63, "\r\033[A", " "*63)

                time.sleep(0.6)
                return storyNum[storyLevel.level]
    except: storyLevel.level = storyLevel.level
    if storyLevel.level >= len(storyNum): storyAdv()
    else: return 0
def storyObjs(type): #Returns the array of items needed to achieve compeltion of level
    arrRew = type
    itemArray = []; stepCounter = 0; itemMultipliyer = arrRew[1];
    for item in arrRew[0]:
        if item not in itemArray:
            for x in range(0, itemMultipliyer[stepCounter]):
                itemArray.append(item)
        stepCounter += 1
    return itemArray
def changeMessage(message) :
    t  = animations["Spokesman"]
    animations["Spokesman"] = [t[0], message, t[2], t[3], t[4], t[5], t[6], t[7]]
def checkStoryComplete(): #Checks if completion happens, and then triggers change of level
    try:
        arrSt = sortItemCount(storyBoard[storyNum[storyLevel.level]], "add")
        monSt = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "add")
        levelNum = storyLevel.level
        objCoLe = arrayChecker(arrSt, User["InventoryCollected"], arrSt)
        MoCoKilled = arrayChecker(monSt, User["Monsters Killed"], monSt)
        if objCoLe and MoCoKilled and levelNum + 1 <= len(storyNum):
            awardAdd = sortItemCount(storyAward[storyNum[storyLevel.level]], "add")
            awardCount = sortItemCount(storyAward[storyNum[storyLevel.level]], "count")
            erases(30)
            time.sleep(0.2)
            os.system('cls')
            print("<-","-"*40,"->")
            changeMessage(f"""#Congrats on completing level: {storyNum[storyLevel.level]}\n$For your acomplishment you will recieve: \n$->{awardCount}\n$(press 'f' to go to next page) """)
            animation("Spokesman", True, False, f"    Rewarding System for completing {storyNum[levelNum]}:")
            key_listener = MyKeyListener()
            listener = keyboard.Listener(
                on_press=key_listener.on_press,
                on_release=key_listener.on_release)
            listener.start()
            while (key_listener.is_f_pressed() == False):
                if (key_listener.is_f_pressed()):
                    break
            listener.stop()
            erases(20)
            print("<-","-"*40,"->")
            try:
                for item in awardAdd:
                    User["Inventory"].append(item)
            except: erases(1)
            storyLevel(True)
    except:
        return False
def sortItemCount(key, countOrAdd):
    countItemsinKey = []; counter = 0
    if "count" in countOrAdd or "add" in countOrAdd: k = key[0]; tea = True
    else: k = set(key); tea = False; listK = list(key)
    for item in k:
        if tea: count = key[1]
        if "count" in countOrAdd:
            countItemsinKey.append(f'{item} ({count[counter]})')
        elif "add" in countOrAdd:
            for x in range(0, count[counter]):
                countItemsinKey.append(item)
        else:
            countItemsinKey.append(f'{item} ({listK.count(item)})')
        counter += 1
    return countItemsinKey
def checkItemInfo(said):
    saidObj = "nothing"
    for row in itemInfo:
        for obj in row:
            if obj in string.capwords(said):
                saidObj = obj
    return saidObj

def Call():

    #to save space for else statement maybe make the entire
    #thng a for loop that checkswat you wrote against the names
    #of other functions. can store dictionary with names of all functions
    #an then they trigure the funtions assigned to dictionry
    #mamish im a genius
    com, direct = Input.choice, words["direction"]
    if "animate" in com:
        Call.thing = False; help.ran = True
        # if not storyLevel.level >= len(storyNum):Call.level = storyNum[storyLevel.level];
        # else: Call.level = "Spokesman" #animation("Beginning", True, False)
    elif anys(com.lower(), words["story"]):
        if not storyLevel.level >= len(storyNum):Call.level = storyNum[storyLevel.level]; Call.message = False
        else: Call.level = "Spokesman";
        Call.thing = True; help.ran = True#storyAdv()
    elif "quest" in com and "/quest" not in com: help.ran = True;Call.level = "Jeffery"; Call.thing = False; #Call.message = False#Change for quest
    skip = True
    #erases(30);  #Fix blinking issue (Fixed without system clear a lot better)!!!!!!
            #Can make a number that calculates how many lines are printed
            #dont need to rewrite quest objective every times

        #change for quest system later
        #Make it so cant animate anymore after reaching max quests
        #make it soa  guy tells you, you have completed the game
        #(TO DO) Make a visible board that gets printed eveyrtime
        #(TO DO) ADD chat features with the guy!!!!
    if not "animate" in com and not "quest" in com or "/quest complete" in com: Call.thing = True
    mess = False
    if not "/quest complete" in com:
        if "quest" in com: mess = False
        else: mess = Call.message
    if help.ran == True: 
        os.system('cls')
        print("<-","-"*40,"->")
        animation(Call.level, True, Call.thing, mess); help.ran = False
    if not com == "":
        #print("\033[K")
        mapErase(40)
        #animation(Call.level, True, Call.thing, mess)
        # input("")
        # erases(1)

        loadMap()
    if Call.thing == False: Call.thing == True
    Call.skipe = False
    ##; findItem.skip = False; #Call.move = True
    if "again" == com: 
        Input.choice = Call.memory

        Call()
    elif Input.choice == "/item locate": #Cheats for all items in game (For testing)
        print(itemLoc)
        recipeBook("Item Locate") #not really needed annoying to flip through, but cleaner
    elif com == "/item drop":
        print(itemDrop)#Maybe create recipe book for itemDrop to Super Easy
    elif com == "/item count":
        try:
            gridI = gridItems[User["Current Biome"]]
            print("Items", gridI[0], "\nCount", gridI[1])
        except: print("Unfinished items in that locations")
    elif Input.choice[0:7] == "/damage":
        try:
            User["Health"] -= int(Input.choice[8:])
            mapErase()
            loadMap()
            print(colored(f'Took damage: {int(Input.choice[8:])} off of User',"red"))
        except: print("Wrong Input for taking damage")
    elif Input.choice[0:5] == "/heal":
        try:
            User["Health"] += int(Input.choice[6:])
            if User["Health"] > 100: 
                User["Health"] = 100
            mapErase()
            loadMap()
            print(colored(f'Healed: {int(Input.choice[6:])} to User',"light_green"))
        except: print("Wrong Input for healing")
    elif Input.choice == "/build locate": #Cheats for environment locations of everywhere
        for i in buildList:
            print(i.getName(),": ",i.getCordinate())
    elif com[0:9] == "/teleport": #make it later so by typing /you get list of commands
                                  #Make it so dictionary has master commands and does stuff,
                                  #but maybe not since each command does something
        teleport()
    elif com[0:4] == "/add":
        try:
            amount = com[com.index("(")+1: com.index(")")]
            addItem(com[com.index(') ') + 1: ], int(amount))
        except:
            print("Wrong input, try using brackets /add '(#) item'")
    #Call.level = "Jeffery"; Call.thing = False#Placeholders to test head system (Change for what quest you are doing)
        #animation("Jeffery", True, False) #Make a definition that tells you what quest you are doing
        #Or/and make a book that keeps track of all the quests you are doing
    elif com == "/clear":
        os.system('cls')
        print("<-","-"*40,"->",flush=True)
        animation(Call.level, True, Call.thing, mess)
        input("")
        erases(1)
        mapErase(1)
        loadMap()
        mapErase(1)
    elif com == "/story": #Can make system where if you kill all monsters on map you get bonus
        print(f'{storyLevel.level}\n{len(storyNum)}')
        if (storyLevel.level < len(storyNum)):
            gridI = sortItemCount(storyBoard[storyNum[storyLevel.level]], "count")
            gridMon = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "count")
            print(f'To complete {storyNum[storyLevel.level]}\nItems/Count: {gridI}')
            print(f'Monsters to kill/Count {gridMon}')
        else: print("Completed all levels")
    elif com == "/quest complete":
        if not storyLevel.level >= len(storyNum):
            Call.message = False
            questArrItem = sortItemCount(storyBoard[storyNum[storyLevel.level]], "add")
            for item in questArrItem:
                User["Inventory"].append(item)
                User["InventoryCollected"].append(item)
            questArrMonster = sortItemCount(storyBoardMon[storyNum[storyLevel.level]], "add")
            for mon in questArrMonster:
                User["Monsters Killed"].append(mon)
            print(f"Completing {storyNum[storyLevel.level]}")
        else: os.system('cls'); print("<-","-"*40,"->");storyAdv(); mapErase(1); loadMap()
    elif com == "/monster":
        print(monstersClear)
        if not storyLevel.level >= len(storyNum): print(sortItemCount(monsters[storyNum[storyLevel.level]], "count"))
        else: storyAdv()
    elif com == "/setMap":
        print(Call.biMap.getName())
    elif ("open" in com or "unlock" in com):
        getObject = lookAhead(True)
        if isinstance(getObject[2], KeyBlocks):
            if getObject[2].getKeyLevel() in User["Inventory"]:
                print("Opening Gate")
                Call.biMap.setStuffPos(getObject[0], getObject[1], getObject[2].getLook())
                Call.biMap.deleteObject(getObject[0], getObject[1])
                
                # del getObject[2].setIsBlocking(False)
                mapErase(1);loadMap()
                print(f"Opened {getObject[2].getLook()} with {getObject[2].getKeyLevel()}")
                del getObject[2]
            else:
                print(f"Do Not have required: ({getObject[2].getKeyLevel()}) to open gate")
            
        else: print("Nothing to open")

    elif anys(com.lower(), words["insults"]): print("You have a tiny dick")
    elif anys(com.lower(), words["shoot"]): shoot()
    elif anys(com.lower(), words["breaking"]): breakItem()
    elif "discover" in com: print(User["Biomes Discovered"])
    elif "quest" in com: h = ""#Call.message = False
    elif "animate" in com: h = ""#Call.message = False;#Call.level = storyNum[storyLevel.level]; Call.thing = False#animation("Beginning", True, False)
    elif anys(com.lower(), words["story"]): h = ""#Call.message = False#Call.level = storyNum[storyLevel.level]; Call.thing = True; #storyAdv()
    elif "help" in Input.choice: help()
    elif Input.choice == "info": Info()
    elif Input.choice == "item info": itemDesc()
    elif anys(com.lower(), words["building"]):build(checkItemInfo(com))
    elif "drop" in com or "get rid of" in com: dropItem(string.capwords(com))
    elif Input.choice == "exit":
        while True:
            mapErase(1)
            loadMap()
            exits = input("Are you sure you want to exit ('y' or 'n')").lower()
            if exits == "y" or "yes" in exits: print("Shalom"); exit()
            elif exits == "n" or "no" in exits: break
    elif (anys(com.lower(), words["recipeCraft"]) or anys(com.lower(), words["recipeCook"])) and "crafting table" not in com:#"recipe" in com or "cook" in com or "craft" in com or "ingredient" in com :
        #Make a list of nouns and check if {com} is any of the nouns pro strats - Done!!!!! Great invention past hershel
        choice = words["recipeCraft"] #change for recipesss
        if choice[2] == com[0: 7].lower(): print("Cant find recipe for something blank")
        elif "book" in com.lower() and anys(com.lower(), words["recipeCraft"]): recipeBook("Craft")
        elif "book" in com.lower() and anys(com.lower(), words["recipeCook"]): recipeBook("Cook")
        else: craftRecipe(checkItemInfo(com))
    elif anys(com.lower(), words["craft"]) or anys(com.lower(), words["smelt"]): #Add so you can do 'craft Bomb' an it checks if you have
                                  #items and does same thing as craft items but dont have to type in all items\
                                  #Faster!!!1
        if checkItemInfo(com) == "nothing":
            #Add user checkability to see if person is on furnace
            if anys(com.lower(), words["craft"]): print("Type in items you want to craft together (seperate items with ', '): ")
            else: print("Type in items you want to cook or smelt together (seperate items with ', '): ")
            craft = input("->")
            if craft != "": craftItem(craft, False);
            else: "Crafting Nothing"
        else: craftItem(checkItemInfo(com), True)
    elif com == "killed": killed = sortItemCount(User["Monsters Killed"], "None");print(f'Monster kill list: \n{killed}') #fix
    elif ("check" in com or "what" in com or "?" in com) and anys(com.lower(), words["hand"]): print(f'Mainhand: \n{User["Main Hand"]}\nDamage {int(itemBuffs[2][User["Main Hand"]][0])}\nTool Level: {itemBuffs[2][User["Main Hand"]][1]}')
    elif anys(com.lower(), words["consume"]):
        food = checkItemInfo(com)
        if food != "nothing": eat = food
        elif food == "nothing" and findItem.ItemMemory != "": eat = findItem.ItemMemory
        else: eat = "nothing"
        consume(eat)
    elif anys(com.lower(), words["hand"]):
        if checkItemInfo(com) != "nothing": item = checkItemInfo(com)
        elif checkItemInfo(com) == "nothing" and findItem.ItemMemory != "": item = findItem.ItemMemory
        else: item = "nothing"
        mainhand("MH", item)
    elif ("check" in com or "what" in com or "?" in com) and anys(com.lower(), words["wear"]): print(f'Wearing: \n{User["Wearing"]}\nArmor Protection: {itemBuffs[1][User["Wearing"]][0]}')
    elif anys(com.lower(), words["wear"]) or ("put" in com.lower() and "on" in com.lower()): #maybe make it so it has to be first word
        if checkItemInfo(com) != "nothing": armor = checkItemInfo(com)
        elif checkItemInfo(com) == "nothing" and findItem.ItemMemory != "": armor = findItem.ItemMemory
        else: armor = "nothing"
        mainhand("Wear", armor) #Problem is that is check for if item in armor not equal so if share name is
                                #is similar like stone armor or stone then it will break (fix by changing to equal, but problem is armorwil
                                # later be an array so wont work)
    elif anys(com.lower(), words["inv"]): invLoc()
    elif anys(com.lower(), words["locate"]): location()
    elif anys(com.lower(), direct[0:9]) or ("n"==com or"e"==com or"s"==com or"w"==com) or (("move" or "step" in com) and anys(com.lower(), direct[0:9])):
        Movement() #Fix Find item and make a definiton for any(word) so its not super long (any(com.lower() == word for word in direct[9:13]))
        #if findItem.skip == False:
    elif anys(com.lower(), words["itemFind"]): takeItem()
    else:
        Call.skipe = True
        if not com == "":
           # erases(2)
            print(wrongKey[random.randint(0, 4)]); Call.first = True
        else: print("\033[A\033[A"," "*63, end = "\r")
    checkStoryComplete()
    Call.memory = Input.choice
    Input()
def Input():
    if findItem.skip != True:
        Input.choice = input("\nAdventurer Input: ")
    findItem.skip = False
    Call()
Call.biMap = mapGreenland
try:
    os.system('cls')
    mess = ""
    # numList = ["⓪","➀","➁","➂","➃","➄","➅","➆","➇","➈","➉","⑪","⑫","⑬","⑭","⑮","⑯","⑰","⑱","⑲","⑳,"㉑","㉒","㉓","㉔","㉕","㉖","㉗","㉘","㉙","㉚","㉛","㉜","㉝","㉞","㉟","㊱","㊲","㊳","㊴","㊵","㊶","㊷","㊸","㊹","㊺","㊻","㊼","㊽","㊾","㊿"]
    # print(numList)
    Call.inits = True
    # while True:
    #     os.system('cls')
    #     type = input("\nAre you running this on Command Prompt or similar?\n(Windows CMD or Mac OS)\nBreaks game if given incorrect answer!!!!\n->")
    #     mess = type.lower()
    #     if "y" == mess or "yes" in mess: inits = True; Call.inits = True; break
    #     elif "n" == mess or "no" in mess: inits = False; break
    # if Call.inits == True: print("Running init")

    os.system('cls'); storyLevel.skip = False;  help.ran = False; dropItem.count = 1
    Call.level = "Beginning"; Call.thing = True; Call.direction = True; Call.message = False; Input.f = True
    storyLevel.level = 0;findMonster.list = []; findMonster.HP = 0; findMonster.DG = 0; findItem.era  = 0
    space = [4,4]; Movement.spotN = 5; Movement.spotE = 4
    # Movement.saveN = 9; Movement.saveE = 9;
    findItem.ItemMemory = ""; takeItem.s = True; findEnv.yes = False
    Call.memory = ""
    storyBC["Beginning"] = storyBoard["Beginning"][:]; User["LVL"]=storyLevel.level;Call.skipe = False
    recipeBook.choice = 1; findItem.skip = False; Call.first = True;
    Movement.pre = '\033[31m' + " " + '\033[39m'; Movement.userImage = "p"
    monsterAttacks.armor = itemBuffs[1][User['Wearing']][0];takeItem.mainhand = int(itemBuffs[2][User['Main Hand']][0])
    scatterItem("item", "Greenland", 0, 9, 0, 9, True)
    scatterItem("monster", "Greenland", 0, 9, 0, 9, True)
    Input.f = False
    print("<-","-"*40,"->")
    time.sleep(0.3)
    animation("Beginning", True, False, False)
    input("")
    # time.sleep(0.8)
    # print("Type 'help' for help")
    # time.sleep(0.2)
    Input.choice = "start"
    Movement()
    # os.system('cls')
    # print("<-","-"*40,"->")
    # animation(Call.level, True, Call.thing, mess)
    # input("")
    erases(1)
    mapErase(1)
    loadMap()
    Call()
    # loadMap()
    # Input()
except:
    print(" ")
    print("End of the Most Glorious Adventure")
    exc_type, exc_value, exc_tb = sys.exc_info()
    # print the error message and line number
    print(exc_type, exc_value, exc_tb.tb_lineno)
    traceback.print_exc()
