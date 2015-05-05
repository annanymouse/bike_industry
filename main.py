"""
Refactoring bicycles.py
"""

from bicycles import Bicycle, BikeShops, Customers, Wheels, Frames

def divider(title):
    print("*"*30)
    print("{:^30}".format(title))
    print("*"*30)

divider("Wheels Available")
basic = Wheels("Basic", 5, 60)
print(basic)
premium = Wheels("Premium", 6, 150)
print(premium)
allterrain = Wheels("All Terrain", 7, 300)
print(allterrain)
divider("Frames Available")
light = Frames(4, 20)
print(light)
heavyduty = Frames(5, 50)
print(heavyduty)
divider("Initial Inventory") 
cruiser = Bicycle("Cruiser", basic, light)
beach_bum = Bicycle("Beach Bum", basic, heavyduty)
city_slicker = Bicycle("City Slicker", premium, light)
bruiser = Bicycle("Bruiser", premium, heavyduty)
xtreme = Bicycle("Xtreme", allterrain, light)
mad_max = Bicycle("Mad Max", allterrain, heavyduty)
royalbikes = BikeShops("Royal Bikes")
bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
for bike in bike_list:
    royalbikes.add_inventory(bike)
print(royalbikes)
curly = Customers("Curly", 200)
larry = Customers("Larry", 500)
moe = Customers("Moe", 1000)
divider("Bike Quote for Curly") 
royalbikes.give_quote(curly)
divider("Bike Quote for Larry") 
royalbikes.give_quote(larry)
divider("Bike Quote for Moe") 
royalbikes.give_quote(moe)
divider("Bike Receipt for Curly")    
curly.buy_bike(royalbikes, cruiser)
divider("Bike Receipt for Larry") 
larry.buy_bike(royalbikes, city_slicker)
divider("Bike Receipt for Moe") 
moe.buy_bike(royalbikes, mad_max)
divider("Inventory & Profit After Sales") 
print(royalbikes)
print(royalbikes.profit())