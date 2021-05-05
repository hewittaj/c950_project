# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Will pop a package from the hashmap when it has been decided it will be delivered next
truck2 = []
truck3 = []  # Will be the reserve truck

starting_point = 0  # Starting point is the hub i.e. index 0
skip_list = []

# Load truck 1
while len(truck1) < 16:
    # Assign info from the next shortest algo
    distance_info = d.get_next_shortest(starting_point, package_hashmap, skip_list, 1)

    # Append information to the truck to be loaded onto
    truck1.append(package_hashmap.get_val(distance_info[3]))

    # Add our package number to the skip list
    skip_list.append(distance_info[3])

    # Delete the value from the hashmap
    package_hashmap.delete(distance_info[3])
    # Update the next starting point
    starting_point = distance_info[2]

# Load truck 2
starting_point = 0  # Reset the starting point to the hub
while len(truck2) < 16:
    # Assign info from the next shortest algo
    distance_info = d.get_next_shortest(starting_point, package_hashmap, skip_list, 2)

    # Append information to the truck to be loaded onto
    truck2.append(package_hashmap.get_val(distance_info[3]))

    # Add our package number to the skip list
    skip_list.append(distance_info[3])

    # Delete the value from the hashmap
    package_hashmap.delete(distance_info[3])

    # Update the next starting point
    starting_point = distance_info[2]

# Load truck 3
starting_point = 0  # Reset the starting point to the hub
while len(truck3) < 16:
    # Assign info from the next shortest algo
    distance_info = d.get_next_shortest(starting_point, package_hashmap, skip_list, 3)

    # Append information to the truck to be loaded onto
    truck3.append(package_hashmap.get_val(distance_info[3]))

    # Add our package number to the skip list
    skip_list.append(distance_info[3])

    # Delete the value from the hashmap
    package_hashmap.delete(distance_info[3])

    # Update the next starting point
    starting_point = distance_info[2]



print(truck1)
print(len(truck1))
print(truck2)
print(len(truck2))
print(truck3)
for num in range(1,41):
    print(package_hashmap.get_val(num))