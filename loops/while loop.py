#while loop
'''counter=10
while(counter>0):
    print(counter*100)
    print("Elai ram")
    counter=counter-1'''
#break(exit the loop completly) + continue(return to the beginning of the loop)
'''while(True):
    name=str(input("Enter a name: "))
    if(name=="Elai"):
        print("Hello Elai")
        break
    elif(name=="ben"):
        continue
    else:

        print("Where is Elai?")
    number=int(input("Enter a number: "))
    print(number*4)

print("Bye Bye...")'''

while(True):
    print("Menu:\n-------" + "\n1.Insert number and ** it by 3" + "\n2.Insert 4 IPs to a list and ptint it" + "\n3.Insert 4 Entries to a DNS_Dictionary and print it" + "\n4.Check if a string is a polindrom")
    num1 = int(input("Enter a number from 1-4 only: "))
    if (num1 == 1):
        print("The new number is: " + "\n" + (str((int(input("Enter a number: "))) ** 3)))
    elif (num1 == 2):
        IP_list = []
        IP_list.append(input("Enter an IP: "))
        IP_list.append(input("Enter an IP: "))
        IP_list.append(input("Enter an IP: "))
        IP_list.append(input("Enter an IP: "))
        print("The new list is: " + "\n-----------\n" + str(IP_list))
    elif (num1 == 3):
        DNS_dict = {}
        DNS_dict.update({(input("Enter an URL: ")): (input("Enter an IP: "))})
        DNS_dict.update({(input("Enter an URL: ")): (input("Enter an IP: "))})
        DNS_dict.update({(input("Enter an URL: ")): (input("Enter an IP: "))})
        DNS_dict.update({(input("Enter an URL: ")): (input("Enter an IP: "))})
        print("The new DNS_dict is: " + "\n-----------\n" + str(DNS_dict))
    elif (num1 == 4):
        my_str = (input("Enter a word: "))
        if ((my_str[::-1]) == my_str):
            print("your word is a polindrom\n")
        else:
            print("your word is not a polindrom\n")
    else:
        print("Enter a number from 1-4 only...!\n")

    exit=str(input("\nDo you want to exit the menu?" + "\nif you want to exit enter yes\y. if you want to return enter no/n.\nEnter:"))
    if(exit=="yes" or exit=="y"):
        break
    else:
        print("\nWelcome back!\n")

print("Thank you and bye bye")




