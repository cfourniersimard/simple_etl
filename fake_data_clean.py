import sqlite3
import pandas as pd

# Step 1: Extract
data = pd.read_csv('fake_data.csv')

# Step 2: Transform
# Remove records with age over 60
data = data[data['age'] <= 60]

# Step 3: Load
conn = sqlite3.connect('fake_data.db')
data.to_sql('people', conn, if_exists='replace', index=False)

print("ETL process completed successfully! Records with age over 60 have been removed.")

