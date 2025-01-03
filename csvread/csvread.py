import csv

file=open("sample.csv")
rows=csv.reader(file)  #csv.reader gives csv file o/p as lists
for row in rows:
    print(row)
