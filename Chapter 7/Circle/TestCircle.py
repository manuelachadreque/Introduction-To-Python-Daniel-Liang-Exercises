from Circle import  Circle

def main():
    #create circle with radius 1
    circle1 = Circle()
    print("The are of the circle with radius: ", circle1.radius, "is ", circle1.getArea())

    circle2 = Circle(25)
    print("The are of the circle with radius: ", circle2.radius, "is ", circle2.getArea())

    circle3 = Circle(125)
    print("The are of the circle with radius: ", circle3.radius, "is ", circle3.getArea())

    #Modify Circle2 radius
    circle2 = Circle(100)
    print("The are of the circle with radius: ", circle2.radius, "is ", circle2.getArea())

main()