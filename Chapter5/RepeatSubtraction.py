import random
number1 = random.randint(1,100)
number2 = random.randint(1,100)
if number1>number2:
    number1, number2 = number2, number1

answer = eval(input("who much is "+ str(number1)+ "-" + str(number2)+ "? "))
while number1 - number2 != answer:
    answer = eval(input("The answer is not correct, try again, how much is "+ str(number1)+ "-" + str(number2) + "? "))
print("It's correct")
