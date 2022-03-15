class Book:
    def __init__(self, title, authors, pages, price):
        self.title = title
        #add properties
        self.authors = authors
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    #Create Instance Methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount  # the underscore here describes that this instance has a local scope

b1 = Book("The Secret", "Rhonda Bryne", 198, 32.99 )
b2 = Book("Emotional Intelligence", "Danial Golemen", 352, 43.26)

#Print the price of the book
print("\n Price of book 1: " + str(b1.getprice()))

#Setting the discount
print("\n Price of Book 2 before the discount: " + str(b2.getprice()))

b2.setdiscount(0.25)

print("\n Price of Book 2 after the discount: " + str(b2.getprice()))

#Properties with double underscores are hidden by the interpreter a.k.a name mangling

print("\n")

#print(b2.__secret) #it prevents the same name to be used a.k.a name manglingn and has a special way to be accessed by

print(b2._Book__secret) # <= the special way

