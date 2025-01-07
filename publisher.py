#Create a class Publisher (name). Derive class Book from Publisher with attributes title and author.Derive class Python from Book with attributes price and no_of_pages.Write a program that displays information about a Python book.Use base class constructor invocation and method overriding.
class Publisher:
    def __init__(self, name):
        self.__name=name
        
    def display(self):
        print("Name of Publisher: ", self.__name)
    
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.__title= title
        self.__author = author
        
    def display(self):
        super().display();
        print("Book Title:",self.__title)
        print("Book Author:",self.__author)
class Python(Book):
    def __init__(self,name, title, author,price, pages):
        super().__init__(name, title, author)
        self.__price=price
        self.__page=pages
    def display(self):
        super().display()
        print("Price of the book: ", self.__price)
        print("Number of pages: ", self.__page)
        
res = Python("DC Books", "Invisible Man", "Ralph Ellison", 250, 350)
res.display()   
        
