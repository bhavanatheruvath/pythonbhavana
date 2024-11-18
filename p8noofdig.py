print("Number of digits")
print("----------------")
n=int(input("Enter the number: "))
t=n
d=0
while(n>0):
    d=d+1
    n=n//10
print(f"Number of digits in {t} is",d)    
