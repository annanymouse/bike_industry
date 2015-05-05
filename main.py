"""
Refactoring bicycles.py
"""

from bicycles import Bicycle, BikeShops, Customers, Wheels, Frames

def divider(title):
    print("*"*30)
    print("{}".format(title))
    print("*"*30)

# WHEELS
divider("Wheels Available")
basic = Wheels("Basic", 5, 60)
premium = Wheels("Premium", 6, 150)
allterrain = Wheels("All Terrain", 7, 300)
wheels = [basic, premium, allterrain]
print('\n'.join([str(wheel) for wheel in wheels]))

# FRAMES
divider("Frames Available")
light = Frames(4, 20)
heavyduty = Frames(5, 50)
frames = [light, heavyduty]
print('\n'.join([str(frame) for frame in frames]))

# BIKES & BIKESHOP
divider("Initial Inventory") 
cruiser = Bicycle("Cruiser", basic, light)
beach_bum = Bicycle("Beach Bum", basic, heavyduty)
city_slicker = Bicycle("City Slicker", premium, light)
bruiser = Bicycle("Bruiser", premium, heavyduty)
xtreme = Bicycle("Xtreme", allterrain, light)
mad_max = Bicycle("Mad Max", allterrain, heavyduty)
bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
royalbikes = BikeShops("Royal Bikes")
for bike in bike_list:
    royalbikes.add_inventory(bike)
print(royalbikes)


# CLIENTS
curly = Customers("Curly", 200)
larry = Customers("Larry", 500)
moe = Customers("Moe", 1000)
clients = [curly, larry, moe]

# QUOTES FOR CLIENTS
for client in clients:
    print("*"*30 + "\nBike Quote for {}\n".format(client.name) + "*"*30)
    royalbikes.give_quote(curly)

# CLIENT PURCHASES
divider("Bike Receipt for Curly")    
curly.buy_bike(royalbikes, cruiser)
divider("Bike Receipt for Larry") 
larry.buy_bike(royalbikes, city_slicker)
divider("Bike Receipt for Moe") 
moe.buy_bike(royalbikes, mad_max)

# BIKESHOP INVENTORY & PROFIT AFTER SALES
divider("Inventory & Profit After Sales") 
print(royalbikes)
print(royalbikes.profit())