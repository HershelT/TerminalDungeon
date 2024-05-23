class StoreKeeper:
    def __init__(self, name = 'storekeeper'):
        self._store = {}
        self.add('name', name)
    def add(self, key, value):
        self._store[key] = value
    def get(self, key):
        return self._store.get(key)
    def remove(self, key):
        del self._store[key]
    def clear(self):
        self._store.clear()
    #Sets name and prices of each item
    def getLook(self):
        return "B"
    def setName(self, name):
        self.add('name', name)
    def addItemPrice(self, item, price):
        self.add(item, price)   
    #Gets name and prices of each item
    def getItemPrice(self, item):
        return self.get(item)
    def getName(self):
        return self.get('name')
    #Gets all items minus name
    def getItems(self):
        items = list(self._store.keys())
        items.remove('name')
        return items
    def buy(self, item):
        if item in self.getItems():
            print('You bought ', item.capitalize(), ' for $ ', self.getItemPrice(item), sep = '')
        else:
            print('Sorry, we do not have', item)
    #Gets all prices minus name
    def getPrices(self):
        prices = list(self._store.values())
        prices.remove(self.get('name'))
        return prices
    #Gets all items and prices minus name
    def getItemsAndPrices(self):
        items = self.getItems()
        prices = self.getPrices()
        itemsAndPrices = {}
        for i in range(len(items)):
            itemsAndPrices[items[i]] = prices[i]
        return itemsAndPrices
    #prints out prices nicely
    def printPrices(self):
        itemsAndPrices = self.getItemsAndPrices()
        for item in itemsAndPrices:
            items = item.capitalize()
            print(items, ': $', itemsAndPrices[item], sep = '')
    def printSeller(self):
        print('Seller:', self.getName())

bob = StoreKeeper()
bob.setName('Bob')
bob.addItemPrice('apple', 1.00)
bob.addItemPrice('banana', 0.50)
bob.addItemPrice('orange', 1.50)
bob.buy('apple')
# print(bob)
# print(bob.getItems())
# print(bob.getPrices())
# print(bob.getItemsAndPrices())
bob.printSeller()
bob.printPrices()