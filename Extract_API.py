import requests

# Pull from API

def get_people_api():
    endpoint = requests.get("https://swapi.dev/api/people/")
    people = endpoint.json()
    # print(people)
    return people

def get_starships_api():
    endpoint = requests.get("https://swapi.dev/api/starships/")
    starships = endpoint.json()
    # print(starships)
    return starships

def get_films_api():
    endpoint = requests.get("https://swapi.dev/api/films/")
    films = endpoint.json()
    # print(films)
    return films

def get_vehicles_api():
    endpoint = requests.get("https://swapi.dev/api/vehicles/")
    vehicles = endpoint.json()
    # print(vehicles)
    return vehicles

def get_species_api():
    endpoint = requests.get("https://swapi.dev/api/species/")
    species = endpoint.json()
    # print(species)
    return species

def get_planets_api():
    endpoint = requests.get("https://swapi.dev/api/planets/")
    planets = endpoint.json()
    return planets

# Call functions

get_people_api()
get_starships_api()
get_films_api()
get_vehicles_api()
get_species_api()
get_planets_api()

# Setting retrieve data
people = get_people_api()
starships = get_starships_api()
films = get_films_api()
vehicles = get_vehicles_api()
species = get_species_api()
planets = get_planets_api()


# Checking type
print(type(people))
print(type(starships))
print(type(films))
print(type(vehicles))
print(type(species))
print(type(planets))



