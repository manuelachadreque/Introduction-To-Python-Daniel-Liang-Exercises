import math

n = eval(input("Enter the number of sides of the polygon: "))

s = eval(input("Enter the lenght of the sides: "))


area = (n * math.pow(s,2)) / (4* math.tan(math.pi/n))

print(" the are of the polygon is ", area)