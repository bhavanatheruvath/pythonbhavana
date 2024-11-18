import math
print("Quadratic equation")
print("------------------")
a=int(input("Enter the first coefficient: "))
b=int(input("Enter the second coefficient: "))
c=int(input("Enter the third coefficinet: "))
di=(b**2)-(4*a*c)
d=math.sqrt(di)
if(di==0):
    print("Equation has only one root")
    print("root is ",-b/(2*a))
elif(di>0):
    print("Equation has 2 distint roots")
    print("roots are",(-b+d)/(2*a),"and",(-b-d)/(2*a))
else:
    print("No roots")
