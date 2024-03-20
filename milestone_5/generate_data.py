import csv
from faker import Faker
import random
import sys

def generate_data(num_employees):
    fake = Faker()
    departments = ['HR', 'Finance', 'Marketing', 'IT']
    with open('database.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Hiring Date', 'Department', 'Birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_employees):
            name = fake.name()
            hiring_date = fake.date_this_decade()
            department = random.choice(departments)
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
            writer.writerow({'Name': name, 'Hiring Date': hiring_date, 'Department': department, 'Birthday': birthday})

if __name__ == '__main__':
    num_employees = int(sys.argv[1])
    generate_data(num_employees)
