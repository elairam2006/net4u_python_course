#מצב קריאה מקובץ בלבד
'''
filename="C:/Users/oded/OneDrive/New folder/hello.txt"
file = open(filename, "r")
print(file.read())
file.close()


file = open(filename, "w")
(file.write("192.168.1.1\n192.168.1.2"))
file.close()
'''


filename="C:/Users/oded/OneDrive/New folder/hello.txt"

file = open(filename, "r+")
print(file.read())
file.write("\n192.168.1.1\n192.168.1.2")
print(file.read())
file.close()

file = open(filename, "a")
file.write("\n192.168.1.3\n192.168.1.4")
file.close()

file = open(filename, "r")
print(file.read())
file.close()

#בכתיבה מוחק וכותב מחדש אך גם ניתן לקרוא(R+)
#בכתיבה לא מוחק אלא רק מוסיף אך גם ניתן לקרוא(A+)











