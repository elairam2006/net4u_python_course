'''if("idan"=="idan"):
    print("correct")
else:
    print("incorrect")

name=input("Enter your name: ")
if(name=="elai"):
    print("Hello elai\n")
    age=int(input("Enter your age: "))
    if(age==14):
        print("wow, you are 14 years old")
    else:
        print("you are too young")
else:
    print("where is elai")

#signs that are used in if:

 if(age==14): Equal
 if(age<14): smaller
 if(age>14): bigger
 if(age!=14): unequal
 if(age>=14):bigger or  Equal
 if(age<=14): smaller or unequal
  
'''

name=input("Enter your name: ")
age=int(input("Enter your age: "))
if((name=="elai" or "Elai" or "ELAI") and (age>=18)):
    print("enter")
else:
    print("go")

if((((5+3)<=10) and ("man" in "mana")) or ((100!=3) and 90<=91)):
    print("true")
else:
    print("false")