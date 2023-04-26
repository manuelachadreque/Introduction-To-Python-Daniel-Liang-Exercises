data = eval(input("Enter an integer, enter 0 to quit: "))

sum = 0

while(data != 0):
    sum += data
    data = eval(input("Enter an integer, enter 0 to quit: "))

print("The sum is ", sum)
