print("Welcome to our cube game\n" + "A game cost 3 NIS\n")
#money
money=int(input("Enter how much money do you have: \n"))
#turns
turns=(money//3)
print("You have: " + str(turns) + " turns\n")
print("Your change is: " + str(money%3) + " NIS\n")
prize=0
from random import randint
from time import sleep
print("Getting random numbers...\n")
sleep(2)
for i in range(turns):
    print("Rolling cubes for Round number " + str(i+1) + ":\n-------------\n")
    sleep(2)
    num1 = (randint(1, 6))
    num2 = (randint(1, 6))
    print("Your 1st number is: " + str(num1) + "\nYour 2nd number is: " + str(num2) + "\n")
    if(num1==num2):
        if(num1==6):
            print("You won 100 NIS\n-------\n")
            prize=prize+1000
        else:
            prize = prize + 100
            print("You won 100 NIS\n-------\n")
    elif(num2 == 2):
        prize = prize + 40
        print("You won 40 NIS\n--------\n")
    elif(num1 == 1):
        prize = prize + 20
        print("You won 20 NIS\n-------\n")
    else:
        prize=prize+0
        print("You won 0$\n--------\n")
print("calculating your prize...\n")
sleep(2)
print("Your prize is: " + str(prize) + " NIS")

