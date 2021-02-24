##for loops
'''for x in range(3):
    print(x)
    print("wow\n")
print("\n------\n")
for y in range(1,5,2):
    print(y)
    print("wow\n")

list=["apple","banana","mango"]
for x in list:
    print(x)
'''
from time import sleep

print("Now we will get all of your students details:\n------------\n")
for i in range(2):
    name=(str(input("Enter your name: ")))
    age=(int(input("Enter your age: ")))
    phone=(int(input("Enter your phone: ")))
    print("Printing student number " + str(i+1) + " Details...\n" )
    sleep(3)
    print("Full name: " + name + "\nAge: " + str(age) +"\nPhone: " + str(phone) + "\n-----------\n")

print("\nBye Bye")