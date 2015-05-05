"""
Modeling the Bicycle Industry
"""

class Bicycle(object):
    """Bicycle have a model name, weight, and cost to produce"""
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return "Model: {}, Weight: {}, Cost: {}".format(self.model, self.weight, self.cost)
      
class BikeShops(object):
    """
    Bike Shops have a name, an inventory of different bicycles,
    sell bicycles with a margin over their cost, and
    can see how much profit they have made from selling bikes.
    """
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.margin = 0.20
        self.bikes_sold = {}
        
    def give_quote(self, customer):
        """Creates quote on bicycles in stock within customer's budget."""
        print("Here is your quote:")
        print(customer)
        #bike_quote = []
        for bike in self.inventory:
            retail_price = bike.cost+(bike.cost*self.margin)
            if retail_price < customer.money:
                #bike_quote.append(bike)
                print("Model: {}, Weight: {}, Retail Price: {}".format(bike.model, bike.weight, retail_price))
        #return bike_quote
        #return "{}".format('\n'.join([str(bike) for bike in bike_quote]))
        
    def add_inventory(self, bike):
        self.inventory.append(bike)
        
    def __str__(self):
        return "{}".format('\n'.join([str(bike) for bike in self.inventory]))
        
    def profit(self):
        """Create a dictionary for this with bicycles and profits."""
        pass
    
class Customers(object):
    def __init__(self, name, money):
        """Customers have a name, a fund of money to buy a bike, and can buy and own a new bicycle."""
        self.name = name
        self.money = money
        self.bikes_owned = []
        
    def __str__(self):
        return "Customer Name: {}, Budget: {}".format(self.name, self.money)       
        
    def buy_bike(self):
        """Create a function that add a bike to bikes_owned and subtracts money."""
        pass
        
if __name__ == '__main__':
    cruiser = Bicycle("Cruiser", 17, 100)
    beach_bum = Bicycle("Beach Bum", 18, 150)
    city_slicker = Bicycle("City Slicker", 17, 425)
    bruiser = Bicycle("Bruiser", 19, 475)
    xtreme = Bicycle("Xtreme", 20, 800)
    mad_max = Bicycle("Mad Max", 18, 850)
    royalbikes = BikeShops("Royal Bikes")
    bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
    for bike in bike_list:
        royalbikes.add_inventory(bike)
    print(royalbikes)
    curly = Customers("Curly", 200)
    larry = Customers("Larry", 500)
    moe = Customers("Moe", 1000)
    print(royalbikes.give_quote(curly))
    
    
    