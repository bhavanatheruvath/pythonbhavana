import csv

file=open("sample.csv")
rows=file.readlines()
i=int(input("Enter the colum index to be displayed: "))
for row in rows:
    column=row.split(",")
    print(column[i])