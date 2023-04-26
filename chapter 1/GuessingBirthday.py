'''
This program finds out the birthday of the user



'''

#Define and innitiate the birthday to be determined

day = 0


question1 = "It's yor birthday in Set 1? \n" +\
    "1 3 5 7\n" +\
    "9 11 13 15\n" +\
    "17 19 21 23\n" +\
    "25 27 29 31" +\
    "\nEnter 0 for No and1 for Yes: "

answer=eval(input(question1))

if answer == 1:
    day +=1

question2 = "It's yor birthday in Set 2? \n" +\
    "2 3 6 7\n" +\
    "10 11 14 15\n" +\
    "18 19 22 23\n" +\
    "26 27 30 31" +\
    "\nEnter 0 for No and1 for Yes: "

answer=eval(input(question2))

if answer == 1:
    day +=2

question3 = "It's yor birthday in Set 2? \n" +\
    "4 5 6 7\n" +\
    "12 13 14 15\n" +\
    "20 21 22 23\n" +\
    "28 29 30 31" +\
    "\nEnter 0 for No and1 for Yes: "

answer=eval(input(question3))

if answer == 1:
    day +=4


question4 = "It's yor birthday in Set 2? \n" +\
    "8 9 10 11\n" +\
    "12 13 14 15\n" +\
    "24 25 26 27\n" +\
    "28 29 30 31" +\
    "\nEnter 0 for No and1 for Yes: "

answer=eval(input(question4))

if answer == 1:
    day +=8

question4 = "It's yor birthday in Set 2? \n" +\
    "16 17 18 19\n" +\
    "20 21 22 23\n" +\
    "24 25 26 27\n" +\
    "28 29 30 31" +\
    "\nEnter 0 for No and1 for Yes: "

answer=eval(input(question4))

if answer == 1:
    day +=16

print("\nYour birthday is "+str(day)+"!")