import random

number1 = random.randint(0,100)

number2 = random.randint(0,100)



soma =eval(input("what is "+ str(number1)+ " + "+ str(number2) +"?"))



if soma == number1+number2:
    print("It is right")
else:
    print("It is wrong")

