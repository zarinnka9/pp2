import csv

data = [
    ['Alice', '1234567890'],
    ['Bob', '2345678901'],
    ['Charlie', '3456789012'],
    ['Diana', '4567890123'],
    ['Eve', '5678901234']
]

with open('phonebook.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("phonebook.csv has been created.")