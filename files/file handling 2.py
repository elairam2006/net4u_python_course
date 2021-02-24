filename="C:/Users/oded/OneDrive/New folder/hello.txt"
'''
file = open(filename, "r")
for line in file:
    print(line)
file.close()
'''
file = open(filename, "r")
my_str=file.read()
file.close()
print(my_str)
list=my_str.split(",")
print(type(list))
print(list)