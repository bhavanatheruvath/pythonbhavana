
print("Leap year or not")
print("----------------")
n=int(input("Enter the year: "))
if(n%100==0):
    if(n%400==0):
        print(f"{n} is a leap year")
elif(n%4==0):
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")
        
