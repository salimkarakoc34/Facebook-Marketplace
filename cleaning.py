import csv
import webscraping

# Open the text file for reading
with open('facebookcars.txt', 'r') as f:
    lines = f.readlines()

data = []

i = 0
while i < len(lines):
    price = lines[i]
    i += 1
    if lines[i].startswith('$'):
        i += 1
    year_make_model = lines[i].strip().split(' ', 1)
    if len(year_make_model) < 2:
        i += 1
        continue
    year = year_make_model[0]
    make_model = year_make_model[1]
    i += 1

    # location
    location = lines[i].strip()
    i += 1

    #  mileage
    if i < len(lines):
        mileage = lines[i].split()[0]
        i += 1
    else:
        mileage = 'N/A'

    data.append([make_model.split()[0], ' '.join(make_model.split()[1:]), year, mileage, price, location])

with open('cleandata.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['Make', 'Model', 'Year', 'Mileage', 'Price', 'Location'])

    writer.writerows(data)
