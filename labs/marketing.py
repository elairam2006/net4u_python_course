print("Now we will calculate your marketing:\n\nPrices:\nTomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS ")
tomatos=int(input("Enter how many tomatos?"))
cucumbers=int(input("Enter how many cucumbers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))


print("\nSummery of your order:\ntomatos: " + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

summery=((tomatos*3) + (cucumbers*2) + (colas*5) + (chickens*20))

print("You have to pay: " + str(summery) + " NIS without tax")
print("You have to pay: " + str("%.2f" %(summery*1.17)) + " NIS with tax")





