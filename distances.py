import csv
import datetime

# Open and read in package_csv files as a list so we can work with the data
with open("./resources/distance_table.csv", "r", encoding='utf-8-sig') as distance_table:
    distances = list(csv.reader(distance_table, delimiter=","))

with open("./resources/distance_table_with_names.csv", "r", encoding='utf-8-sig') as distance_table_names:
    distance_with_names = list(csv.reader(distance_table_names, delimiter=","))


# This determines the next shortest route to deliver to
def get_next_shortest(current_location):
    shortest_value = 100.0  # Starting minimum value to compare against
    num = 0  # Our number we iterate to compare against all the indexes that are from that location
    size = len(distances)  # Size of the distance map

    # While the number is less than the size of the map, loop through and get distances
    while num < size:
        # If the distance is 0 we aren't moving so we ignore
        if get_current_distance(num, current_location) == 0:
            num += 1
            continue
        # If the current distance is less than or equal to our shortest value we update
        if get_current_distance(num, current_location) <= shortest_value:
            shortest_value = get_current_distance(num, current_location)
            num += 1
            continue
        # Catch all, will continue in the loop
        else:
            num += 1
            continue
    return shortest_value


# Get the current distance using the row and column passed.
def get_current_distance(row, column):
    current_distance = distances[row][column]
    if distances[row][column] == '':
        current_distance = distances[column][row]
    return float(current_distance)
