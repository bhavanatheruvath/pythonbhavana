a,b=map(int,input("Enter 2 numbers: ").split())
for i in range(min(a,b),0,-1):
    if(a%i==0 & b%i==0):
        print(i)
        break
