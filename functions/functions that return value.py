#פונקציות שנותנות ערך אבל לא מקבלות ערך
def calculate():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum = (num1 * num2)
    print("Your new number is: " + str(sum))
    return sum


a = calculate()+2**3
print("Wow:" + str(a))


#פונקציות שנותנות ערך ומקבלות ערך
def calculate2(x,y):
    print("Your first number is: " + str(x) + " \nYour second number is: " + str(y))
    sum=x*y
    print("\nYour new number is: " + str(sum))
    return sum

elai=calculate2(int(input("Enter a number: ")),int(input("Enter a number: "))) + 29
print("Wow: " + str(elai))


