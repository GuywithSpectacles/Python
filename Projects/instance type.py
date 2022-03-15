"""Checking Class types and instances"""

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

#Creating some instances of the class

b1 = Book("Machine Learning")
b2 = Book("Data Science")
n1 = Newspaper("Dawn")
n2 = Newspaper("The News")

#Use type() to inspect the object type

print(type(b1))
print(type(n1))

#Compare two types together

print("\n")

print(type(b1) == type(b2))
print(type(b2) == type(n2))

#Use isinstance to compare a specific instance to a known type

print("\n")

print(isinstance(b1,Book))

print(isinstance(n1,Newspaper))

print(isinstance(n2,Book))

print(isinstance(b2, object))