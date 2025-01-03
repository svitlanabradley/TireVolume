'''
tire_volume.py reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire. Stores values in volumes.txt file.
'''
# import the math module for using math.pi
import math

# function tire_volume calculates and returns results
def tire_volume (w, a, d):
    tire_volume = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
    return tire_volume

# get input from a user and convert user input from a string to a number
width = int(input('\nEnter the width of the tire in mm (ex 205): '))
aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

if width <= 205 and aspect <= 60 and diameter <= 15:
    volume = tire_volume(width, aspect, diameter)

    # display the results for user to see 
    print(f'\nThe approximate volume is {volume:.2f} liters')
    
    if width == 185 and aspect == 50 and diameter == 14:
        price = "$123,57"
    elif width == 205 and aspect == 60 and diameter == 15:
        price = "$137,41"
    elif width == 215 and aspect == 60 and diameter == 16:
        price = "$112,82"
    elif width == 235 and aspect == 75 and diameter == 15:
        price = "$113,53"
    # ask the user if he wants to buy tires with the dimensions that he entered
    answer = input(f'The tires with the dimensions that you entered cost: {price}\nWould you like to buy it? ')

    #If the user answers “yes”, the program ask for phone number
    if answer == "yes":
        phone_number = input("What is your phone number? ")
    else:
        phone_number = "-"

    # Import the datetime class from the datetime
    # module so that it can be used in this program.
    from datetime import datetime

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Open a text file named volumes.txt in append mode.
    with open("volumes.txt", "at") as volumes_file:
        # print information to the file
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {phone_number}", file=volumes_file)

else:
    print('Wrong input')


