'''The program may work as follows:
Step 1: Generate two single-digit integers for number1 and number2.
Step 2: If number1 < number2, swap number1 with number2.
Step 3: Prompt the student to answer, “What is number1 – number2?”
Step 4: Check the student’s answer and display whether the answer is correct.
'''

import random

number1 = random.randint(1, 100)

number2 = random.randint(1, 100)

if number1 < number2:
    number1, number2 = number2, number1

subtraction = number1 - number2
response = eval(input("what is the subtraction of " + str(number1) + " - "+str(number2) + " ? "))

if subtraction != response:
    print("Incorrect")
else:
    print("Correct")




