# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Most important packages go here
truck2 = []
truck3 = []  # Will be the reserve truck

greedy_route_truck1 = []  # Updated list of greedy route for each truck
greedy_route_truck2 = []
greedy_route_truck3 = []  # All end of day packages w/ no constraints

starting_point = 0  # Starting point is the hub i.e. index 0
total_distance = 0.0  # Sum of all the distances a truck traveled

# Manually load some packages
be_together = [13, 14, 15, 16, 19, 20]  # Packages that must be delivered together
only_truck_two = [3, 18, 35, 37]  # Packages that can only be on truck two
delayed = [6, 25, 31]  # Packages that are delayed and won't arrive until 9:05
no_special_needs = [2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26, 27]  # Packages that don't have special needs

# Manually sort packages
for i in range(1, 41):
    package_info = package_hashmap.get_val(i)

    # Load packages that have to be delivered together
    if int(package_info[0]) in be_together:
        truck1.append(package_info)

    if int(package_info[0]) in only_truck_two:
        truck2.append(package_info)

    if int(package_info[0]) in delayed:
        truck2.append(package_info)

    if int(package_info[0]) in no_special_needs:
        truck3.append(package_info)


greedy_route_truck1.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
greedy_route_truck2.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub
greedy_route_truck3.insert(0, ['0', '4001 South 700 East'])  # Insert 0 as they all start at the hub

while truck1:
    distance_info = d.get_greedy_route(truck1, greedy_route_truck1)
    greedy_route_truck1.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck1.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck
distance_info = []  # Clear out info

while truck2:
    distance_info = d.get_greedy_route(truck2, greedy_route_truck2)
    greedy_route_truck2.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck2.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck
distance_info = []  # Clear out info

while truck3:
    distance_info = d.get_greedy_route(truck3, greedy_route_truck3)
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