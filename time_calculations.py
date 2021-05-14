import datetime


# Calculate the time needed for each delivery on a truck
def calculate_time(distance_info, truck_list):
    count = 0
    delivery_time = datetime.timedelta()

    for info in distance_info:
        # Calculate time traveled by using avg speed of truck and convert into minutes
        calculated_time = info[0] / 18
        calculated_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(calculated_time * 60, 60))
        calculated_minutes += ':00'
        # Time to travel to the next location/be delivered
        (hour, minute, second) = calculated_minutes.split(":")
        time_to_travel = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

        if count == 0:
            # The time the previous package was delivered, split so we can work with it
            (prior_hour, prior_minute, prior_seconds) = truck_list[count][10].split(":")

            # Calculate the prior time
            delivery_time = datetime.timedelta(hours=int(prior_hour), minutes=int(prior_minute),
                                               seconds=int(prior_seconds))
            delivery_time += time_to_travel
            truck_list[count + 1][9] = str(delivery_time)
            count += 1
            continue
        else:
            # The time the previous package was delivered split so we can work with it

            delivery_time += datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
            truck_list[count + 1][9] = str(delivery_time)
            count += 1

    return truck_list
