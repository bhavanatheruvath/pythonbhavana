#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to 
find sum of 2 time.
class Time:
    def __init__(self,hours=0,mins=0,secs=0):
        self.hours=hours
        self.mins=mins
        self.secs=secs
    def __add__(self,time2):
        secs=(self.secs+time2.secs)%60
        mins=(self.secs+time2.secs)//60+(self.mins+time2.mins)%60
        hours=(self.mins+time2.mins)//60+(self.hours+time2.hours)%60
        time3=Time(hours,mins,secs)    
        return time3
    def getTime(self):
        print(str(self.hours)+":"+str(self.mins)+":"+str(self.secs))

h1,m1,s1=map(int,input("Enter the hours,minutes,seconds of time 1: ").split())
h2,m2,s2=map(int,input("Enter the hours,minutes,seconds of time 2: ").split())  

t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
t3=t1+t2
t1.getTime()
t2.getTime()
t3.getTime()