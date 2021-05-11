# Alex Hewitt student ID 001346462
from hashmap import HashMap
import import_packages_csv as package_csv
import distances as d
import time_calculations as t

package_hashmap = package_csv.get_hashmap()  # Initialize our hashmap with the packages from the csv

truck1 = []  # Most important packages go here
truck2 = []
truck3 = []  # Will be the reserve truck

greedy_route_truck1 = []  # Updated list of greedy route for each truck
greedy_route_truck2 = []
greedy_route_truck3 = []  # All end of day packages w/ no constraints

truck1_distance_info = []  # Distance info for each truck
truck2_distance_info = []
truck3_distance_info = []

starting_point = 0  # Starting point is the hub i.e. index 0
total_distance = 0.0  # Sum of all the distances a truck traveled

# Manually load some packages
be_together = [13, 14, 15, 16, 19, 20, 1, 28, 29, 30, 34, 39]  # Packages that must be delivered together on truck one
only_truck_two = [3, 18, 35, 37, 38, 27, 31, 33, 36, 40]  # Packages that can only be on truck two
delayed = [6, 25, 28, 32]  # Packages that are delayed and won't arrive until 9:05 go to truck two
no_special_needs = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26]  # Packages that don't have special needs

# Manually sort packages
for i in range(1, 41):
    # Get package info
    package_info = package_hashmap.get_val(i)

    # Load packages that have to be delivered together on truck 1
    if int(package_info[0]) in be_together:
        truck1.append(package_info)
        truck1[-1][10] = '8:00'

    # Load packages that can only be on truck two
    if int(package_info[0]) in only_truck_two:
        truck2.append(package_info)
        truck2[-1][10] = '9:05'

    # Load packages that are delayed to truck two
    if int(package_info[0]) in delayed:
        truck2.append(package_info)
        truck2[-1][10] = '9:05'

    # Load packages with no special needs to truck 3. Will be full after this
    if int(package_info[0]) in no_special_needs:
        # Update package w/ wrong address since it is on our reserve truck time will have passed
        # for it to be corrected
        if package_info[0] == '9':
            package_info[1] = '410 S State St'
            package_info[2] = 'Salt Lake City'
            package_info[3] = 'UT'
            package_info[4] = '84111'
        truck3.append(package_info)
        truck3[-1][10] = '8:00'


# Insert 0 as they all start at the hub
greedy_route_truck1.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00'])
greedy_route_truck2.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '9:05'])
greedy_route_truck3.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00'])

while truck1:
    distance_info = d.get_greedy_route(truck1, greedy_route_truck1)  # Get distance info for the next truck
    truck1_distance_info.append(distance_info)  # Append to our list for our later time calculations
    greedy_route_truck1.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck1.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

    # If the last package has gone out, then we need to return to the hub
    if len(truck1) == 0:
        truck1.append(['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00'])  # Set truck to return to hub
        distance_info = d.get_greedy_route(truck1, greedy_route_truck1)  # Get distance info for the next truck
        truck1_distance_info.append(distance_info)  # Append to our list for our later time calculations
        greedy_route_truck1.append(['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00'])  # Add package to greedy_route
        break  # Done with this loop
distance_info = []  # Clear out info

while truck2:
    distance_info = d.get_greedy_route(truck2, greedy_route_truck2)  # Get distance info for the next truck
    truck2_distance_info.append(distance_info)  # Append to our list for our later time calculations
    greedy_route_truck2.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck2.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck
distance_info = []  # Clear out info

while truck3:
    distance_info = d.get_greedy_route(truck3, greedy_route_truck3)  # Get distance info for the next truck
    truck3_distance_info.append(distance_info)  # Append to our list for our later time calculations
    greedy_route_truck3.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck3.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

# Get the total distance of each truck
total_distance = d.get_total_distance(greedy_route_truck1) + \
                 d.get_total_distance(greedy_route_truck2) + \
                 d.get_total_distance(greedy_route_truck3)
print(f"Total Distance: {total_distance:0.2f} miles.")

t.calculate_time(truck1_distance_info, greedy_route_truck1)  # TO DO DELETE

print(greedy_route_truck1)
print(greedy_route_truck2)
print(greedy_route_truck3)