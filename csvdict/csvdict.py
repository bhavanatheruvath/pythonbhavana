

datadict=[
    {"Rollno":"3","Name":"Babu","Place":"Malappuram"},
    {"Rollno":"5","Name":"Rana","Place":"Kannur"},
    {"Rollno":"8","Name":"Chaii","Place":"Thrissur"},
    {"Rollno":"3","Name":"Aishu","Place":"Palakkad"}
]
#writing key data into csv
titles=list(datadict[0].keys)
file=open("result.csv","w")
header=",".join(titles)
file.write(header+"\n")
#writing value data into csv 
for data in datadict:
    row=",".join(str(data[title]) for title in titles)
    file.write(row+"\n")
file.close() 
#printing csv data
print("File data : ")
file=open("result.csv","r")
rows=file.readlines()
for row in rows:
    data=row.strip().split(",")
    print(", ".join(data))
