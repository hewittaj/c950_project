import csv
import datetime

# Open and read in package_csv files as a list so we can work with the data
with open("./resources/distance_table.csv", "r", encoding='utf-8-sig') as distance_table:
    distances = list(csv.reader(distance_table, delimiter=","))

with open("./resources/distance_table_with_names.csv", "r", encoding='utf-8-sig') as distance_table_names:
    distance_with_names = list(csv.reader(distance_table_names, delimiter=","))


# This determines the next shortest route to deliver to
def get_greedy_route(list_of_packages_on_truck):
    shortest_value = 100.0  # Starting minimum value to compare against
    shortest_package_id = 0  # Id of shortest package
    shortest_package_index = 0  # Index of shortest package
    greedy_route = {}  # Route that will be taken by using the greedy algorithm starting from hub i.e zero
    first_cycle = True  # Keeps track if it is the first time through so we don't assign 0 as shortest value
    length_of_packages = len(list_of_packages_on_truck)
    temp_distance = 0.0  # Temp distance that we use for assigning to shortest_value, constantly moving

    for item in list_of_packages_on_truck:  # Cycle through packages on truck
        for distance in distance_with_names:
            if item[1] == distance[2]:  # If the items address matches the address in our .csv
                if first_cycle:  # Starting from hub
                    temp_distance = get_current_distance(0, int(distance[0]))
                    if temp_distance <= shortest_value:
                        shortest_value = temp_distance
                        shortest_package_id = int(item[0])
                        shortest_package_index = int(distance[0])
                        continue
                else:
                    values = greedy_route.values()
                    updated = list(values)
                    temp_distance = get_current_distance(updated[1], int(distance[0]))
                    if temp_distance <= shortest_value:
                        shortest_value = temp_distance
                        shortest_package_id = int(item[0])
                        shortest_package_index = int(distance[0])
                        continue
        first_cycle = False

        for i in range(length_of_packages - 1):  # Pop package info and append to route
            if int(list_of_packages_on_truck[i][0]) == shortest_package_id:
                greedy_route.update({"package_id": shortest_package_id})
                greedy_route.update({"index": shortest_package_index})
                greedy_route.update({"package_info": list_of_packages_on_truck.pop(i)}) # Pop package info and append to route

    return greedy_route


# Get the current distance using the row and column passed.
def get_current_distance(row, column):
    current_distance = distances[row][column]
    if distances[row][column] == '':
        current_distance = distances[column][row]
    return float(current_distance)


# Get the total distance of a truck's route
def get_total_distance(truck_list):
    # Length of our trucks list
    list_length = len(truck_list)
    list_of_indexes = []
    list_of_distances = []
    total_distance = 0.0
    try:
        # Loop through the length of our list of trucks and find the indexes
        for num in range(list_length):
            # Loop through our items in our .csv file
            for item in distance_with_names:

                if truck_list[num][1] is None:
                    continue
                # If it matches then append the index number to our list
                if item[2] == truck_list[num][1]:
                    list_of_indexes.append(item[0])
    except TypeError:
        pass

    try:
        for i in range(len(list_of_indexes)):
            # If there is an empty spot on a truck we skip it
            if list_of_indexes[i] is None:
                continue
            if i == list_length - 1:
                list_of_distances.append(get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i])))
                total_distance += get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i]))
                continue
            list_of_distances.append(get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i])))
            total_distance += get_current_distance(int(list_of_indexes[i]), int(list_of_indexes[i + 1]))
    except IndexError:
        pass
    print(f"List of Distances{list_of_distances}")
    return total_distance


# Calculates time of delivery for a package
def calculate_time(distance, truck_list):
    pass
