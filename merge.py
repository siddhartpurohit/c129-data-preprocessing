import csv

data = []

with open("dataset_2.csv","r") as w:
    creader = csv.reader(w)
    for i in creader:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for i in planet_data:
    i[2] = i[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])

with open("finalsorter.csv","a+") as a:
    c = csv.writer(a)
    c.writerow(headers)
    c.writerows(planet_data)

