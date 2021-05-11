import datetime


# Calculate the time needed for each delivery on a truck
def calculate_time(distance_info, truck_list):
    adjusted_time = ''
    count = 0
    for info in distance_info:
        calculated_time = info[0] / 18  # Calculate time traveled by using avg speed of truck
        calculated_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(calculated_time * 60, 60))  # Calculate minutes
        #print(truck_list[0][10])
        adjusted_time = datetime.timedelta()  # Our time that will be adjusted by
        prior_time = datetime.timedelta()
        (prior_hour, prior_minute) = truck_list[count][10].split(":")
        prior_time = datetime.timedelta(hours=int(prior_hour), minutes=int(prior_minute))
        (hour, minute) = calculated_minutes.split(":")
        adjusted_time += datetime.timedelta(hours=int(hour), minutes=int(minute))
        print(adjusted_time)
        if count == 0:
            prior_time += datetime.timedelta(hours=int(hour), minutes=int(minute))
            truck_list[count + 1][9] = str(prior_time)

        count += 1

    return truck_list
