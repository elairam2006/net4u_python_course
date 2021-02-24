a=(str(input("Enter your name: ")))
b=(str(input("Enter your mail: ")))
c=(int(input("Enter your age: ")))
d=(str(input("Enter your phone: ")))
my_list=[a,b,c,d]
print(my_list)
print("Full name: " + my_list[0] + "\nMail: " + my_list[1] + "\nAge: " + str(my_list[2]) + "\nPhone: " + my_list[3])
new_list=["1.1.1.1","2.2.2.2"]
print(new_list)
(new_list.append("3.3.3.3"))
(new_list.append("4.4.4.4"))
(new_list.append("5.5.5.5"))
print(new_list)
new_list.pop(2)
print("New list lengh is: " + str(len(new_list)) + "\nAnd the new list: " + str(new_list))



