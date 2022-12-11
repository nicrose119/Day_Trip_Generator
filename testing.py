#from lists import day_trip_elements, destinations, restaurants, transportation, entertainment
# import random
# destinations = ['New York City', 'Miami', 'Malibu', 'Aspen', 'Nashville']
# location = random.choice(destinations)   
# print(location)



from lists import destinations, restaurants, mode_of_transportation, type_of_entertainment

import random
destinations, restaurants, mode_of_transportation, type_of_entertainment
location = random.choice(destinations)
restaurant = random.choice(restaurants)
transportation = random.choice(mode_of_transportation)
entertainment = random.choice(type_of_entertainment)

print(location, restaurant, transportation, entertainment, sep='\n')





    