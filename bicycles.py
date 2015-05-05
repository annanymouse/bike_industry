"""
Modeling the Bicycle Industry
"""
import random

class Wheels(object):
    """
    Wheels have a model name, weight, and a cost to produce.
    There should be a total of three different wheel types
    """
    def __init__(self, model=None, weight=None, cost=None):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return "Model: {}, Weight: {}, Cost: {}".format(self.model, self.weight, self.cost)
    
class Frames(object):
    """
    Frames can be made of aluminum, carbon, or steel, have a weight and a cost to produce
    """
    def __init__(self, weight=None, cost=None):
        materials = ['aluminum', 'carbon', 'steel']
        self.material = random.choice(materials)
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return "Material: {}, Weight: {}, Cost: {}".format(self.material, self.weight, self.cost)
        
class Bicycle(object):
    """Bicycle have a model name, weight, and cost to produce"""
    def __init__(self, model=None, wheel=None, frame=None):
        self.model = model
        self.wheel = wheel
        self.frame = frame
        self.weight = frame.weight + (wheel.weight*2)
        self.cost = frame.cost + (wheel.cost*2)
        
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
        self.inventory = {}
        self.margin = 0.20
        self.total_profit = 0
        
    def give_quote(self, customer):
        """Creates quote on bicycles in stock within customer's budget."""
        print("Here is your quote:")
        print(customer)
        for bike in self.inventory:
            retail = self.retail_price(bike)
            if retail < customer.money:
                print("Model: {}, Weight: {}, Retail Price: {}".format(bike.model, bike.weight, retail))
        
    def add_inventory(self, bike, quantity=10):
        self.inventory[bike] = quantity
        
    def retail_price(self, bike):
        return bike.cost+(bike.cost*self.margin)
        
    def __str__(self):
        """Print the inventory nicely."""
        return "\n".join(["{}, Quantity: {}".format(str(bike), self.inventory[bike]) for bike in self.inventory])
        
    def profit(self):
        """Create a dictionary for this with bicycles and profits."""
        return "Our total profit is now {}.".format(str(self.total_profit))
    
class Customers(object):
    def __init__(self, name, money):
        """Customers have a name, a fund of money to buy a bike, and can buy and own a new bicycle."""
        self.name = name
        self.money = money
        self.bikes_owned = []
        
    def __str__(self):
        return "Customer Name: {}, Budget: {}".format(self.name, self.money)       
        
    def buy_bike(self, bikeshop, bike):
        """Create a method that add a bike to bikes_owned and subtracts money."""
        """Method should also add profit and decrease inventory to the bike shop."""
        retail = bikeshop.retail_price(bike)
        if retail < self.money:
            self.money = self.money - retail
            self.bikes_owned.append(bike)
            bikeshop.inventory[bike] -= 1
            bikeshop.total_profit += bike.cost*bikeshop.margin
            print("Thanks for purchasing the {} bicycle, {}!\nThe bike cost you {} and you have {} left in your bicycle fund."
                  .format(bike.model, self.name, retail, self.money))
        else:
            print("Sorry! You can't afford this bike.")