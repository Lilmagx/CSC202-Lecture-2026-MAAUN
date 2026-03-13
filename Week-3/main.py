from models import FuelDispenser, CarWash

# Create assets
fuel1 = FuelDispenser("Fuel Pump 1", 500, 1.5)
fuel2 = FuelDispenser("Fuel Pump 2", 300, 1.5)

wash1 = CarWash("Automatic Wash", 40, 10)

# Store assets in list
station_assets = [fuel1, fuel2, wash1]

total_revenue = 0

for asset in station_assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue

print("Total Station Revenue:", total_revenue)