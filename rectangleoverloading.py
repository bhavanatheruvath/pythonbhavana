#Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to 
compare the area of 2 rectangles.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def __gt__(self,rect2):
        return self.area()>rect2.area()

length=int(input("Enter the length of 1st rectangle: "))
breadth=int(input("Enter the breath of 1st rectangle: "))
rec1=Rectangle(length,breadth)
length=int(input("Enter the breadth of 2nd rectangle: "))
breadth=int(input("Enter the breath of 2nd rectangle: "))
rec2=Rectangle(length,breadth)   

print("Area of 1st rectangle : ",rec1.area())
print("Perimeter of 1st rectangle : ",rec1.perimeter())

print("Area of 2nd rectangle : ",rec2.area())
print("Perimeter of 2nd rectangle : ",rec2.perimeter())

if rec1>rec2:
    print("First rectangle is larger")
else:
    print("Second rectangle is larger")    

