'''
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length


'''


# Request the user to insert the radius and length of the cylinder

radius = eval(input("Please input the radius of the cylinder: "))

length = eval(input("Please input the lenght of the cylinder: "))


# Compute the are of the cylinder

area = radius * radius *3.15159

volume = area * length


# Display the colume of the cylinder
print( "the area of a cylinder with radius", radius," and length ", length, " is: ", area)

print( "the volume of a cylinder with radius", radius," and length ", length, " is: ", volume)

