import csv
import datetime

# Open and read in package_csv files as a list so we can work with the data
with open("./resources/distance_table.csv", "r", encoding='utf-8-sig') as distance_table:
    distances = list(csv.reader(distance_table, delimiter=","))

with open("./resources/distance_table_with_names.csv", "r", encoding='utf-8-sig') as distance_table_names:
    distance_with_names = list(csv.reader(distance_table_names, delimiter=","))


# This determines the next shortest route to deliver to
def get_greedy_route(list_of_packages_on_truck, updated_greedy_route):
    shortest_value = 100.0  # Starting minimum value to compare against
    index_of_shortest_value = 0  # Index of shortest value found matched against distance_table_with_names
    package_id_of_shortest = 0
    prior_index = 0  # Starting index of previous package

    # Get the previous packages index
    for distance in distance_with_names:
        test = updated_greedy_route[-1]
        if updated_greedy_route[-1][1] == distance[2]:
            prior_index = int(distance[0])

    # Find shortest route for next delivery
    for package in list_of_packages_on_truck:
        for index in distance_with_names:
            if package[1] == index[2]:  # Matched addresses
                if get_current_distance(prior_index, int(index[0])) <= shortest_value:
                    shortest_value = get_current_distance(prior_index, int(index[0]))
                    index_of_shortest_value = int(index[0])
                    package_id_of_shortest = int(package[0])

    return shortest_value, index_of_shortest_value, package_id_of_shortest


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
                # If it matches then append the index number to our list
                if item[2] == truck_list[num][1]:
                    list_of_indexes.append(item[0])
                    break
    except TypeError:
        pass

    try:
        for i in range(len(list_of_indexes)):
            # If there is an empty spot on a truck we skip it
            if i == list_length - 1:
                # list_of_distances.append(get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i])))
                # total_distance += get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i]))
                continue

            else:
                list_of_distances.append(get_current_distance(0, int(list_of_indexes[i + 1])))
                total_distance += get_current_distance(int(list_of_indexes[i]), int(list_of_indexes[i + 1]))

    except IndexError:
        pass
    print(f"List of Distances{list_of_distances}")
    return total_distance


# Calculates time of delivery for a package
def calculate_time(distance, truck_list):
    pass
