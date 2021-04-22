# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap() # Initialize our hashmap with the packages from the csv

truck1 = []
truck2 = []
truck3 = [] # Will be the reserve truck

# Manually load some of the packages

print(d.get_next_shortest(7))
while(len(truck1) < 16): # Load truck 1
    truck1.append("")