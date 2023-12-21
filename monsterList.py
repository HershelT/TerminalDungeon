monsters = { #Gives certain monsters for story level
    "Beginning": [["Goblin", "Cat Noir", "Chomper"],[5, 3, 2]],
    "A New Leaf" : [["Hoboglin", "Buck I","LeGoat"],[3, 2, 2]],
    "The Might of the Novice" : [["Brick Master", "EGGxcelent", "Like a Boss"],[2,2,1]],
}
monstersClear = {
    #Empty board to store each monsters position
    #need to make it so when new level it also gets cleared: Not difficult
    #need to make it so armor wearing reduces damage
}
#Maybe change system so monsters give experience that can boost leveling up
#Maybe add clases like mage where you can boost your magica or fighting skills
#Make a skill tree
storyBoardMon = {#monsters needed to kill and how many of each monster needed to kill to advance level as long as collected items
    "Beginning" : [["Goblin", "Cat Noir", "Chomper"],[3, 1, 1]],
    "A New Leaf" : [["Hoboglin", "Buck I","LeGoat"],[2, 1, 1]],
    "The Might of the Novice" : [["Brick Master", "EGGxcelent", "Like a Boss"],[2, 1, 1]],
}
monMDandHP = { #Gives [Max damage, health, ["Award"], max drop count, Should add new one for probability of drop] Maybe add buffs like posion damage and stuff Add Award
    #Make it so you have slash between tiems so they can drop more than one
    #(TO DO) Have to make another array that gives each drop its own max drop count - similar to what i did with scattering items
    #[Max DG, Health ['item' rewards],[item drop chace], If I want drop automatic no matter what like a boss add this int of 1 to make it automatic]
    "Goblin" : [10, 20, ["Rock", "Iron Ore", "Stick"], [4, 4, 2], 0], #make second to last number max amount each item can drop can make it a list
    "Cat Noir" : [15, 40, ["Stone Axe", "Stone", "Iron Ingot"], [3, 6, 3], 0], #or make it so each item has that specific probabilty to drop and rerolls for each item
    "Chomper" : [20, 50, ["Pine Arrow", "Iron Ingot", "Iron Axe"], [5, 8, 2], 0],
    "Hoboglin" : [19, 60, ["Iron Armor", "Iron Ingot"], [2, 4], 0],
    "Buck I" : [25, 65, ["Gun Powder", "Flipers", "Apple"], [5, 1, 3], 0],
    "LeGoat" : [30, 70, ["Flint", "Iron Ingot"], [6, 9], 0],
    "Brick Master" : [35, 45, ["Iron Armor", "Iron Ore", "Flint"], [2, 8, 5], 0],
    "EGGxcelent" : [40, 20, ["Pine Sap", "Raw Egg", "Iron Ore", "Gun Powder"], [3, 4, 4, 5], 0],
    "Like a Boss" : [45, 150, ["Aragon's Blade", "Bomb"], [1, 5], 1],
    #(TO DO) Change it so monsters arent as hard to kill, or if they are make drops better
}
monsterAward = { #Gives awards based on destorying bosses, however 
                    #Fucntion that gives award gives a random amount of it

}
#CREATE A SYSTEM TO PLACE CERTAIN MONSTERS IN A CERTAIN AREA AT ALL TIMES, LIKE BOSS ROOMS ["MONSTER"],[LOCATION]
#so when it loADS IT ALWAYS PLACES MONSTER IN THAT SPOT