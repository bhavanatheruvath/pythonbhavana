def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
    
n=int(input("Enter the number: "))
print(f"factorial of {n} is",fact(n))
