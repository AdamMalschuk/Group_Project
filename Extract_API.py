import requests

# Pull from API

def get_people_api():
    endpoint = "https://swapi.dev/api/people"
    people = []
    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        people.extend(data["results"])
        endpoint = data["next"]

    return people


def get_starships_api():
    endpoint = "https://swapi.dev/api/starships/"
    starships = []
    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        starships.extend(data["results"])
        endpoint = data["next"]
    return starships

def get_films_api():
    endpoint = "https://swapi.dev/api/films/"
    films = []
    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        films.extend(data["results"])
        endpoint = data["next"]
    return films

def get_vehicles_api():
    endpoint = "https://swapi.dev/api/vehicles/"
    vehicles = []

    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        vehicles.extend(data["results"])
        endpoint = data["next"]

    return vehicles

def get_species_api():
    endpoint = "https://swapi.dev/api/species/"
    species = []
    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        species.extend(data["results"])
        endpoint = data["next"]

    return species

def get_planets_api():
    endpoint = "https://swapi.dev/api/planets/"
    planets = []
    while endpoint:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()
        planets.extend(data["results"])
        endpoint = data["next"]
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

# Print test
# print(people)
# print(starships)
# print(films)
# print(vehicles)
# print(species)
# print(planets)


# # Checking type
# print(type(people))
# print(type(starships))
# print(type(films))
# print(type(vehicles))
# print(type(species))
# print(type(planets))



