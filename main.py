# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Will pop a package from the hashmap when it has been decided it will be delivered next
truck2 = []
truck3 = []  # Will be the reserve truck

greedy_route_truck1 = []  # Updated list of greedy route
greedy_route_truck2 = []
greedy_route_truck3 = []

starting_point = 0  # Starting point is the hub i.e. index 0
skip_list = []
total_distance = 0.0
# Manually load some packages
be_together = [13, 14, 15, 16, 19, 20]
only_truck_two = [3, 18, 35, 37]

# Load packages that have to be delivered together
for num in be_together:
    skip_list.append(num)
    truck3.append(package_hashmap.get_val(num))

# Load packages that can only be on truck two
for num in only_truck_two:
    skip_list.append(num)
    truck2.append(package_hashmap.get_val(num))

greedy_route_truck1.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
greedy_route_truck2.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
greedy_route_truck3.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub

truck1.insert(1, package_hashmap.get_val(25))

while truck1:
    distance_info = d.get_greedy_route(truck1, greedy_route_truck1)
    greedy_route_truck1.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck1.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

while truck2:
    distance_info = d.get_greedy_route(truck2, greedy_route_truck2)
    greedy_route_truck2.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck2.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

while truck3:
    distance_info = d.get_greedy_route(truck3, greedy_route_truck1)
    greedy_route_truck3.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck3.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

# Get the total distance of each truck
total_distance = d.get_total_distance(greedy_route_truck1) + \
                 d.get_total_distance(greedy_route_truck2) + \
                 d.get_total_distance(greedy_route_truck3)
print(f"Total Distance: {total_distance:0.2f} miles.")

print(greedy_route_truck1)
print(greedy_route_truck2)
print(greedy_route_truck3)