#Following snippet asks for a number and prints multiplications facts for the number from 1 upto 12
number = int(input(" Let's create multiplication table. Enter a number from 2 to 10: "))
if number<2:
  print(" You entered a number less than 2. Good bye! ")
elif number>10:
  print(" You entered a number greater than 10. Good bye! ")
else:
  i=1
while (i<=12):
  #print (number*i)
  print(str(number) + " x " + str(i) + " = "+ str(number*i))
  i=i+1