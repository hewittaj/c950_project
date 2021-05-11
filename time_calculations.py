import datetime


# Calculate the time needed for each delivery on a truck
def calculate_time(distance_info, truck_list):
    for info in distance_info:
        calculated_time = info[0] / 18  # Calculate time traveled by using avg speed of truck
        calculated_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(calculated_time * 60, 60))
        print(f"{calculated_minutes}")
