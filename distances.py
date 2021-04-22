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
    num = 0
    # print(distances)
    # print(float(distances[1][1]))
    # Infinite loop for some reason!!!
    while num < 28:
        for distance in distances[0][current_location]:
            if distance == '':
                num += 1
                continue
            elif float(distance) <= shortest_value:
                shortest_value = distance
                num += 1
                continue


# Get the current distance using the row and column passed.
def get_current_distance(row, column):
    current_distance = distances[row][column]
    return float(current_distance)


# Get the total distance using the row and column passed, plus the current total
def get_total_distance(row, column, total):
    total_distance = distances[row][column]
    return total + float(total_distance)
