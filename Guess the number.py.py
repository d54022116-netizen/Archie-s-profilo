import random

secret_number = random.randint(1, 100)
guess = ""
while guess !=secret_number:
    guess = int(input ("Guess a number from 1 to 100: "))

    if guess == secret_number:
        print ("You win")
    elif guess > secret_number:
        print("Too high")
    else:
        print("too low")