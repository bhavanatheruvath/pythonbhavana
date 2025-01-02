numbers=[]
s=int(input("Enter the size of the list: "))
for i in range(s):
    n=int(input(f"{i+1} element: "))
    numbers.append(n)
print(numbers)
evennumbers=[x for x in numbers if x%2!=0]
print(evennumbers)
