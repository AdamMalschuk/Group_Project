import pandas as pd
import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, Float, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy_utils import database_exists, create_database
#from Transform import (Function with pandas dfs)

# 1 Connect to SQL Server
def get_sql_connection():
    engine = db.create_engine('dialect://User:password@sa:localhost:1433//starwars')
    return engine

try:
    with get_sql_connection().connect() as conn:
        print("Connection successful")

except Exception as e:
    print("Connection Failed: ", e)


# Creating database with Alchemy
engine = get_sql_connection()
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))


# 2 Receive transformed DataFrames
#Each dataframe will need a variable
#function from transform will be unpacked (will change once given access to transform file)

characters_df, starships_df, films_df, vehicles_df, species_df, planets_df = transform_data()

#check data is fine
print(characters_df.head())
print(starships_df.head())
print(films_df.head())
print(vehicles_df.head())
print(species_df.head())
print(planets_df.head())


# 3 Prep tables to match schema

meta = MetaData()
characters_df = Table(
    "characters",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("height", Float),
    Column("mass", Float),
    Column("hair color", String),
    Column("skin color", String),
    Column("eye color", String),
    Column("birth year", String),
    Column("gender id", String, foreign_key="gender.id"),
    Column("homeworld id", String, foreign_key="homeworld.id"),
    Column("films id", String, foreign_key="films.id"),
    Column("species", String),
)

gender = Table(
    "gender",
    meta,
    Column("id", Integer, primary_key=True),
    Column("gender", String),
)

starships_df = Table(
    "starships",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("model", String),
    Column("manufacturer", String),
    Column("length", Float),
    Column("max atmosphering speed", Float),
    Column("num of crew members", Integer),
    Column("passenger number", Integer),
    Column("pilot id", String, foreign_key="pilot.id"))

films_df = Table(
    "films",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)


# 4 Insert into SQL Server
    # use .to_sql()

# 5 Check data is inserted successfully