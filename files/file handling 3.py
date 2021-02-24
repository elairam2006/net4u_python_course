
list=[]
filename="C:/Users/oded/OneDrive/New folder/hello.txt"

file = open(filename, "r")
for line in file:
    print(line)
    list.append(line)
file.close()
print("\n" + str(list))

filename="C:/Users/oded/OneDrive/New folder/hello.txt"
file = open(filename, "r")
new_list=[]
new_list=file.read().splitlines()
print("\n"+ str(type(new_list)))
print("\n" + str(new_list))
file.close()
for i in new_list:
    print(i)


