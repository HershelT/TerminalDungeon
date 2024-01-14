blockedItems = ["\033[1;32mΨ\033[0m","🪵","\033[47m \033[0m","\033[34mΩ\033[0m","\033[0;34mΩ\033[0m","\033[38;2;101;6733m∏\033[0m", '\033[31m▓\033[39m', "\033[32m※\033[0m","\033[38;2;218;165;32mⅡ\033[0m","\033[37m¤\033[0m", "🪨", "|", "🪦","💎", "※", "Ω","\033[90mΩ\033[0m", "₡", "Ⅲ", "Ⅷ", "Ⅱ"]


blockStrength = ["All","Unbreakable","Diamond","Quartz","Iron", "Stone", "Wood", "Nothing"]
#Item : [Item needed to destroy, Damage to item]
def heirarchyCheck(block, itemBreak):

    block = itemDrops[block][3]
    blockBreak = blockStrength.index(block)
    # print(itemBreak, block) Debug
    if itemBreak == block:
        return [True, block] 
    for x in range(0, blockBreak):
        if itemBreak == blockStrength[x]:
            return [True, blockStrength[x]]
    return [False, block]



# key_blocks_list = []
#Class to make objects in games with special charterstics like display 
#and message that happens when i run into object or key level required to open
class KeyBlocks():
    def __init__(self, look, name, keyOrBombLevel, message, color = ""):
        self.look = look
        self.name = name
        self.keyOrBombLevel = keyOrBombLevel
        self.message = message
        self.isBlocking = True
        self.color = color
        # key_blocks_list.append(self)
    def setIsBlocking(self, isBlocking: bool):
        self.isBlocking = isBlocking
    def getColor(self):
        return self.color
    def getLook(self):
        return self.look
    def getName(self):
        return self.name
    def getIsBlocking(self):
        return self.isBlocking
    def getKeyLevel(self):
        return self.keyOrBombLevel
    def getMessage(self):
        return self.message
class Blocks():
    def __init__(self, look):
        self.look = look
        self.isBlocking = True
    def setIsBlocking(self, isBlocking: bool):
        self.isBlocking = isBlocking
    def getLook(self):
        return self.look
    def getIsBlocking(self):
        return self.isBlocking
#
#Make a block that can be moved around the board

#"Item" : [["Items"][int(item amount),[random drop]],"Name", Type of material needed to destroy"]
itemDrops = {
    #Tree
    "\033[1;32mΨ\033[0m" : [["Wood Plank", "Stick", "Apple"],[1, 2, [-3,4]],"Tree","Nothing"], #Tree
    
    #Stone Boulder
    "\033[37m¤\033[0m" : [["Stone","Flint"],[2,[-3,3]], "Boulder","Wood"], 
    #Wood Door
    "∏" : [["Wood Door"],[1], "Wood Door", "Nothing"], 
    #Iron Ore Deposit
    "\033[90mΩ\033[0m" : [["Iron Ore"],[2], "Iron Ore Deposit", "Stone"], 
    #Diamond Ore Deposit
    "\033[34mΩ\033[0m" : [["Diamond"],[1], "Diamond Ore Deposit", "Iron"],
    #Crafting Table
    "\033[38;2;101;6733m∏\033[0m":[["Crafting Table"],[1],"Crafting Table", "Nothing"], 
    #Stone
    "\033[47m \033[0m" : [[],[], "Unbreakable Wall", "Unbreakable"], #Stone
    #Wood Wall (Building Block)
    "\033[38;2;218;165;32mⅡ\033[0m" : [["Wood Wall"],[1],"Wood Wall", "Nothing"],

    # "🪨" : [["Stone"],[2], "Boulder","Wood"], #
    # "🪦" : [["Stone", "Flint"],[1,1], "Grave Yard", "Stone"], Graveyard Emoji
    # "🪵" : [["Crafting Table"],[1],"Crafting Table", "Nothing"], 
    
}
def getItemList(item : str):
    itemsList = itemDrops[item]
    return itemsList




