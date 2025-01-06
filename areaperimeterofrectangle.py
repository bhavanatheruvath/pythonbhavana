#Create Rectangle class with attributes length and breadth and methods to find area and 
perimeter. Compare two Rectangle objects by their area.
class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        area=self.l*self.b
        return area
    def perimeter(self):
        perimeter=2*(self.l+self.b)
        return perimeter

l,b=map(int,input("Enter the length and breadth of rectangle 1: ").split())
r1=rectangle(l,b)
l,b=map(int,input("Enter the length and breadth of rectangle 2: ").split())
r2=rectangle(l,b)
print("Area of rectangle 1 : ",r1.area())
print("Area of rectangle 2 : ",r2.area())
a1=r1.area()
a2=r2.area()
if a1>a2:
        print("Rectangle 1 has largest area")
else:
    print("Rectangle 2 has largest area")
