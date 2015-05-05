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
        self.inventory = {}
        self.margin = 0.20
        self.total_profit = 0
        
    def give_quote(self, customer):
        """Creates quote on bicycles in stock within customer's budget."""
        print("Here is your quote:")
        print(customer)
        #bike_quote = []
        for bike in self.inventory:
            retail = self.retail_price(bike)
            if retail < customer.money:
                #bike_quote.append(bike)
                print("Model: {}, Weight: {}, Retail Price: {}".format(bike.model, bike.weight, retail))
        #return bike_quote
        #return "{}".format('\n'.join([str(bike) for bike in bike_quote]))
        
    def add_inventory(self, bike, quantity=10):
        self.inventory[bike] = quantity
        
    def retail_price(self, bike):
        return bike.cost+(bike.cost*self.margin)
        
    def __str__(self):
        #return "{}".format('\n'.join([str(bike) for bike in self.inventory]))
#        return "{}".format("\n".join([str(bike), qty for bike, qty in self.inventory.items()]))
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
        
           
# if __name__ == '__main__':
#     cruiser = Bicycle("Cruiser", 17, 100)
#     beach_bum = Bicycle("Beach Bum", 18, 150)
#     city_slicker = Bicycle("City Slicker", 17, 380)
#     bruiser = Bicycle("Bruiser", 19, 400)
#     xtreme = Bicycle("Xtreme", 20, 750)
#     mad_max = Bicycle("Mad Max", 18, 780)
#     royalbikes = BikeShops("Royal Bikes")
#     bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
#     for bike in bike_list:
#         royalbikes.add_inventory(bike)
#     print(royalbikes)
#     curly = Customers("Curly", 200)
#     larry = Customers("Larry", 500)
#     moe = Customers("Moe", 1000)
#     royalbikes.give_quote(curly)
#     curly.buy_bike(royalbikes, cruiser)
#     larry.buy_bike(royalbikes, city_slicker)
#     moe.buy_bike(royalbikes, mad_max)
#     print(royalbikes)
#     print(royalbikes.profit())