class Book:

    #Properties defined at the class level are shared by all instance
    BOOK_TYPE = ("Hardcover", "Paperback", "EBook")

    #Double-underscore properties are hidden from other classes
    __booklist = None

    #Create a class method
    @classmethod

    def getbooktypes(cls):
        return cls.BOOK_TYPE

    #Create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def settitle(self, newtitile):
        self.newtitile = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPE):
            raise ValueError(f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype


#Access the class attribute
print("\nBook types: ", Book.getbooktypes())  # used the class type to call the class method

#Create some book instances

b1 = Book("\nTitle 1", "Hardcover")
b2 = Book("\nTitle 2", "Paperback")

#Use the static method to access a singleton object

thisbook = Book.getbooklist()
thisbook.append(b1)
thisbook.append(b2)
print(thisbook)