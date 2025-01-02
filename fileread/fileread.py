file=open("sample.txt")
lines=file.readlines()
file.close()
print("The lines in file are : ")
for line in lines:
    print(line)