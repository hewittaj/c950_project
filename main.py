# Alex Hewitt student ID 001346462
import datetime
import itertools

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
be_together = [13, 14, 15, 16, 19, 20, 1, 29, 30, 34, 39]  # Packages that must be delivered together on truck one
only_truck_two = [3, 18, 35, 37, 38, 27, 31, 33, 36, 40]  # Packages that can only be on truck two
delayed = [6, 25, 28, 32]  # Packages that are delayed and won't arrive until 9:05 go to truck two
no_special_needs = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26]  # Packages that don't have special needs

# Manually sort packages
for i in range(1, 41):
    # Get package info
    package_info = package_hashmap.get_val(i)

    # Load packages that have to be delivered together on truck 1
    if int(package_info[0]) in be_together:
        truck1.append(package_info)
        truck1[-1][10] = '8:00:00'

    # Load packages that can only be on truck two
    if int(package_info[0]) in only_truck_two:
        truck2.append(package_info)
        truck2[-1][10] = '9:05:00'

    # Load packages that are delayed to truck two
    if int(package_info[0]) in delayed:
        truck2.append(package_info)
        truck2[-1][10] = '9:05:00'

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
        truck3[-1][10] = '8:00:00'


# Insert 0 as they all start at the hub
greedy_route_truck1.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00:00'])
greedy_route_truck2.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '9:05:00'])
greedy_route_truck3.insert(0, ['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00:00'])

while truck1:
    distance_info = d.get_greedy_route(truck1, greedy_route_truck1)  # Get distance info for the next truck
    truck1_distance_info.append(distance_info)  # Append to our list for our later time calculations
    greedy_route_truck1.append(package_hashmap.get_val(distance_info[2]))  # Add package to greedy_route
    truck1.remove(package_hashmap.get_val(distance_info[2]))  # Remove package from truck

    # If the last package has gone out, then we need to return to the hub
    if len(truck1) == 0:
        # Set truck to return to hub
        truck1.append(['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00:00'])
        distance_info = d.get_greedy_route(truck1, greedy_route_truck1)  # Get distance info for the next truck
        truck1_distance_info.append(distance_info)  # Append to our list for our later time calculations

        # Add package to greedy_route
        greedy_route_truck1.append(['0', '4001 South 700 East', '', '', '', '', '', '', '', '', '8:00:00'])
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

# Calculate delivery times for truck one
t.calculate_time(truck1_distance_info, greedy_route_truck1)

# Set new start time for truck 3 to be when truck 1 gets back
truck1_finish_time = greedy_route_truck1[len(greedy_route_truck1)-1][-2]
for package in greedy_route_truck3:
    package[-1] = truck1_finish_time

# Calculate delivery times for remaining trucks
t.calculate_time(truck2_distance_info, greedy_route_truck2)
t.calculate_time(truck3_distance_info, greedy_route_truck3)


# This begins the section of the user interface
print("***************************************************")
print("* Welcome to the package delivery system for WGU! *")
print("***************************************************\n")

# Get the total distance of the routes taken and print to the screen
total_distance = d.get_total_distance(greedy_route_truck1) + \
                 d.get_total_distance(greedy_route_truck2) + \
                 d.get_total_distance(greedy_route_truck3)
print(f"The distance required to deliver all packages was: {total_distance:0.2f} miles.\n")

# Ask user what they would like to do
print("Please enter '1' to get the status of a package at a particular time.\n"
      "Please enter '2' to get the status of all packages at a particular time."
      "Or alternatively enter 'quit' to quit the program.")

# Store the user response
answer = input("Response: ")

# Boolean used to continuously loop until we designate it to be false
my_boolean = True
# Boolean used to detect if package was found so we can skip remaining loops
was_found = False

while my_boolean:
    # Get status of a particular package choice
    if answer == '1':
        selected_package = int(input("Please enter the package id you would like to inspect: "))  # Get package id
        selected_time = datetime.timedelta()  # Create time delta
        time = input("Please enter time you would like to search for in the format "
                     "'HH:MM:SS': ")
        # Split the time so we can work with it
        (hour, minute, second) = time.split(":")
        selected_time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

        # Get time that package will be delivered and when it can start to be delivered
        delivery_time = datetime.timedelta()
        start_time = datetime.timedelta()

        # Loop through trucks
        for package in greedy_route_truck1:
            # If the package the user selected is on truck one do the following
            if int(package[0]) == selected_package:
                (package_hour, package_minute, package_second) = package[9].split(":")
                delivery_time = datetime.timedelta(hours=int(package_hour), minutes=int(package_minute),
                                                   seconds=int(package_second))

                (start_hour, start_minute, start_second) = package[10].split(":")
                start_time = datetime.timedelta(hours=int(start_hour), minutes=int(start_minute),
                                                seconds=int(start_second))
                if selected_time <= start_time:
                    print(f"Package {package[0]}: is at the hub")
                    was_found = True
                    break
                if start_time <= selected_time <= delivery_time:
                    print(f"Package {package[0]}: is en route")
                    was_found = True
                    break
                if selected_time >= delivery_time:
                    was_found = True
                    print(f"Package {package[0]}: is delivered")
                    break
            else:
                continue

        for package in greedy_route_truck2:
            # If the package the user selected is on truck one do the following
            if int(package[0]) == selected_package:
                (package_hour, package_minute, package_second) = package[9].split(":")
                delivery_time = datetime.timedelta(hours=int(package_hour), minutes=int(package_minute),
                                                   seconds=int(package_second))

                (start_hour, start_minute, start_second) = package[10].split(":")
                start_time = datetime.timedelta(hours=int(start_hour), minutes=int(start_minute),
                                                seconds=int(start_second))
                if selected_time <= start_time:
                    print(f"Package {package[0]}: is at the hub")
                    was_found = True
                    break
                if start_time <= selected_time <= delivery_time:
                    print(f"Package {package[0]}: is en route")
                    was_found = True
                    break
                if selected_time >= delivery_time:
                    was_found = True
                    print(f"Package {package[0]}: is delivered")
                    break
            else:
                continue

        for package in greedy_route_truck3:
            # If the package the user selected is on truck one do the following
            if int(package[0]) == selected_package:
                (package_hour, package_minute, package_second) = package[9].split(":")
                delivery_time = datetime.timedelta(hours=int(package_hour), minutes=int(package_minute),
                                                   seconds=int(package_second))

                (start_hour, start_minute, start_second) = package[10].split(":")
                start_time = datetime.timedelta(hours=int(start_hour), minutes=int(start_minute),
                                                seconds=int(start_second))
                if selected_time <= start_time:
                    print(f"Package {package[0]}: is at the hub")
                    was_found = True
                    break
                if start_time <= selected_time <= delivery_time:
                    print(f"Package {package[0]}: is en route")
                    was_found = True
                    break
                if selected_time >= delivery_time:
                    was_found = True
                    print(f"Package {package[0]}: is delivered")
                    break
            else:
                continue

        answer = input("Please give another package you would like to search for or type 'quit': ")
        if answer != 'quit':
            pass
        else:
            print("\nGoodbye!")
            my_boolean = False

    # Get status of all packages selection
    elif answer == '2':

        answer = input("Please give another package you would like to search for or type 'quit': ")
        if answer != 'quit':
            pass
        else:
            print("\nGoodbye!")
            my_boolean = False
    elif answer == 'quit':
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid response, try again: ")
        answer = input()
