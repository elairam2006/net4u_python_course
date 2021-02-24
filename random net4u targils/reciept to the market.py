a=str(input("Enter a  full name: "))
b=int(input("Enter an age: "))
c=str(input("Enter mail: "))

print("Full name: " + a + "\nAge: " + str("%.1f" %(b))+ "\nMail: " + c)


print("Now we will calculate your marketing:\n\nPrices:\ntomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS ")
tomatos=int(input("Enter how many tomatos?"))
cucumbers=int(input("Enter how many cucumbers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))


print("\nSummery of your order:\ntomatos: " + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

summery=((tomatos*3) + (cucumbers*2) + (colas*5) + (chickens*20))

num=(summery)

print("\nAhad=" + str(num//10000) + "\nAlafim=" + str(num//1000) + "\nMeot=" + str((num%1000)//100) + "\nAsarot=" + str((num%100)//10) + "\nAhadot=" + str((num%10)) )


print("You have to pay: " + str("%.1f" %(summery*1.17)) + " NIS with tax")



print("\n\nReceipt" + "\nFull name: " + a + "\nAge: " + str("%.1f" %(b)) + "\nMail: " + c + "\nYou have to pay: " + str("%.1f" %(summery*1.17/1.17)) + " NIS minos tax discount")



print("You have to pay: " + str("%.1f" %(summery*1.45)) + " NIS with mas")












