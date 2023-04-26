def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result

def main():
    i = 5
    j = 5

    k = max(i,j)
    print("The larger number is ", k)

main()