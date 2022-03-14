'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.'''

import datetime

print("Please enter your 'Name' and 'Age'")

name = input("Name: ")
age = int(input("Age: "))

date = datetime.date.today()
year = date.strftime("%Y")
year = int(year)
age = year - age + 100

message = f"\nYour name is {name} and you will turn 100 in year {age}"

print(message)

print("\n--------------------------------------------------------------")

#Extra

'''Ask the user for another number and print out that many copies of 
the previous message.

Print out that many copies of the previous message on separate lines.'''

num = int(input("\n enter a random number: "))
i = 1

while(i <= num):
    print(message)
    i += 1

print("\n--------------------------------------------------------------")

#Extra


''''''