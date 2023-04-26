'''
get the radius from the ser

compute the area

display the area

'''

radius = eval(input("enter the radius: "))
if radius>0:
    area= radius * radius *3.14159
    print( "the are of a circle of radius " , radius , "is ",area)
else:
    print("Invalid Radius")

