# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Will pop a package from the hashmap when it has been decided it will be delivered next
truck2 = []
truck3 = []  # Will be the reserve truck

# Manually load some of the packages

starting_point = 0  # Starting point is the hub i.e. index 0
while(len(truck1) < 16): # Load truck 1
    distance_info = d.get_next_shortest(starting_point, package_hashmap)  # Assign info from the next shortest algo
    truck1.append(package_hashmap.get_val(distance_info[2]))  # Append information to the truck to be loaded onto
    print(package_hashmap.get_val(distance_info[2]))
    # Delete the value from the hashmap
    package_hashmap.delete(distance_info[2])  # Delete package from hashmap
    starting_point = distance_info[2]  # Update the next starting point
print(truck1)
