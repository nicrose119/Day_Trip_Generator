# #user_satisfied = False

# import random
# destinations = ['New York City', 'Miami', 'Malibu', 'Aspen', 'Nashville']
# location = random.choice(destinations)   
# print(location)

# import random
# restaurants = ['Prime & Proper Steak House', 'Calexico', 'Slows BBQ', 'Island Eats', 'Bessa']
# restaurant = random.choice(restaurants)
# print(restaurant)

# import random
# mode_of_transportation = ['Plane', 'Train', 'Helicoptor', 'RV', 'Charter Bus']
# transportation = random.choice(mode_of_transportation)
# print(transportation)

# import random
# type_of_entertainment = ['Live Theatre', 'Concert', 'Day at the Spa', 'Guided Tour of citys attractions', 'Sky Diving']
# entertainment = random.choice(type_of_entertainment)
# print(entertainment)

# user_response = False

# user_satisfied = input("Are you satisfied with the outcome of your trip? ")
# print(user_satisfied)

# while user_response == False:
#     user_feedback = input("Which item on your list would you like to change?")
#     print(user_feedback)
#     if user_feedback == "destination":
#         import random
#         destinations = ['New York City', 'Miami', 'Malibu', 'Aspen', 'Nashville'] 
#         location = random.choice(destinations)  
#         print(location)



from lists import destinations, restaurants, mode_of_transportation, type_of_entertainment

import random
destinations, restaurants, mode_of_transportation, type_of_entertainment
location = random.choice(destinations)
restaurant = random.choice(restaurants)
transportation = random.choice(mode_of_transportation)
entertainment = random.choice(type_of_entertainment)

print(location, restaurant, transportation, entertainment, sep='\n')