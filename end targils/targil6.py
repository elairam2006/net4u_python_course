def personal_details():
    name, age =(str(input("Enter your name: "))),(int(input("Enter your age: ")))
    address =(str(input("Enter your address: ")))
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()