import random
secret = random.randrange(1, 10)
while True:
    guess = int(input("Please enter your guess number between 1 and 10: "))
    if(guess==secret):
        print("You got it!!")
        break
    elif(guess < secret):
        print("Your guess is too low")
    else:
        print("Your guess is too high")
print("Program has ended!")