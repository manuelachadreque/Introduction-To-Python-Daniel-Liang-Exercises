import random

number1 = random.randint(0,127)

character1 = chr(number1)

print(number1,"-"+ character1)

#Lower case
number = random.randint(ord('a'),ord('z'))
character2 = chr(number)
print(number,"-"+ character2)