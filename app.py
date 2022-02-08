import csv

dataset1 = []
dataset2 = []

with open("finalsorter.csv","r") as w:
    cfinalsorter = csv.reader(w)
    for i in cfinalsorter:
        dataset1.append(i)

with open("dataset_1.csv","r") as f:
    cdataset = csv.reader(f)
    for i in cdataset:
        dataset2.append(i)

header1 = dataset1[0]
header2 = dataset2[0]

planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]

headers = header1+header2

planetdata = []
for index,datarow in enumerate(planetdata2):
    planetdata.append( planetdata1[index] + planetdata2[index])

with open("finaldata.csv","a+") as g:
    cfinaldata = csv.writer(g)
    cfinaldata.writerow(headers)
    cfinaldata.writerows(planetdata)

