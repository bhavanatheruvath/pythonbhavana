print("Basic calculator")
print("----------------")
while(True):
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    o=int(input("1)Add \t 2)Sub \t 3)Mult\t 4)Div \t 5)Exit \n Select your operation: "))
    if(o==1):
        s=a+b
        print(f"{a}+{b}={s}")
    elif(o==2):
        m=a-b
        print(f"{a}-{b}={m}")
    elif(o==3):
        p=a*b
        print(f"{a}*{b}={p}")
    elif(o==4):
        d=a/b
        print(f"{a}/{b}={d}")
    else:
        break

