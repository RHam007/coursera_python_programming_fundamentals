# Function returns a specific city's population
"""
This function searches a hardcoded dictionary looking for the city key to return the population value

variables:
    - city_populations: dictionary containing city(key):populatio(value)
    - city_name: global variable used as placeholder for user selection (user input not implemented for this function)
    - city: local variable taken from the global city_name variable
    - populations: the returned value based on the identified city

Exceptions:
 - City name not present within the dictionary (see "Output examples" for error messaging)

Output example(s):
 - #The population of New York is 8336817.
 - #City "Tampa" not found in population data.
"""

def get_city_population(populations, city):
    city = city_name
    try:        
        populations = city_populations[city]        
    except KeyError:
        print(f'City "{city}" not found in population data.')
    else:
        print(f"The population of {city} is {populations}.")

city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

city_name = "New York"
populations = get_city_population(city_populations, city_name)
city_name = "Tampa"
populations = get_city_population(city_populations, city_name)