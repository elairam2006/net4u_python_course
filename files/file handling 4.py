filename="C:/Users/oded/OneDrive/New folder/hello.txt"

file = open(filename, "r")
print(file.read(3))

file.close()

file = open(filename, "r")
print(file.readlines()[0])

file.close()
