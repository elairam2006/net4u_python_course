a=(str(input("Enter your name: ")))
b=(str(input("Enter your mail: ")))
c=(int(input("Enter your age: ")))
print("name: " + a + "\nMail : " + b + "\nAge: " +str(c))
s1=a
print("name: " + s1[::-1] + "\nAge: " + str(c*3))
print(a in (s1[::-1] + str(c*3)))
print(a in "elay ben shimi ram")
print(a in "elai ben shimi ram")


