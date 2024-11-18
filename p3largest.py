print("Greatest of 3 numbers")
print("---------------------")
a,b,c=[int(num) for num in input("Enter 3 numbers: ").split()]
if(a>b and a>c):
    print(f"{a} is greatest")
elif(b>a and b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
