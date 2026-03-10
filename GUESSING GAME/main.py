# guessing game

import random

a = random.randint(1,100)

guess = int(input("Guess a number"))
counter = 1

while guess != a:
    if guess > a:
        print("Guess lower")
    else:
        print("Guess higher")
    guess = int(input())
    counter += 1

print("yes the answer is right!")
print("You total attempted is", counter)


