def sort(number1: object, number2: object) -> object:
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1

n1,n2 = sort(10, 5)
print("n1 is: ", n1)
print("n2 is: ", n2)


