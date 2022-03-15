#Create a basic class

class book:
    def __init__(self, title):
        self.title = title

#Create Instances of the class

b1 = book("Permanent Record")
b2 = book("The Journey of Hardwork")

#Print the class and property

print(b1)
print(b1.title)

print("\n")

print(b2)
print(b2.title)