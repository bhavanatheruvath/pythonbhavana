file=open("file.txt")
lines=file.readlines()
file.close()
file=open("file2.txt","w")

for i in range(len(lines)):
    if(i%2!=1):
        file.write(lines[i])        

file=open("file2.txt")
lines=file.readlines()
file.close()
for line in lines:
    print(line)
