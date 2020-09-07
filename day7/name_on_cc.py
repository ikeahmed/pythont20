def fullName(fName, mName, lName):
  if ( len(mName) == 0):
    return (fName + " " + mName + " " + lName).upper()
  else:
    return (fName +  " " + lName).upper()

#write a function  that takes three parameters  first name, middle name, last name and  prints name on credit card in all upper case. 
# the credit card name 
#can only be 15 characters long due to print space limitation on the physical card.

returned = fullName('Ikhlas', 'M','Ahmed')
expected = 'IKHLAS M AHMED'
print ('Expected: ' + expected)
print ('Returned: ' + returned )
assert ( expected == returned)
assert (len(returned) <= 15)

returned = fullName('Ikhlas', '','Ahmed')
expected = 'IKHLAS AHMED'
print ('Expected: ' + expected)
print ('Returned: ' + returned )
assert ( expected == returned)
assert (len(returned) <= 15)


#Ikhlas M Ahmed => IKHLAS M AHMED  
#Zad Ali Ahmed   => ZAD ALI AHMED
#Shahadat Khan => SHAHADAT KHAN  
#Syed Huzaifa Nabeel => SYED H NABEEL
#Zakariah Saifullah => Z SAIFULLAH
#Muhammad Nasir Mohideen => M MOHIDEEN