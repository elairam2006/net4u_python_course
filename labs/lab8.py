'''fibo=[1,2,3,5,8,13,21]

boolean="True"
for i in range(2,len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]==(fibo[i-1]+fibo[i-2]):
       continue
    else:
        boolean="False"
        break
if boolean=="True":
    print("It is a fibo series")
else:
    print("It isn't a fibo series")
'''
while(True):
    print("welcome to the menu: " + "\n-----------\npress 1 to print 100 numbers " + "\npress 2 to check if a list of numbers is a fibo" + "\npres 3 to roll numbers 10 times and try to win 12 ")
    num = int(input("Enter a number to do one of the menu actions: "))
    if (num == 1):
        for i in range(1, 101):
            print(i)
    elif (num == 2):
        fibo = []
        for i in range(5):
            fibo.append(int(input("Enter a number to your fibo list: ")))

        print("Your fibo list is: " + str(fibo) + "\n")

        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] == (fibo[i - 1] + fibo[i - 2]):
                continue
            else:
                boolean = "False"
                break
        if boolean == "True":
            print("It is a fibo series")
        else:
            print("It isn't a fibo series")
    elif (num == 3):
        #option 1
        counter = 1
        for i in range(1, 11):
            from random import randint
            from time import sleep
            print("Getting random number...\n")
            sleep(0.5)
            num1 = (randint(1, 12))
            print("Counter " + str(counter) + " : " + " Number= " + str(num1))
            counter=counter+1
            if (num1 == 12):
                print("Wow, you got 12\nYou are winner!!!")
                break
            else:
                print("You did not get 12...")

    else:
        print("Enter a number from 1-3 only...!\n")
        continue

    exit = str(input("\nDo you want to exit the menu?" + "\nif you want to exit enter yes\y. if you want to return enter no/n.\nEnter: "))
    if (exit == "yes" or exit == "y"):
        print("\nThank you and bye bye")
        break
    else:
        print("\nWelcome back!\n")















