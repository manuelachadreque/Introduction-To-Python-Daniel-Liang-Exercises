
'''
The program prompts the user to enter the coordinates of the first point  and the
second point 
It then computes the distance between them (line 8) and displays it.
'''
# Enter the first point with two float values
x1,y1 = eval( input("enter the first two point values separated by commas: "))

# Enter the second point with two float values
x2,y2 = eval( input("Enter the second the two point coordinated separated by comma: "))

# Calculate the distance between the two points

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
distance1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

# Display the distance

print("The distance between the poit (", x1,",",y1 ,") and (",x2,",",y2,") is", distance)

