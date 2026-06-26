def military_to_minutes(time):
    time = int(time)
    hours = time // 100
    minutes = time % 100
    return hours * 60 + minutes


shift = float(input('Enter how many hours each boat crew is to be on the water: '))

# Boat 1
boat_1_start = input('Enter first boat start time (military time): ')
boat_1_end = input('Enter first boat end time (military time): ')

boat_1_time_on_water = (
    military_to_minutes(boat_1_end)
    - military_to_minutes(boat_1_start)
)

more_times_1 = input('Do you have more times to enter for boat 1? (y/n): ')

while more_times_1.lower() == 'y':
    boat_1_start = input('Enter first boat start time (military time): ')
    boat_1_end = input('Enter first boat end time (military time): ')

    boat_1_time_on_water += (
        military_to_minutes(boat_1_end)
        - military_to_minutes(boat_1_start)
    )

    more_times_1 = input('Do you have more times to enter for boat 1? (y/n): ')

# Boat 2
boat_2_start = input('Enter second boat start time (military time): ')
boat_2_end = input('Enter second boat end time (military time): ')

boat_2_time_on_water = (
    military_to_minutes(boat_2_end)
    - military_to_minutes(boat_2_start)
)

more_times_2 = input('Do you have more times to enter for boat 2? (y/n): ')

while more_times_2.lower() == 'y':
    boat_2_start = input('Enter second boat start time (military time): ')
    boat_2_end = input('Enter second boat end time (military time): ')

    boat_2_time_on_water += (
        military_to_minutes(boat_2_end)
        - military_to_minutes(boat_2_start)
    )

    more_times_2 = input('Do you have more times to enter for boat 2? (y/n): ')

# Convert total minutes to decimal hours
boat_1_hours = round(boat_1_time_on_water / 60, 2)
boat_2_hours = round(boat_2_time_on_water / 60, 2)

print(f'\nBoat 1 time on water: {boat_1_hours} of {shift} hours')
print(f'Boat 2 time on water: {boat_2_hours} of {shift} hours')

# Convert decimal hours to hours and minutes
boat_1_whole_hours = boat_1_time_on_water // 60
boat_1_minutes = boat_1_time_on_water % 60

boat_2_whole_hours = boat_2_time_on_water // 60
boat_2_minutes = boat_2_time_on_water % 60

print(
    f'Boat 1 total time: {boat_1_whole_hours} hours '
    f'{boat_1_minutes} minutes'
)

print(
    f'Boat 2 total time: {boat_2_whole_hours} hours '
    f'{boat_2_minutes} minutes'
)

# Remaining shift time
boat_equal_1 = round(shift - boat_1_hours, 2)
boat_equal_2 = round(shift - boat_2_hours, 2)

if boat_1_hours >= shift:
    print('\nBoat 1 crew has been on the water for more than or equal to the shift time.')
else:
    remaining_minutes_1 = round(boat_equal_1 * 60)
    remaining_hours_1 = remaining_minutes_1 // 60
    remaining_mins_1 = remaining_minutes_1 % 60

    print(f'\nBoat 1 crew needs {remaining_hours_1} hours {remaining_mins_1} minutes more.')

if boat_2_hours >= shift:
    print('Boat 2 crew has been on the water for more than or equal to the shift time.')
else:
    remaining_minutes_2 = round(boat_equal_2 * 60)
    remaining_hours_2 = remaining_minutes_2 // 60
    remaining_mins_2 = remaining_minutes_2 % 60

    print(f'Boat 2 crew needs {remaining_hours_2} hours {remaining_mins_2} minutes more.')