"""
Modeling the Bicycle Industry
"""
import random

class BikeManufacturers(object):
    """
    Bike manufacturers have a name, produce 3 models of bikes each, 
    and have a percentage over cost they sell bikes at to shops.
    """
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        
    def __str__(self):
        return self.name
    
    def print_details(self):
        """Prints out details nicely."""
        print "Bike Manufacturer: {}, Margin: {}".format(self.name, self.margin)

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
    def __init__(self, model=None, wheel=None, frame=None, manufacturer=None):
        bike_cost = frame.cost + (wheel.cost*2)
        self.model = model
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer
        self.weight = frame.weight + (wheel.weight*2)
        self.cost = bike_cost + (bike_cost * manufacturer.margin)
        
    def __str__(self):
        return "Model: {}, Weight: {}, Cost: {}, Manufacturer: {}".format(self.model, self.weight, self.cost, self.manufacturer)
      
class BikeShops(object):
    """
    Bike Shops have a name, an inventory of different bicycles,
    sell bicycles with a margin over their cost, and
    can see how much profit they have made from selling bikes.
    """
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
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
                print("Model: {}, Manufacturer: {}, Weight: {}, Retail Price: {}".format(bike.model, bike. manufacturer, bike.weight, retail))
        
    def add_inventory(self, bike, quantity=10):
        """Adds inventory to the bike shop."""
        self.inventory[bike] = quantity
        self.budget -= bike.cost * quantity
        
    def retail_price(self, bike):
        """Calculates the retail price by adding the bike shop margin."""
        return bike.cost+(bike.cost*self.margin)
        
    def __str__(self):
        """Basic String Output"""
        return self.name
    
    def print_inventory(self):
        """Print the inventory nicely."""
        print "{}\n".format(self.name).upper() + "\n".join(["{}, Quantity: {}".format(str(bike), self.inventory[bike]) for bike in self.inventory])
        
    def profit(self):
        """Create a dictionary for this with bicycles and profits."""
        print "Our total profit is now {}.".format(str(self.total_profit))
    
    def budget_details(self):
        """Prints out budget report nicely."""
        print "Our budget to buy bikes wholesale is now {}.".format(str(self.budget))
    
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
            print("Thanks for purchasing the {} bicycle by {}, {}!\nThe bike cost you {} and you have {} left in your bicycle fund."
                  .format(bike.model, bike.manufacturer, self.name, retail, self.money))
        else:
            print("Sorry! You can't afford this bike.")