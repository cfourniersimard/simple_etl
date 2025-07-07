import pandas as pd
from sqlalchemy import create_engine

# Connect to the SQLite database
engine = create_engine('sqlite:///realestate_database.db')
query = "SELECT * FROM multiplex"
df = pd.read_sql(query, engine)

# Print the DataFrame
print(df)
