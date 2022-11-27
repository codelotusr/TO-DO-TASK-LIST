import csv
from pyllist import sllist

# read data from duomenys.csv and store it in a singly linked lists
with open('duomenys.csv', 'r') as f:
    reader = csv.reader(f)
    data = sllist()
    for row in reader:
        data.append(row)
print(data[0][0])


