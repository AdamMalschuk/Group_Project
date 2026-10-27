from pymongo import MongoClient


def extract_data_mongodb():
    with MongoClient("mongodb://localhost:27017/") as client:
        database = client["starwars"]

        # Converting each collection into a list of dictionaries
        characters = list(database["characters"].find({}, {"_id": 0}))
        starships = list(database["starships"].find({}, {"_id": 0}))

    return characters, starships
