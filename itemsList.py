#Maybe make all items objects
#When making new items add to itemInfo and if damage weapon or armor add to items buffs and crafting


itemInfo = [
    #Will Add more tools as I figure out what to add 
    #Use info to give background to each item like a little history 
    #buffs can be applied later
    #Make it so later you can use items and check in inventory
    #Make something that blows up walls to cross if there is gunpowder
    #{"item" : ": description"}
    #utilities
    {"Stone" : ": Can be used as a stepping stone up small bumps", 
    "Gun Powder" : ": Used with Flint to blow up obstacles", 
    "Flint" : ": Used as a stricker with flamables",
    "Stick" : ": Used in many crafting recipes", 
    "String" : ": Used in crafting recipes that involve stretch", 
    "Cloth" : ": Used for lightweight armor and craftables", 
    "Iron Ore" : ": Used to craft Iron and Steal Ingots", 
    "Iron Ingot" : ": A Strong metal used in many Recipee",
    "Wood Plank" : ": Used for building and Crafting", 
    "Furnace" : ": Used to cook food and ore. Needs Fuel Possibly dpening on how i feel", 
    "Wood Wall" : ": Cannot be walked on, used as decoration or defense",
    "Wood Door" : ": Used for decroation, can be walked through by player", 
    "Wood Board" : ": Used for building materials and consutruction",
    "Crafting Table" : ": Used for crafting complex items",
    },
    #wearbles
    {"Cloth Tunic" : ": Provides minimal defense", 
    "Iron Armor" : ": Provides mid defense", 
    "Weathered Tunic" : ": Player Starts Journey with Cloths that have tested time",
    "Flippers" : ": These little webs boost your speed in water",
    },
    #damage items
    {
    "Rock" : ": Can be hurled at enemies for minimal damage", 
    
    "Wood Sword" : ": Provides minimal attack damage", 
    "Wood Pickaxe" : ": Breaks stone",
    "Wood Axe" : ": Breaks trees",
    
    "Iron Sword" : ": The shinest blade in the east creates fear in enemies" ,
    "Stone Pickaxe" : ": Can break ore deposits",
    "Stone Axe" : ": Provides improved attack damage", 
    
    "Iron Sword" : ": higher damage sword",
    "Iron Pickaxe" : ": can break iron blocks and higher quality ore deposits",
    "Iron Axe" : ": Attack Boost of 2 and Breaks Doors",
    
    "Aragon's Blade" : ": A fiery blade forged from the notorious half-born eating dragon, Aragon", 
    "Pine Bow" : ": Lightweight low attack bow", 
    "Pine Arrow" : ": lightwieght arrow made from flimsy wood",
    "Bomb" : ": Craftable weapon that can blow up doors and walls, as well as damage others", 
    
    "Instant Kill" : ": If you have this item you are cheating!",
    },
    #maybe bomb is utility 
    #Consumables
    {"Pine Sap" : ": Heals 5 health", 
    "Apple" : ": Heals 3 health", 
    "Raw Egg" :": Can be eaten, but not recomended. Try cooking with it (Just dont ask where it came from)", 
    "Omelet": ": A protein infused breakfast", 
    "Frozen Cow" : ": MOOOOooooo", 
    "Crisp Apple" : ": These crunchy delicacies give a boost to health", 
    "Steak" : ": I see you are trying to bulk up"}
]
itemBuffs = [
    #Add number for buffs [Damage/protection]
    #!!! Decide if it doesnt have another affect to keep null or 
    #Need to make methods to figure out what each one does
    #(TO DO) IF drop bomb and shoot, explode!

    #ADD TO AXES AND WEAPONS WHAT TYPE OF MATERIAL IT CAN BREAK
    #MAKE IT SO CERTAIN ITEMS ARENT PICKABLE AFTER BUILT (CAN JUST MAKE DROP AND BUILD DIFFERENT) ONLY CAN BE DESTROYED
    #"name of item" : [damage,power/buff/ability], [type of matariel], "pickable"]
    #utilities
    {
    "Stone" : ["0","Stepping Stone"], 
    "Gun Powder" : ["0", "Fire Starter"], 
    "Flint" : ["0", "Striker"], 
    "Furnace" : ["0", "Cooker"]
    }, 
    #wearbles (Number is how much damage can potentially be decreased per someones attack])
    {
    "Cloth Tunic" : ["3", "Wearable"], 
    "Iron Armor" : ["5", "Wearable"], 
    "Weathered Tunic" : ["2", "Wearable"], 
    "Flippers" : ["3","Wearable", "Swim"]
    },
    #damage items (Number is how much damage can be done) Array [damage, buff/power] Element damge leaves a lingering affect during fight
    #(TO DO) Make it so range weapons have certain range and speed of shot (Just decrease time.sleep in shoot function)
    #Items : ["Damage",["Materials it breaks"E.X "Wood", "Stone"]]
    #Can add heiarchy chart where if it can break stone it can break more
    {
    "Rock" : ["2", ["Projectile-5 (Squares)", "Speed-0.5 (Milliseconds)"]], 
    
    "Wood Sword" : ["4", ["Nothing"]], 
    "Wood Pickaxe" : ["2", ["Stone"]],
    "Wood Axe" : ["3", ["Wood"]],
    
    "Stone Sword" : ["7", ["Nothing"]], 
    "Stone Pickaxe" : ["4", ["Wood","Stone"]],
    "Stone Axe" : ["5", ["Wood"]], 
    
    "Iron Sword" : ["10", ["Nothing"]],
    "Iron Axe" : ["7", ["Wood","Stone"]],
    "Iron Pickaxe" : ["4", ["Wood","Stone","Iron"]],

    "Aragon's Blade" : ["9", "Fire Damage"], 
    
    "Pine Bow" : ["10", "Range-10", "Speed-0.3"], 
    "Pine Arrow" : ["2", "Projectile"],
    "Bomb": ["10", "Explosive"], 
    
    "Instant Kill" : ["30000", ["Death Touch"]], 
   
    },  

    #consumbales (Food, potions, posion)
    #(TO DO) Add a cookable feature 'cookable' and then what it turns into after cooking
    #Dont need to do turn into just to do that in crafting book for cooking
    {"Pine Sap" : ["5", "Consumable"], 
    "Apple" : ["3", "Consumable"], 
    "Raw Egg": ["1", "Consumable", "Poison"], 
    "Omelet" : ["8", "Consumable"],
    "Frozen Cow" : ["3", "Consumable", "Poison"],
    "Crisp Apple" : ["7", "Consumable"], 
    "Steak" : ["15", "Consumable"]
    }
]   
####ADD craftable items, but make sure not to put those items in fields, only craftable. 
# (Like combining stuff to make a bomb)
itemCraft = { #Works now just add whatever I want. However, make sure to then add it to item list and category
    #Make it so i do same thing as spawning in items where i write amount of items
    #Like: [["Flint", "Gun Powder"], [1, 1]] or [["Stick", "String", "Pine Sap"],[3,2,2]] can even make it so you get it this many times
    "Wood Plank" : [["Stick"],[2],[4]],
    "Stick" : [["Wood Plank"],[1],[2]],
    "Crafting Table": [["Wood Plank"],[2],[1]],
    
    "Furnace" : [["Stone"],[2],[1]],
    "Rock" : [["Stone"],[1],[2]],
    
    
    # "Iron Ingot": [["Iron Ore"],[2],[1]], #Comment out later for smelting
    
    "Wood Sword" : [["Stick", "Wood Plank"],[1, 2],[1]],
    "Wood Pickaxe" : [["Stick", "Wood Plank"], [2, 3],[1]],
    "Wood Axe" : [["Stick", "Wood Plank"],[2, 3],[1]],

    "Stone Sword" : [["Stick", "Stone"],[1, 2],[1]],
    "Stone Pickaxe" : [["Stick", "Stone"], [2, 3],[1]],
    "Stone Axe" : [["Stick", "Stone"],[2, 3],[1]],

    "Iron Sword" : [["Stick", "Iron Ingot"], [1, 2],[1]],
    "Iron Pickaxe" : [["Stick", "Iron Ingot"], [2, 3],[1]],
    "Iron Axe": [["Stick", "Iron Ingot"],[2, 3],[1]],

    "Wood Board" : [["Wood Plank"], [1],[2]],
    "Wood Wall" : [["Wood Plank"],[3],[4]],    
    "Wood Door" : [["Wood Wall", "Wood Plank", "Stick"],[1, 2, 2],[4]],

    "Bomb" : [["Flint", "Gun Powder"],[1, 1],[1]],
    "Pine Bow" : [["Stick", "String", "Pine Sap"],[3, 3, 2],[1]],
    "Pine Arrow" : [["Rock", "Stick", "Pine Sap"],[1, 1, 2],[4]],
    
    "Cloth Tunic" : [["Cloth"],[4],[1]],
    "Iron Armor": [["Iron Ingot"],[8],[1]],
    
    
    
    
    
    
}
#Add a cooking device so you can cook items like Omelet or cooked apple
itemCook = {
    #Make it so you place cooker and when person is on it they can cook items
    #however, when not on it they cannot. the cooking device is portable 
    #person just has to drop it
    #[[items],[count]]
    "Iron Ingot" : [["Iron Ore"],[2], [1]],
    "Omelet" : [["Raw Egg"],[2], [1]], #Turn into cooking for later and not craftable
    "Crisp Apple" :[["Apple"],[1], [1]],
    "Steak" : [["Frozen Cow"],[1], [1]],
    "Iron Ore" :[["Iron Axe"],[1], [4]] #Maybe change book for smelting
}