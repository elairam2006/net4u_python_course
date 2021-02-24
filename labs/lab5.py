my_dict={"elai":10,"ram":15,"oded":20,"celine":25,"rafael":30}
print(my_dict)
summery=my_dict["elai"] + my_dict["rafael"]
print("The summery is: " + str(summery))
my_dict.update({"avi":summery})
print(my_dict)
print("The number of entries: " + str(len(my_dict)))
print("elai" in my_dict)

