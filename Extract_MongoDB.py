from pymongo import MongoClient


# Extract characters and starships as lists of dictionaries, excluding _id
def extract_data_mongodb(database):
    characters_list = list(database["characters"].find({}, {"_id": 0}))
    starships_list = list(database["starships"].find({}, {"_id": 0}))

    return characters_list, starships_list


# Replace pilot IDs with matching character names in the starships collection
def replace_pilot_ids_with_names(database):
    starship_collection = database["starships"]
    character_collection = database["characters"]

    for starship in starship_collection.find({}):
        pilot_names = []

        for pilot in starship["pilots"]:
            character = character_collection.find_one({"_id": pilot})

            if character:
                pilot_names.append(character["name"])
            else:
                pilot_names.append(pilot)

        starship_collection.update_one(
            {"_id": starship["_id"]},
            {"$set": {"pilots": pilot_names}})


try:
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["starwars"]

        # Replacing pilot IDs before extracting the updated data
        replace_pilot_ids_with_names(db)
        characters, starships = extract_data_mongodb(db)

except Exception as e:
    raise Exception("The following error occurred: ", e)
