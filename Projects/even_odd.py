'''
Ask the user for a number. Depending on whether the number is even
or odd, print out an appropriate message to the user.

If the number is a multiple of 4, print out a different message.
'''

num = int(input("Enter a number please: "))

if(num % 2 == 0):
    print("\nThe number is even.")

    if (num % 4 == 0):
        print("\n and a multiple of 4 as well")

else:
    print("\nThe number is odd")

print("\n----------------------------------------")

#Extra

'''
Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly into num, 
tell that to the user. If not, print a different appropriate message.
'''

print("Enter two numbers Please!")

numm = int(input("\nFirst Number: "))
check = int(input("\nSecond Number: "))

if(numm % check == 0):
    print("\nFirst number is even with respect to second number")

else:
    print("\nThey didn't divide evenly amid each other.")