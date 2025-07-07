import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('C:\\Users\\ChristopheFournier-S\\OneDrive - Laps\\Bureau\\simple_etl\\realestate_database.db')
cursor = conn.cursor()

# Calculate KPIs and add them as additional columns
def calculate_kpis():
    # Add new columns for KPIs if they don't exist
    cursor.execute("ALTER TABLE multiplex ADD COLUMN total_revenue_per_apartment REAL")
    cursor.execute("ALTER TABLE multiplex ADD COLUMN maintenance_cost_per_apartment REAL")
    cursor.execute("ALTER TABLE multiplex ADD COLUMN revenue_to_maintenance_ratio REAL")

    # Calculate KPIs for each row and update the table
    cursor.execute("SELECT id, annual_rent_revenue, number_of_apartments, maintenance_cost FROM multiplex")
    rows = cursor.fetchall()

    for row in rows:
        id, annual_rent_revenue, number_of_apartments, maintenance_cost = row

        # Calculate total revenue per apartment
        total_revenue_per_apartment = annual_rent_revenue / number_of_apartments if number_of_apartments else 0

        # Calculate maintenance cost per apartment
        maintenance_cost_per_apartment = maintenance_cost / number_of_apartments if number_of_apartments else 0

        # Calculate revenue to maintenance ratio
        revenue_to_maintenance_ratio = annual_rent_revenue / maintenance_cost if maintenance_cost else 0

        # Update the table with calculated KPIs
        cursor.execute('''
            UPDATE multiplex
            SET total_revenue_per_apartment = ?,
                maintenance_cost_per_apartment = ?,
                revenue_to_maintenance_ratio = ?
            WHERE id = ?
        ''', (total_revenue_per_apartment, maintenance_cost_per_apartment, revenue_to_maintenance_ratio, id))

    # Commit the changes
    conn.commit()

# Call the function to calculate KPIs and update the table
calculate_kpis()

# Close the connection
conn.close()

print("KPIs were successfully calculated and added to the 'multiplex' table.")

