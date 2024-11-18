print("Multiplication table")
print("--------------------")
n=int(input("Enter the number: "))
t=int(input("Enter the limit: "))
for i in range(1,t+1):
    print(f"{i}*{n}=",i*n)
