"""
Refactoring bicycles.py
"""
import random

from bicycles import Bicycle, BikeShops, Customers, Wheels, Frames, BikeManufacturers

def divider(title):
    print("*"*30)
    print("{}".format(title))
    print("*"*30)

if __name__=="__main__":
    # MANUFACTURERS
    divider("Bike Manufacturers")
    champion = BikeManufacturers("Champion", 0.05)
    energy = BikeManufacturers("Energy", 0.03)
    champion.print_details()
    energy.print_details()
    
    # WHEELS
    divider("Wheels Available")
    basic = Wheels(model="Basic", weight=5, cost=60)
    premium = Wheels(model="Premium", weight=6, cost=150)
    allterrain = Wheels(model="All Terrain", weight=7, cost=300)
    wheels = [basic, premium, allterrain]
    print('\n'.join([str(wheel) for wheel in wheels]))

    # FRAMES
    divider("Frames Available")
    light = Frames(weight=4, cost=20)
    heavyduty = Frames(weight=5, cost=50)
    frames = [light, heavyduty]
    print('\n'.join([str(frame) for frame in frames]))

    # BIKES & BIKESHOP
    divider("Initial Inventory") 
    cruiser = Bicycle(model="Cruiser", wheel=basic, frame=light, manufacturer=champion)
    beach_bum = Bicycle(model="Beach Bum", wheel=basic, frame=heavyduty, manufacturer=energy)
    city_slicker = Bicycle(model="City Slicker", wheel=premium, frame=light, manufacturer=champion)
    bruiser = Bicycle(model="Bruiser", wheel=premium, frame=heavyduty, manufacturer=energy)
    xtreme = Bicycle(model="Xtreme", wheel=allterrain, frame=light, manufacturer=champion)
    mad_max = Bicycle(model="Mad Max", wheel=allterrain, frame=heavyduty, manufacturer=energy)
    bike_list = [cruiser, beach_bum, city_slicker, bruiser, xtreme, mad_max]
    royalbikes = BikeShops("Royal Bikes", 200000)
    royalbikes.budget_details()
    for bike in bike_list:
        royalbikes.add_inventory(bike, random.randint(5,25))
    royalbikes.print_inventory()
    royalbikes.budget_details()

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
    royalbikes.print_inventory()
    royalbikes.profit()