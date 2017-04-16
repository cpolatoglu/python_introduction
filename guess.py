import random

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "Please guess a number between {0} and {1}"
print(message.format(minNumber, maxNumber))

guess = int(input())

if guess == magicNumber:
    print("Correct!")
else:
    print("Wrong! The magic number is: ", magicNumber)
