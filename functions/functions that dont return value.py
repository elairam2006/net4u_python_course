#פונקציה שלא מקבלת או מחזירה ערך
def calculate():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    print("Your new number is: " + str(num1*num2))

calculate()
##################################
#פונקציה שמקבלת ערך אבל לא מחזירה ערך
def calculate2(x,y):
    print("Your first number is: " + str(x) + " \nYour second number is: " + str(y))
    print("\nYour new number is: " + str(x*y))

calculate2(int(input("Enter a number: ")),int(input("Enter a number: ")))
