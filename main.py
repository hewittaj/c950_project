# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Will pop a package from the hashmap when it has been decided it will be delivered next
truck2 = []
truck3 = [] # Will be the reserve truck

# Manually load some of the packages

print(d.get_next_shortest(12))
starting_point = 0  # Starting point is the hub i.e. index 0
while(len(truck1) < 16): # Load truck 1
    truck1.append(d.get_next_shortest(starting_point))
    starting_point = 1  # TO DO , calculate next starting point
print(truck1)
