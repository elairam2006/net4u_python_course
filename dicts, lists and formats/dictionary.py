my_dict={"www.google.com": "8.8.8.8", "www.facebook.com": "7.7.7.7", "www.youtube.com": ["5.5.5.5","6.6.6.6"]}
print(my_dict)
my_dict2={"www.net4uc.com":"33.33.33.33"}
print(my_dict2)
my_dict.update(my_dict2)
print(my_dict)
my_dict.update({"website":"33.44.55.66."})
print(my_dict)
print("Number of Entries: " + str(len(my_dict)))
print(my_dict["www.google.com" ])
print(my_dict.values())
my_dict["www.google.com"]="8.8.8.4"
print(my_dict["www.google.com" ])
print("www.google.com" in my_dict)
print("8.8.8.4" in my_dict.values())
