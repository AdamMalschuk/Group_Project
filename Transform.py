from unittest import result

import pandas as pd
import Extract_API

def createDataFrame(resultset):
    rawData = pd.DataFrame(resultset)
    return rawData
def extractColumn(database, column):
    newDB = pd.DataFrame()
    newDB.insert(0, column, database[column])
    newDB.index.rename(column + "_ID", inplace=True)
    newDB = pd.DataFrame({
        column: database[column].dropna().unique()
    })
    newDB[column + "_ID"] = range(1, len(newDB) + 1)
    newDB2 = database.copy()
    newmap = newDB.set_index(column)[column + "_ID"]
    newDB2[column] = newDB2[column].map(newmap)
    newDB2.rename(columns={column: column + "_ID"}, inplace=True)
    return newDB2,newDB
rawStarships = createDataFrame(Extract_API.starships["results"])
rawPeople = createDataFrame(Extract_API.people["results"])
rawSpecies = createDataFrame(Extract_API.species["results"])
rawFilms = createDataFrame(Extract_API.films["results"])
rawVehicles = createDataFrame(Extract_API.vehicles["results"])
rawPlanets = createDataFrame(Extract_API.planets["results"])

starships,manufacturer = extractColumn(rawStarships, "manufacturer")
print(starships.head())
print(manufacturer.head())