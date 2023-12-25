from storyAdventure import *;   import time; import keyboard; import random
import sys
from colorama import init; from colorama import Fore, Back, Style
if inits == True: init()
if sys.stdin and sys.stdin.isatty():
    # running interactively
    hi = ""
# else:
#     with open('output','w') as f:
#         f.write("running in the background!\n")
def storyList(type, talk, animationEyeBrow, animationEyes, animationChin, animation1, animation2, wait):
    storyletter = []; lineAnimation = animationEyes; nextAnimation = animationEyes; line = 0; count = 0; s = animationEyeBrow; t = animationEyeBrow; isOnCount = True; ani = animation1
    for i in type:
        if  i == "$" or i == "#":
            if talk and i == "$":
                if count < 1:
                    storyletter.append(f"&\r                                                                                               \rt{nextAnimation}    t")
                else: 
                    storyletter.append(f"&\r                                                                                               \r{nextAnimation}    ")
            elif talk and i == "#":     
                storyletter.append(f"\r{t}    ")
            line+= 1    
        elif talk and count % 5 == 0:
            isOnCount = not isOnCount
            if isOnCount and not wait == True: ani = animation1
            else: ani = animation2
            if line >= 0:
                if line == 1:
                    lineAnimation = animationEyeBrow; nextAnimation = animationEyes
                    storyletter.append(f"*\r\n\n{ani}    \r\033[A\r\033[A{lineAnimation}    ")
                if line == 2:
                    lineAnimation = animationEyes; nextAnimation = ani
                    storyletter.append(f"*\r\n{ani}    \r\033[A{lineAnimation}    ")
                if line == 3:
                    lineAnimation = ani; nextAnimation = animationChin
                    storyletter.append(f"*\r{ani}    ")
                if line == 4:
                    lineAnimation = animationChin; nextAnimation = "                    "
                    storyletter.append(f"*\r\033[A{ani}   \r\n{lineAnimation}    ")
                if line == 5:
                    lineAnimation = "                    "; nextAnimation = """"""
                    storyletter.append(f"*\r\033[A\033[A{ani}   \r\n\n{lineAnimation}    ")
            storyletter.append(i)#Make math
        else: storyletter.append(i)
        count += 1  
    lastWritten = []
    #time.sleep(0.3)
    keyboard.release("Enter")
    for i in storyletter:
        if talk and not wait == True: 
            if keyboard.is_pressed("s"): time.sleep(0.0000000000000000001)
            elif keyboard.is_pressed("x"): time.sleep(0)
            else: time.sleep(0.02)
        if '*' in i and '$' not in i:
            print(f"{i[1:]}", end = "", flush= True)
            for lastLet in lastWritten:
                if '*' not in lastLet and '&' not  in lastLet: print(lastLet, end = "", flush= True)
        else:
            if '&' in i or '$' in i:
                lastWritten = []
                if talk: print(i[1:], end = "", flush= True)
            else: print(i, end = "", flush= True)
            lastWritten.append(i)
    print('\n\r', flush= True)
    keyboard.press("Enter")

Jeffery_AnimationHair =       """    \33[93m/////////\033[0m"""
Jeffery_AnimationBrow =       """    \033[0m|-\033[30m\33[1m~~\033[0m-\033[30m\33[1m~~\033[0m-|"""
Jeffery_AnimationEye =        """    \033[0m|-\33[36m[]\033[39m-\33[36m[]\033[39m-|"""

Jeffery_AnimationCloseMouth = """    \033[0m|--\033[31m( )\033[0m--|"""
Jeffery_AnimationMouthMove =  """    \033[0m|--\033[31m< >\033[0m--|"""

Jeffery_AnimationChin =       """    \033[0m\_______/"""
questsJ = storyQuests["Jeffery"]
questsJ = questsJ[0]
def animation(part, bools: bool, waitTime, stringorNot):
    parts = animations[part]
    if stringorNot != False: print(parts[0], end = f"{stringorNot}\n")
    else: print(parts[0], end = f"    {part}'s Quest: ('x' to skip, 's' to fast forward)\n", flush= True)
    print(parts[3], flush= True)
    print(parts[4], flush= True)
    print(parts[7], flush= True)
    print(parts[5], end = '\r', flush= True)
    print("\033[A\r\033[A\r\033[A\r\033[A", flush= True)
    runAnimation(parts, bools, waitTime)
def runAnimation(type, TorF: bool, wait):
    # if stringYorN == True: type1 = type; print("Geshmach"); time.sleep(2)
    # else: type1 = type[1] 
    return storyList(type[1], TorF, type[3], type[4], type[5], type[6], type[7], wait)
try:
    animations = {
        "Beginning" : [Jeffery_AnimationHair, story["Beginning"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "A New Leaf": [Jeffery_AnimationHair, story["A New Leaf"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "The Might of the Novice" : [Jeffery_AnimationHair, story["The Might of the Novice"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "Jeffery" : [Jeffery_AnimationHair, storyQuests["Jeffery"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "Spokesman" : [Jeffery_AnimationHair, "#jkfshfjkafhsjkhfk hfkhskhfkjhs\n$ggdds\n$dgfgd\n$nk", True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth]#
    }
except: 
    animations = {
        "Beginning" : [Jeffery_AnimationHair, story["Beginning"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "A New Leaf": [Jeffery_AnimationHair, story["A New Leaf"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "The Might of the Novice" : [Jeffery_AnimationHair, story["The Might of the Novice"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
        "Jeffery" : [Jeffery_AnimationHair, storyQuests["Jeffery"], True, Jeffery_AnimationBrow, Jeffery_AnimationEye, Jeffery_AnimationChin, Jeffery_AnimationMouthMove, Jeffery_AnimationCloseMouth],
    }
#TO DO!!! ADD chat feautures