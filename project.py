import csv
import pandas as pd

f1 = "brightstars.csv"
f2 = "unit.csv"

d1 = []
d2 = []
with open(f1,"r") as f:
    reader = csv.reader(f)
    for i in reader:
        d1.append(i)

with open(f2,"r") as f:
    reader = csv.reader(f)
    for i in reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
p1 = d1[1:]
p2 = d2[1:]
h = h1+h2
p = []
for i in p1:
    p.append(i)

for i in p2:
    p.append(i)

with open("totalstars.csv", "w", newline = "")as f:
    store = csv.writer(f)
    store.writerow(h)
    store.writerows(p)

