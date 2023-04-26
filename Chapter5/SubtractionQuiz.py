import random
import time

NumberRepetitions = eval(input("How many times should repeat? "))
count = 0
currentCount = 0
startTime = time.time()
while count < NumberRepetitions:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    if number1 < number2:
        number1, number2 = number2, number1
    answer = eval(input("how much is "+str(number1) +" - " +str(number2)+"? "))
    if number1 - number2 == answer:
        print("Your answer is correct")
        currentCount += 1
    else:
        print("Your answer is incorrect, " + str(number1) + " - " + str(number2) + " is equal to" + str(number1 - number2))
    count += 1

endTime = time.time()

testTime = int(endTime - startTime)
print("Current count is ", currentCount, " out of ", NumberRepetitions, "The test time is", testTime, " seconds.")

