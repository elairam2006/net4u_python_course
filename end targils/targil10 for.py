def positive(num):
    if(num>0):
        sum = 0
        for i in range(1, num):
            sum = sum + (i ** 3)
        print("The summery is: " + str(sum))
        return sum
    else:
        print("Enter a positive number only!")


sum=positive(int(input("Enter a positive number: ")))

def sum_of_cubes(n):
  n = n-1
  total = 0
  while n > 0:
    total = total + (n * n * n)
    n = n-1
  return total
print("Sum of cubes: ",sum_of_cubes(int(input("Enter a positive number: "))))


