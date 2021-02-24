'''fname=str(input("Enter your first name: "))
lname=str(input("Enter your last name: "))
print("Your full name: " + lname + "    " + fname)'''
a=str(input("Enter your full name: "))
b=' '.join(a[::-1])
print(b)