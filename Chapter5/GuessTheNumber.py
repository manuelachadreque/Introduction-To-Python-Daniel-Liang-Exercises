import random

number = random.randint(1, 100)

guess = eval(input("Guess the magic number: "))

while guess != number:
    if guess > number:
        guess = eval(input("Your guess number is higher, guess the magic number: "))
    else:
        guess = eval(input("Your guess number is lower, guess the agic number: "))
print("Your number is correct")