import pandas as pd
import sqlalchemy as db


# 1 Connect to SQL Server
engine = db.create_engine('')

try:
    with engine.connect() as conn:
        print("Connection successful")

except Exception as e:
    print("Connection Failed", e)

# 2 Receive transformed DataFrames



# 3 Prep tables to match schema




# 4 Insert df's into SQL Server
    # use .to_sql()




# 5 Check data is inserted successfully