age = int(input("Enter your age: "))
if age > 65 and age <85:
    print ("you are a senior citizen")
elif age >= 35 and age < 65:
    print ("you are wise")
elif age < 35 and age >=12:
    print ("You are young")
elif age < 12:
    print ("should you be taking this python course?")    
else:
    print ("uncaught exception")

#exercise, when this program can get uncaught exception and how you can fix it?
