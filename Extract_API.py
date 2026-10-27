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

# Setting retrieve data
peoples = get_people_api()
starships = get_starships_api()
films = get_films_api()
vehicles = get_vehicles_api()
species = get_species_api()
planets = get_planets_api()



# Modify urls to names in films

starship_name_by_url = {ship['url']: ship['name'] for ship in starships}
vehicles_name_by_url = {vehicle['url']: vehicle['name'] for vehicle in vehicles}
planet_name_by_url = {planet['url']: planet['name'] for planet in planets}
people_name_by_url = {characters['url']: characters['name'] for characters in peoples}
species_name_by_url = {species['url']: species['name'] for species in species}

for film in films:
    film['starships'] = [
        starship_name_by_url.get(url, url)
        for url in film['starships']
    ]
    film['vehicles'] = [
        vehicles_name_by_url.get(url, url)
        for url in film['vehicles']
    ]
    film['planets'] = [
        planet_name_by_url.get(url, url)
        for url in film['planets']
    ]
    film['characters'] = [
        people_name_by_url.get(url, url)
        for url in film['characters']
    ]
    film['species'] = [
        species_name_by_url.get(url, url)
        for url in film['species']
    ]

print(films)