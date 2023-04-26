'''
1. Prompts the user to enter two points.
2. Computes the distance between the points.
3. Uses Turtle graphics to display the line that connects the two points.
4. Displays the length of the line at the center of the line.

'''
 
 
import turtle


# Enter the first point with two float values
x1,y1 = eval( input("enter the first two point values separated by commas: "))

# Enter the second point with two float values
x2,y2 = eval( input("Enter the second the two point coordinated separated by comma: "))

# Calculate the distance between the two points

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
distance1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


turtle.penup()
turtle.goto(x1,y1) #Move to (x1,y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2,y2)
turtle.write("Point 2")

#Move to the center point of the line

turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distance)

turtle.done()

