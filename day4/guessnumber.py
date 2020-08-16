import random
secret = random.randrange(1, 10)
loop = True
while loop:
    guess = int(input("Please enter your guess number between 1 and 10: "))
    if(guess==secret):
        print("You got it!!")
        loop = False
    elif(guess < secret):
        print("Your guess is too low")
    else:
        print("Your guess is too high")
print("Program has ended!")