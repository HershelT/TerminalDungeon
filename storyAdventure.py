from biomeMaps import *
import math; import random
# map = [
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["►", "*","*","*","*","*","*","*","*","*"]
#     ] 
gl = setMap("Greenland",0, 10, 0, 10)
gl.setStuffPos(9, 0, "►")
for x in range(4, 7): gl.setStuffPos(x,4, "Ⅱ")
#Create new maps for each biome and can world build from there
#can create individual items on island

#create each new map as new map
map = gl.getMap()#Change whole system of cordinates to just spots on map and now i can add and destroy stuff on map
nMap = setMap("Greenland",0, 10, 0, 10)
for x in range(4, 7): nMap.setStuffPos(random.randint(0, nMap.getLength()-1
),4, "Ⅱ")
#newMap = nMap.getMap()
#new setMap object 

OGMap = [  #MAKE Walls Randomly generate and make sure there is always an opening
            #This can lead to the random biome generation and new item spawn system
            #Pretty easy to make random wall generation and make sure it doesnt generate on items
            #Or make each biome have different maps which would be cool. each biome can also have different
            #buildings
            #Chacrters to use: ※ Ω ₡ Ⅲ Ⅷ Ⅱ [░-Change to walls or path][
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["░", "░","░","░","Ⅱ","░","░","░","░","░"],
    ["░", "░","░","░","Ⅱ","░","░","░","░","░"],
    ["░", "░","░","░","Ⅱ","░","░","░","░","░"],
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["░", "░","░","░","░","░","░","░","░","░"],
    ["►", "░","░","░","░","░","░","░","░","░"]
    ]


# [
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","Ⅱ","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"],
#     ["*", "*","*","*","*","*","*","*","*","*"]
#     ]  
#For lists of items i want to do same thing i did for item spawn by doing 2d array and making 
#second array make it amount of items (Could even be a random amount (Or do random for later levels))
storyBoard = { #Items to collect to get reward
        #Can do the same thing i did for spawning items so i dont have to write number of times
        #Genius use it for everything
        
    "Beginning" : [["Stick", "Stone"],[1,3]],
    "A New Leaf" : [["Bomb"],[2]],
    "The Might of the Novice" : [["Apple", "Iron Armor", "Iron Axe"],[3, 1, 1]],
}

inits = False
storyNum = {
    0 : "Beginning",
    1 : "A New Leaf",
    2 : "The Might of the Novice",
}
storyBC = { #Dont need this if using numbers
    #Empty list that is used to place storyBoard as advhievments are unlocked and story progresses

}
storyQuests = { #Other quests from missions from people you come across
#Find people and they give you quests with their name and if you find someone else
#you can change quests and once quest is found the quest is set to "complete"
#And it checks if it is complete or it runs that quest and you have to return to the guy with the items
#Make a dialouge mode with the player that loops until he says exit or selects a mission
#Make it so it can spawn certain animals or items to collect:
#Make it so there is a counter for how many items are collected and make a quest data
#like it can spawn ten sheep randomly in the environment and you have to find them
#[Quest message (0)],[items (1)], [how many you have to collect (2)], [Item Rewards (3)], [how many items you get (4)], [#Location of Jeffery (MAYBE) (5)] len = 6
#make a scatter quest charcters feauture or mae them in designated locations
#Make reward for completing quests
#When get item, adds to quest items. And deletes when new quest, but then if middle of other quest you have to do it again
#Checks for collecting quest specific items and if that quest is on and if those items are in quests: if the are quest items they get added to quest bag 
# Otherwise they go into inventory. however, this only works for non items, but its great because i do not need 
# Those items for player just for quests so you can pikc up random stuff.    
    "Jeffery" : (f""""#OH Dearest ME!\n$I have lost my dearest sheep and cant cope without them\n$Please I beg you to collect 5 of my lost sheep """)

#{NEW 2023 OCtober}
#Can MAke it so when handed a quest you get a public variable that now adds a check each turn to see if you 
#Did quest. like every ove it will check if oyu got certain items or killed monsters from that point on
#will check whats in storyObj,

}
storyObj = {
    "Jeffery" : [["Sheep"],[5],["Iron Axe"],[1],[5, 5]],
}
story = {
    "Beginning" : (f"""#For a lad begins a journey, but a man becometh you! \n$To maketh man out of you aquire those that answer thy riddles:
$->Flick your wrist, and you shall see me skip across thy pond 3 TIMES. \n$->I grow from trees, but STICK in place """),
    "A New Leaf" : (f"""#Sizzle Sizzle. Kaboom Kaboom. \n$->Figure out what I am and I will Explode in hapinnes\n$"""),
    "The Might of the Novice" : (f""""#'The apples ate the cheese' - Hunger Games, \n$I cut down tree with an Iron fist and fight with my iron armor at night
$->Find the items that complete the messages\n$"""),
    
    
    #"Complete Message" : (f"" )
}
storyComplete = {
    
}

storyAward = { #giuves award based on compeltion and also make it you have to complete fighting monster award
    "Beginning" : [["Stone", "Rock", "Stick", "Pine Arrow", "Iron Armor", "Iron Ingot"],[2, 1, 6, 3, 4, 1, 4]],
    "A New Leaf" : [["Bomb", "Frozen Cow", "Stone", "Pine Bow", "Iron Axe",],[3, 4, 5, 1, 1]],
    "The Might of the Novice"  : [["Aragon's Blade", "Raw Egg", "Omelet", "Iron Ingot", ],[1, 3, 4, 7]],
}


#Make a story somehow that sends you on an adventure to 
#collect items and defeat boses. It has a checklist array for 
# everything collected and and enemies defeated. make a user input for story 
#completion and get awards and stuff
