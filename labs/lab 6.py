print("Menu:\n-------" + "\n1.Insert number and ** it by 3" + "\n2.Insert 4 IPs to a list and ptint it" + "\n3.Insert 4 Entries to a DNS_Dictionary and print it" + "\n4.Check if a string is a polindrom")
num1=int(input("Enter a number from 1-4 only: "))
if(num1==1):
    print("The new number is: " + "\n" + (str((int(input("Enter a number: ")))**3)))
elif(num1==2):
    IP_list=[]
    IP_list.append(input("Enter an IP: "))
    IP_list.append(input("Enter an IP: "))
    IP_list.append(input("Enter an IP: "))
    IP_list.append(input("Enter an IP: "))
    print("The new list is: " + "\n-----------\n" + str(IP_list))
elif(num1==3):
    DNS_dict={}
    DNS_dict.update({(input("Enter an URL: ")):(input("Enter an IP: "))})
    DNS_dict.update({(input("Enter an URL: ")):(input("Enter an IP: "))})
    DNS_dict.update({(input("Enter an URL: ")):(input("Enter an IP: "))})
    DNS_dict.update({(input("Enter an URL: ")): (input("Enter an IP: "))})
    print("The new DNS_dict is: " + "\n-----------\n" + str(DNS_dict))
elif (num1==4):
    my_str=(input("Enter a word: "))
    if((my_str[::-1]) == my_str):
        print("your word is a polindrom")
    else:
        print("your word is not a polindrom")

else:
    print("Enter a number from 1-4 only!")
print("Thanks for using the menu, bye bye")
