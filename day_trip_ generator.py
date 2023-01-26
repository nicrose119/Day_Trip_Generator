from lists import destinations, restaurants, mode_of_transportation, type_of_entertainment
import random

def generate_trip():
    location = random.choice(destinations)
    restaurant = random.choice(restaurants)
    transportation = random.choice(mode_of_transportation)
    entertainment = random.choice(type_of_entertainment)

    trip = [location, restaurant, transportation, entertainment]
    return trip

def display_trip(selections_list):
    for selection in selections_list:
        print(selection)


user_response = 'n'
while user_response != 'y':
    trip = generate_trip()
    display_trip(trip)
    user_response = input("Are you satisfied with your trip? y/n \n" ) 
    if user_response == 'y':
        print("Here are the final details of your random day trip:\n" )
        display_trip(trip)
        print("")
        print ("Enjoy!no")

