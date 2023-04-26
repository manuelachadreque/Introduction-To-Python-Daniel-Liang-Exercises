'''
(Geometry: great circle distance) The great circle distance is the distance between
two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical
latitude and longitude of two points. The great circle distance between the two
points can be computed using the following formula:

d = radius * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))


Write a program that prompts the user to enter the latitude and longitude of two
points on the earth in degrees and displays its great circle distance. The average
earth radius is 6,371.01 km. Note that you need to convert the degrees into radians
using the math.radians function since the Python trigonometric functions use
radians. The latitude and longitude degrees in the formula are for north and west.
Use negative to indicate south and east degrees.

'''


import math
# Average earth radius
RADIUS = 6371.01

#Request the user to input the latitude and longitude for the point 
x1,y1 = eval(input("Enter the first point latitude and longitude separated by a comma: "))

x1 = math.radians(x1)

y1 = math.radians(y1)

#Request the user to input the latitude and longitude for the second 

x2,y2 = eval(input("Enter the second point latitude and longitude separated by a comma: "))

x2 = math.radians(x2)
y2 = math.radians(y2)

d =RADIUS * math.acos(math.sin(x1) *math.sin(x2) + math.cos(x1)* math.cos(x2)* math.cos(y1-y2))

print("the distance between the two oints is: ", d)