"""
Refactoring bicycles.py
"""

from bicycles import Bicycles, Customers, BikeShop


cruiser = Bicycle("Cruiser", 17, 100)
beach_bum = Bicycle("Beach Bum", 18, 150)
city_slicker = Bicycle("City Slicker", 17, 380)
bruiser = Bicycle("Bruiser", 19, 400)
xtreme = Bicycle("Xtreme", 20, 750)
mad_max = Bicycle("Mad Max", 18, 780)
royalbikes = BikeShops("Royal Bikes")
bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
for bike in bike_list:
    royalbikes.add_inventory(bike)
print(royalbikes)
curly = Customers("Curly", 200)
larry = Customers("Larry", 500)
moe = Customers("Moe", 1000)
royalbikes.give_quote(curly)
curly.buy_bike(royalbikes, cruiser)
larry.buy_bike(royalbikes, city_slicker)
moe.buy_bike(royalbikes, mad_max)
print(royalbikes)
print(royalbikes.profit())