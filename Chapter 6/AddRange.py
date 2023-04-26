sum = 0
for i in range(1, 11):
    sum += i
print("The sum from 1 to 10 is ", sum)


sum = 0
for i in range(20, 38):
    sum += i
print("The sum from 20 to 37 is ", sum)


def SumRange(i1, i2):
    result = 0
    for i in range(i1, i2+1):
        result += i
    return result

def main():
    print("The sum from ", 1, " to ", 10 , " is ", SumRange(1, 10))
    print("The sum from ", 20, " to ", 37 , " is ", SumRange(20, 37))

main()