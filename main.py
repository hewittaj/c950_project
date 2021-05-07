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
total_distance = 0.0

# Load truck 1
while len(truck1) < 16:
    # Assign info from the next shortest algo
    distance_info = d.get_next_shortest(starting_point, package_hashmap, skip_list, 1)

    # If is an earlier delivery we want to get that first
    if '10:30' in distance_info[4]:
        truck1.insert(1, package_hashmap.get_val(distance_info[3]))
    else:
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

    # If is an earlier delivery we want to get that first
    if '9:00' in distance_info[4]:
        truck2.insert(1, package_hashmap.get_val(distance_info[3]))
    if '10:30' in distance_info[4]:
        truck2.insert(2, package_hashmap.get_val(distance_info[3]))
    else:
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

truck1.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
truck2.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
truck3.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub

# Get the total distance of each truck
total_distance = d.get_total_distance(truck1) + d.get_total_distance(truck2) + d.get_total_distance(truck3)
print(f"Total Distance: {total_distance:0.2f} miles.")

print(truck1)
print(len(truck1))
print(truck2)
print(len(truck2))
print(truck3)
