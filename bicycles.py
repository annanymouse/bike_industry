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
        
    def add_inventory(self, bike):
        self.inventory.append(bike)
        
    def __str__(self):
        return "{}".format('\n'.join([str(bike) for bike in self.inventory]))
        
    def profit(self):
        """Create a dictionary for this with bicycles and profits."""
        pass

    
class Customers(object):
    def __init__(self):
        """Customers have a name, a fund of money to buy a bike, and can buy and own a new bicycle."""
        self.name = name
        self.money = money
        self.bikes_owned = []
        
    def buy_bike():
        """Create a function that add a bike to bikes_owned and subtracts money."""
        pass
        
if __name__ == '__main__':
    cruiser = Bicycle("Cruiser", 17, 100)
    beach_bum = Bicycle("Beach Bum", 18, 120)
    city_slicker = Bicycle("City Slicker", 17, 250)
    bruiser = Bicycle("Bruiser", 19, 275)
    xtreme = Bicycle("Xtreme", 20, 300)
    mad_max = Bicycle("Mad Max", 18, 330)
    royalbikes = BikeShops("Royal Bikes")
    royalbikes.add_inventory(cruiser)
    royalbikes.add_inventory(beach_bum)
    royalbikes.add_inventory(city_slicker)
    royalbikes.add_inventory(bruiser)
    royalbikes.add_inventory(xtreme)
    royalbikes.add_inventory(mad_max)
    print(royalbikes)
    
    