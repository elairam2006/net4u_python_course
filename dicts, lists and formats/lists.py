new_list=[1,2,3,[]]
print(type(new_list))
print(new_list)
print(new_list*3)
new_list2=new_list+[77,"elai"]
print(new_list2)
new_list3=new_list+new_list2
print(new_list3)
new_list4=[1,2,3,44]
print(new_list4[0])
print(new_list4[3])
print(new_list4[0]*3)
my_list=[1,6.6,14,"elai"]
print("My Age: " + str(my_list[2]))
print("My Name: " + my_list[3])
print("My float: " + str(my_list[1]))
my_list2=my_list*2
print(my_list2)
my_list3=list("123456789")
print(my_list3)
my_string=''.join(my_list3)
print(my_string)
my_string2='A'.join(my_list3)
print(my_string2)
my_list4=my_string.split()
print(my_list4)
my_string3="hello elai how are you?"
my_list4=my_string3.split()
print(my_list4)
my_string4="hello elai \nhow are you?"
my_list5=my_string4.splitlines()
print(my_list5)
#my_list=[1,6.6,14,"elai"]
print(len(my_list))
print("My lengh is: " + str(len(my_list)))
'''my_list3=list("123456789")
my_string=''.join(my_list3)
'''
print("My lengh is: " + str(len(my_string)))
#my_list=[1,6.6,14,"elai"]
(my_list.append("wow"))
(my_list.append("elai"))
print("The new lengh is: " + str(len(my_list)))
my_list.insert(5,"ram")
print(my_list)
my_list.pop(5)
print(my_list)
my_list.pop()
print(my_list)
my_list6=["a","b","c","v","n"]
print("e" in my_list6)
print("a" in my_list6)
