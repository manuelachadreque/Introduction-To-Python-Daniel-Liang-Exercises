'''The program in Listing 4.8 checks whether a number is divisible by 2 and 3, by 2 or 3, and
by 2 or 3 but not both.
'''

number = eval(input("Enter a number: "))

if number % 2 == 0 and number % 3 ==0:
    print("the number is divisible by 2 and 3")
if number % 2 ==0 or number % 3 == 0:
    print("The number is divisible by 2 or 3")
if (number % 2 == 0 or number % 3 == 0) and not (number % 2== 0 and number % 3 ==0) :
    print("The nuber is divisible by 2 or 3 but not both")


