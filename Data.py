import random
from biomeMaps import *
User = {
    "Health" : 100, #users current health
    "Max Health" : 100, #This is what will be used to determine how much health the person can max out at
    #Starting Inventory
    "Inventory" : ["Weathered Tunic", "Wood Sword", "Diamond Pickaxe"],
    "InventoryCollected" : ["Weathered Tunic", "Wood Sword"],
    "Monsters Killed" : [],
    
    "Current Biome" : "Greenland",
    "Wearing" : "Weathered Tunic", #What armor the person is currently wearing
    "Main Hand" : "Diamond Pickaxe", #What item the person wants to use
    "Quest" : [],
    "Biomes Discovered" : ["Greenland"],
    "LVL" : 12,
    "Permanent Damage Buff" : "", #Make a skill tree with experience or gold or both to 
    
    "Permanent Armor Buff" : "",  #Unlock permanent attack damage or better damage with swords or axes
                                  #Genius idea to create a leveling up and skill tree
                                  #And make a way to look at everything and make it fun.

}


Inventory = { #Used to determine the rows and what each item is from invLoc() method
    "\033[33mUtilities" : [],
    "\033[90mWearables" : [],
    "\033[35mWeapons" : [],
    "\033[94mConsumables" : [],
}
Inventory1 = {
    #Empty inventory thst gets copied from Inventory for invLoc()
}
startRandom = {
    0 : "Do Something, unlike my Lazy grandfather ", 
    1 : "What are you waiting for, lets go ",
    2 : "Lets get ready to rumble ",
    3 : "I AM WAITING ",
    4 : "YOU SHALL DO SOMETHING "
}
wrongKey = {
    0 : "Try again Fool ", 
    1 : "Oops the Wizard couldn't find that command ",
    2 : "God punishes you for wrong key ",
    3 : "Welp, that did nothing ",
    4 : "You use nothing, it wasnt't very effective "
}
# buildGrid = [
#     #(North/South Boundry, East/West Boundry)
#     #[nS, Ne, eS, eE] #make smaller boundries for things like houses and special areas, 
#     # can make it so if in that area need special stuff to open #Can always increase boundry bt 10
#     {"Meadows": [20, 30, -10, 0],  "Volcano" : [20, 30, 0, 10], "Cliffs" : [20, 30, 10, 20]},
#     {"Lava Plains" : [10, 20, -10, 0], "Ice Plains" : [10, 20, 0, 5], "Frosted Plains" : [10,20, 5, 10] ,"Water Plains" : [10, 20, 10, 20]},
#     {"Waterloo" : mapWaterloo.getCordinate(), "Greenland" : mapGreenland.getCordinate(), "Pine Forest" : [0, 10, 10, 20]}
# ] #Create new maps for each biome [0, 10, -10, 0][0, 10, 0, 10]
dropCopy = {


}
itemLoc = {
    #Empty list that gets deleted and stored depending on location on map(Stores less space)
    #However, doesnt save location of other objects if i delete. So numbers get replaced for each item
}
itemDrop = {#When an item is dropped it stores that item in this location

}
def r(start, end):
    return random.randint(start, end)
gridItems = { #Maybe change to have different items depending on level
    #Make it so each land can spawn certain items, but make it so each land has a different spawn 
    #percantange for each item thus lower biomes have hogher chance for lesser weapons and others biomes have \
    #higher percentage 
    #{Update as new item are introduced in game}
    #'Biome' : [[items],[number of items]]
    #however, can just make it so depending on level the spawn chance is different, can just add this to array of items
    #Can make it so each item gets spawned at random intervals
    #(TO DO) Can make this sytem in setMap class
    "Meadows" : [["Stick", "String", "Iron Ore", "Iron Armor", "Stone Axe", "Stone Sword"],[r(3, 7), r(3, 6), r(6, 10), r(1, 3), r(3, 5), r(2, 3)]],
    "Lava Plains" : [["Iron Axe", "Iron Ingot", "Crisp Apple", "Iron Ore", "Bomb", "Flint", "Stick"],[r(2, 5), r(5, 11), r(5, 8), r(5, 8),r(2, 5), r(4, 7), r(2, 5), ]],
    "Waterloo" : [["Rock", "Iron Axe", "Flint", "Cloth", "Stone Sword", "Apple", "Crisp Apple", "Stick"],[r(6, 9), r(3, 5), r(7, 9), r(4, 9), r(2, 7), r(5, 9), r(3, 7), r(5, 8)]],
    
    "Volcano" : [["Aragon's Blade", "Gun Powder", "Flint", "Iron Ingot", "Iron Ore", "Crisp Apple"],[r(1, 2), r(3, 8), r(4, 9), r(8, 16), r(10, 18), r(4, 9)]],
    "Ice Plains" : [["Iron Axe", "Rock", "String","Wood Sword", "Iron Ore","Frozen Cow"],[r(1,3),r(1, 6), r(5, 8), r(1, 4), r(4, 10), r(3, 9)]],
    "Frosted Plains" : [["Rock", "Frozen Cow"],[r(3,7), r(3, 7)]],
    "Greenland" : [["Stone", "Stone Axe", "Iron Armor", "Stick", "Iron Ore", "Apple"],[r(3, 7), r(1, 2), r(1, 2), r(7, 18), r(3, 7), r(5, 9)]],
    
    "Cliffs" : [["Cloth", "Apple", "Stone", "Iron Ore", "Wood Plank"],[r(4, 8), r(2, 12), r(5, 9), r(6, 12), r(3, 6)]],
    "Water Plains" : [["Flippers", "Apple", "Iron Ore", "Stick"],[r(3, 7), r(6, 10), r(7, 13), r(4, 9)]],
    "Pine Forest" : [["Apple", "Pine Bow", "Pine Arrow", "Pine Sap", "Stick"],[r(1, 7), r(1, 4), r(2, 3), r(4, 7), r(6, 8)]],
}
disMov = {#save lines of code by susbtringing first letter of each and then printing out. Saves lnes of code.
    "n" : ["You venture North! ", "You gingerly take a step North", "Yonder over North", "North it is"],
    "e" : ["You venture East! ", "You gingerly take a step East", "Yonder over East", "East it is"],
    "s" : ["You venture South! ", "You gingerly take a step South", "Yonder over South", "South it is"],
    "w" : ["You venture West! ", "You gingerly take a step West", "Yonder over West", "West it is"],
}