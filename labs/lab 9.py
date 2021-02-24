from random import randint
def menu():
    while(True):
        choice=input("Menu:\n-------------\npress 1 to print your dog details\npress 2 to see and edit your friends list\npress 3 to N Azzert\nEnter a number from 1-3 only: ")
        if(choice=="1"):
            Dogs(str(input("Your dog name is: ")),int(input("Your dog age is: ")))
        elif(choice=="2"):
            Friends()
        elif(choice=="3"):
            Azzert()
        else:
            print("\nEnter a number from 1-3 only!!!\n")
            continue
        exit = str(input("\nDo you want to exit the menu?" + "\nif you want to exit enter yes\y.\nif you want to return enter no/n.\nEnter: "))
        if(exit == "yes" or exit == "y"):
            print("\nThank you and bye bye")
            break
        else:
            print("\nWelcome back!\n")


def Dogs(x,y):
    print("Your dog name is: " + str(x) + " \nYour dog age in human years is: " + (str(int(y)*7)))

def Friends():
    list=[]
    for i in range(5):
        list.append(str(input("Enter a name of a friend: \n")))
    print(list)
    name=str(input("Enter a new name of a friend: "))
    if(name in list):
        print(name + "is in the list")
    else:
        print(name + "is not in the list")

def Azzert():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print(str(num) + " Azzert is: " + str(sum) + "\n")


menu()






