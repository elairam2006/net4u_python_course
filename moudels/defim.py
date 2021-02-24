from time import *
from random import *

def menu():
    print("Menu: \n1.Printing 1-100\n2.Random 2 cubes\n")
    choice=(int(input("Enter a number: ")))
    if choice==1:
        for i in range(1,101):
            print(i)
    elif choice==2:
        print("Cube 1 is: " + str(randint(1,6)))
        print("Cube 2 is: " + str(randint(1, 6)))
    else:
        print("Enter 1-2 only!")


def calculate(a,b):
    c=int(input("Enter a number: "))
    sum=a*b*c
    print("The sum is: " + str(sum))

def dogs_age(a):
    print("real dog age: " + str(a*7))
    return a*7