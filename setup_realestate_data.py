import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('realestate_database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS multiplex (
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    number_of_floors INTEGER,
    number_of_apartments INTEGER,
    annual_rent_revenue REAL,
    occupancy_rate REAL,
    year_built INTEGER,
    property_manager TEXT,
    average_rent_per_apartment REAL,
    maintenance_cost REAL
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO multiplex (name, location, number_of_floors, number_of_apartments, annual_rent_revenue, occupancy_rate, year_built, property_manager, average_rent_per_apartment, maintenance_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('Multiplex A', 'New York', 5, 50, 1.5e6, 0.95, 2005, 'Manager A', 2500, 0.2e6),
    ('Multiplex B', 'Los Angeles', 4, 40, 1.2e6, 0.90, 2010, 'Manager B', 2400, 0.18e6),
    ('Multiplex C', 'Chicago', 6, 60, 1.8e6, 0.92, 2008, 'Manager C', 2600, 0.22e6),
    ('Multiplex D', 'Houston', 7, 70, 2.1e6, 0.88, 2012, 'Manager D', 2700, 0.25e6),
    ('Multiplex E', 'Phoenix', 3, 30, 0.9e6, 0.85, 2015, 'Manager E', 2300, 0.15e6),
    ('Multiplex F', 'Philadelphia', 5, 55, 1.4e6, 0.93, 2007, 'Manager F', 2450, 0.19e6),
    ('Multiplex G', 'San Antonio', 4, 45, 1.1e6, 0.87, 2011, 'Manager G', 2350, 0.17e6),
    ('Multiplex H', 'San Diego', 6, 65, 1.9e6, 0.89, 2013, 'Manager H', 2650, 0.23e6),
    ('Multiplex I', 'Dallas', 7, 75, 2.2e6, 0.91, 2014, 'Manager I', 2750, 0.26e6),
    ('Multiplex J', 'San Jose', 3, 35, 1.0e6, 0.86, 2016, 'Manager J', 2200, 0.16e6)
])

# Commit and close
conn.commit()
conn.close()
