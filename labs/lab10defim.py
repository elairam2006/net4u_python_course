def main_menu():
    while(True):
        print("Menu: \n-------------\nPress 1 to enter the ip system.\nPress 2 to enter the DNS system.\n")
        choice=int(input("Enter a number: "))
        if choice == 1:
            ip_menu()
        elif choice == 2:
            DNS_menu()
        else:
            print("\nEnter a number from 1-2 only!!!\n")
            continue
        exit = str(input("\nDo you want to exit the main menu?" + "\nif you want to exit enter yes\y. if you want to return enter no/n.\nEnter:"))
        if (exit == "yes" or exit == "y"):
            break
        else:
            print("\nWelcome back!\n")

    print("Thank you and bye bye")

def ip_menu():
    while(True):
        print("IP Menu: \n------------\nPress 1 to search for ip address from a list.\nPress 2 to add ip address to a list.\nPress 3 to delete ip address from a list.\nPress 4 to print all the ip addresses to the screen\n")
        choice = int(input("Enter a number: "))
        if choice == 1:
            ip_search()
        elif (choice == 2):
            ip_add()
        elif (choice == 3):
            ip_delete()
        elif choice == 4:
            ip_print()
        else:
            print("Enter 1-4 only!!!\n")
            continue
        exit = str(input("\nDo you want to exit the ip menu?" + "\nif you want to exit enter yes\y. if you want to return enter no/n.\nEnter:"))
        if (exit == "yes" or exit == "y"):
            break
        else:
            print("\nWelcome back!\n")
    print("Thank you and bye bye...")

def ip_search():
    filename = "C:/Users/oded/OneDrive/New folder/hello2.txt"
    file = open(filename, "r")
    my_str = file.read()
    file.close()
    list=my_str.splitlines()
    print(list)
    a = input("Enter an ip address to search it in the list: ")
    if(a in list):
        print(str(a) + " is in the file")
    else:
        print(str(a) + " is not in the file")

def ip_add():
    filename = "C:/Users/oded/OneDrive/New folder/hello2.txt"
    file = open(filename, "a")
    file.write("\n" + str(input("Enter an ip address to add it to the list: ")))
    file = open(filename, "r")
    my_str = file.read()
    list = my_str.splitlines()
    print("The new list is: " + str(list))
    new_str = list
    file = open(filename, "w")
    file.write(str(new_str))
    file.close()

def ip_delete():
    filename = "C:/Users/oded/OneDrive/New folder/hello2.txt"
    file = open(filename, "r")
    my_str = file.read()
    list = my_str.splitlines()
    print(list)
    d=int(input("Enter a cell you want to delete: "))
    list.pop(d-1)
    print("The new list is: " + str(list))
    new_str=list
    file = open(filename, "w")
    file.write(str(new_str))
    file.close()

def ip_print():
    filename = "C:/Users/oded/OneDrive/New folder/hello2.txt"
    file = open(filename, "r")
    print(file.read())
    file.close()

def DNS_menu():
    while(True):
        print("DNS Menu: \n------------\nPress 1 to search for URL from a dictionary.\nPress 2 to add URL + ip address to a dictionary.\nPress 3 to delete URL from a dictionary.\nPress 4 to update the ip address of a specific URL.\nPress 5 to print all the URL : ip addresses to the screen")
        my_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "7.7.7.7",
                   "www.youtube.com": ["5.5.5.5", "6.6.6.6"]}
        choice = int(input("Enter a number: "))
        if choice == 1:
            dict_search()
        elif (choice == 2):
            dict_add()
        elif (choice == 3):
            dict_delete()
        elif choice == 4:
            dict_update()
        elif (choice == 5):
            dict_print()
        else:
            print("Enter 1-5 only!!!\n")
            continue
        exit = str(input("\nDo you want to exit the ip menu?" + "\nif you want to exit enter yes\y. if you want to return enter no/n.\nEnter:"))
        if (exit == "yes" or exit == "y"):
            break
        else:
            print("\nWelcome back!\n")

    print("Thank you and bye bye...")

def dict_search():
    print("a")
def dict_add():
    print("b")
def dict_delete():
    print("c")
def dict_update():
    print("d")
def dict_print():
    print("e")

