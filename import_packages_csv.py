import csv
from hashmap import HashMap as hm

"""
This module is for working with the cleaned up package_csv file.
"""

# Open the package_csv file and then scan it into the hashmap.
with open("./resources/package_info.csv", 'r', encoding='utf-8-sig') as p:
    reader = csv.reader(p, delimiter=",")
    hash_map = hm()  # Create an instance of a hashmap

    for row in reader:  # Read in each value delimited by commas
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip = row[4]
        package_deadline = row[5]
        package_weight = row[6]
        package_notes = row[7]
        delivery_status = 'at the hub'  # Tells where the package is currently at
        delivery_time = ''  # States when the package was delivered
        start_time = ''  # States when package can start to be delivered

        all_values = [package_id, package_address, package_city,  # Create a list of values to store in hash map
                      package_state, package_zip, package_deadline, package_weight, package_notes, delivery_status,
                      delivery_time, start_time]
        hash_map.insert(package_id, all_values)  # Insert into hash_map,

    # Get all of the packages in our hashmap
    def get_hashmap():
        return hash_map
