import csv
from faker import Faker

fake = Faker()

# Define the number of records you want
num_records = 100

# Define the CSV file name
csv_file = 'fake_data.csv'

# Define the field names
fieldnames = ['id', 'name', 'email', 'age', 'city']

# Create and write to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, num_records + 1):
        writer.writerow({
            'id': i,
            'name': fake.name(),
            'email': fake.email(),
            'age': fake.random_int(min=18, max=80),
            'city': fake.city()
        })

print(f"Generated {num_records} records in {csv_file}")
