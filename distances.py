import csv
import datetime

# Open and read in package_csv files as a list so we can work with the data
with open("./resources/distance_table.csv", "r", encoding='utf-8-sig') as distance_table:
    distances = list(csv.reader(distance_table, delimiter=","))

with open("./resources/distance_table_with_names.csv", "r", encoding='utf-8-sig') as distance_table_names:
    distance_with_names = list(csv.reader(distance_table_names, delimiter=","))


# This determines the next shortest route to deliver to
def get_next_shortest(current_location, hashmap, skipped_list, truck_number):
    shortest_value = 100.0  # Starting minimum value to compare against
    shortest_value_index = 0  # Index of our next package to deliver to, with the shortest distance
    num = 0  # Our number we iterate to compare against all the indexes that are from that location
    size = len(distances)  # Size of the distance map
    global package_id

    # While the number is less than the size of the distances table, loop through and get distances
    while num < size:

        # If the current distance is less than or equal to our shortest value we update
        if get_current_distance(num, current_location) <= shortest_value:
            # Loop through the hashmap of packages
            for i in range(1, 41):
                # If the number is in our skip list, we don't want to search the hashmap for that value
                # since it has been removed.
                if i in skipped_list:
                    continue
                try:
                    # If the hashmap at the index matches the distance w/ names table assign these values
                    if hashmap.get_val(i)[1] == distance_with_names[num][2]:
                        if 'Can only be' in hashmap.get_val(i)[7] and truck_number == 2:
                            shortest_value = get_current_distance(num, current_location)
                            shortest_value_index = num
                            package_id = i
                            time = hashmap.get_val(i)[5]

                            # Most important packages so we add to first truck if possible
                            return shortest_value, current_location, shortest_value_index, package_id, time

                        if 'Delayed' in hashmap.get_val(i)[7] and truck_number != 3:
                            continue

                        if 'Wrong address' in hashmap.get_val(i)[7] and truck_number != 3:
                            updated = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD', '2',
                                       'Wrong address listed', 'at the hub']
                            hashmap.update(i, updated)
                            continue

                        if '10:30' in hashmap.get_val(i)[5] or '9:00' in hashmap.get_val(i)[5] and truck_number == 1:
                            shortest_value = get_current_distance(num, current_location)
                            shortest_value_index = num
                            package_id = i
                            time = hashmap.get_val(i)[5]

                            # Most important packages so we add to first truck if possible
                            return shortest_value, current_location, shortest_value_index, package_id, time

                        shortest_value = get_current_distance(num, current_location)
                        shortest_value_index = num
                        package_id = i
                    continue

                except TypeError:  # Excepts if there is a None value in our hashmap
                    pass
            num += 1
        # Catch all, will continue in the loop
        else:
            num += 1
            continue
    time = ''  # Needed so we don't get index out of range
    # Return the shortest value, current location index, and shortest value index
    return shortest_value, current_location, shortest_value_index, package_id, time


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

        for i in range(len(list_of_indexes)):  # TO DO NEED TO CHECK ALL DISTANCES ARE CORRECT
            # ALSO NEED TO CHECK THAT ALL INDEXES GET HIT
            if list_of_indexes[i] is None:
                continue
            if i == list_length - 1:
                total_distance += get_current_distance(int(list_of_indexes[i - 1]), int(list_of_indexes[i]))
                continue
            total_distance += get_current_distance(int(list_of_indexes[i]), int(list_of_indexes[i + 1]))
            # print(get_current_distance(int(list_of_indexes[i]), int(list_of_indexes[i + 1])))
    except TypeError:
        pass

    # print(list_of_indexes)
    return total_distance


# Calculates time of delivery for a package
def calculate_time(distance, list):
    pass
