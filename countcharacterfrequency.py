str=input("Enter the string: ")
ltr=set(str)
for i in ltr:
    count=0
    for j in str:
        if i==j:
            count+=1
    print(f"count of {i} in {str} is",count)        
