num=int(input("Enter a number with 5 digits: "))

print("\nAhad=" + str(num//10000) + "\nAlafim=" + str(num//1000) + "\nMeot=" + str((num%1000)//100) + "\nAsarot=" + str((num%100)//10) + "\nAhadot=" + str((num%10)) )
