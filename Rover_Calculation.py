# ENDG 233 Fall 2023
# Portfolio Project 1
# rover.py
# Program for calculating the time it takes a rover to travel depending on rover parameters and storm status.
# Yassin Soliman 30205455


# This module can be used to access math.floor() and math.ceil() as needed.
# e.g. math.floor(10/3) = 3, math.ceil(10/3) = 4
import math

# Tip: Create constants that can be used to store the rover parameters.
# Units should be indicated in comments
# e.g.  battery_1 = 100         # 100 kWh



# BEGIN CODE HERE
import math # So we can use math.ceil

rover_selection = int(input("Which rover would you like to move? ")) # Asks user for which rover
distance = int(input("How far is the mission in km? ")) # Asks user for mission distance in km
storm = str(input("Is there a storm in the forecast (True or False)? ")) # Asks user if there is a storm with True or False answer

# If the rover selection is not 1, 2, or 3 then program wont recognize it
if rover_selection not in [1,2,3]:
    print("Rover number not recognized.")
    exit()

if rover_selection == 1: # Charlie
    battery = 100 # kW battery
    efficiency = 50/100 # kWh/km efficiency
    solar_capacity = 5 # kW solar capacity
    average_velocity = 5 # km/h average velocity

if rover_selection == 2: # Alpha
    battery = 130 # kW battery
    efficiency = 40/100 # kWh/km efficiency
    solar_capacity = 8 # kW solar capacity
    average_velocity = 4 # km/h average velocity

if rover_selection == 3: # November
    battery = 80 # kW battery
    efficiency = 30/100 # kWh/km efficiency
    solar_capacity = 4 # kW solar capacity
    average_velocity = 6 # km/h average velocity

total_time = distance / average_velocity # Distance/ average velocity gives time in hours
charge_distance = battery / efficiency # Distance in one charge is battery divided by efficiency
    
if distance >= charge_distance: # If distance is higher than one charge distance then:
        number_of_charges = distance / charge_distance - 1 # Figures out how many times the battery needs to be charged subtracted from the one full battery that was used
        number_of_charges = math.ceil(number_of_charges) # Rounds the number of charges up because you have to charge the battery fully
        charge_time = battery / solar_capacity * number_of_charges # Charge time found by dividing battery by solar capacity times number of charges
        total_time = total_time + charge_time # Add the charge time to total time



# Conditional for storm
if storm == "True":
    total_time = total_time * 1.2 # Storm causes total time to be multiplied by 1.2



# This print statement should be your final line of code.
# You may change the variable names or where the statement is placed within a logic block, but the rest of the statement should remain the same.
print("The total travel time for Rover {0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_selection, distance, total_time))