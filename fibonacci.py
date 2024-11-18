a=0
b=1
c=0
n=int(input("Enter the number of terms: "))
for i in range(n):
    print(a,end="\t")
    c=a+b
    a=b
    b=c
