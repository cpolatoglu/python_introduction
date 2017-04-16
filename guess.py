import random

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "Please guess a number between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    guess = int(input())

    if guess == magicNumber:
        print("Correct!")
        found = True
    elif guess < magicNumber:
        print("Wrong! Guess a higher number.")
    else:
        print("Wrong! Guess a lower number.")
