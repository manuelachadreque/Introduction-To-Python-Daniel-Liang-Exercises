Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
turtle.goto(0,50)
turtle.goto(200,0)
area=width*height
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    area=width*height
NameError: name 'width' is not defined
radios = 20
area =  radius*radius*3.14159
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    area =  radius*radius*3.14159
NameError: name 'radius' is not defined. Did you mean: 'radios'?
radius =20
area =  radius*radius*3.14159
print(area)
1256.636
width =5.5
height = 2
print("area is", width*height)
area is 11.0
miles = 100
kilometers = miles*1.609
print(kilometers)
160.9
radios = input("Enter a value: ")
Enter a value: 20
radius = input("Enter a value: ")
Enter a value: 20
radius=eval(input("enter a value: "))
enter a value: 20
area= radius*radius*3.14159
print(area)
1256.636
x =1
y = 2
temp=x
x=y
y= temp
x
2
y
1
xx=1
>>> x=1
>>> y=2
>>> x,y=y,x
>>> x
2
>>> y
1
>>> x=3
>>> y=5
>>> x,y = y,x
>>> x
5
>>> y
3
>>> number1, number2, number3= eval(input("Enter three number separated by commas: "))
Enter three number separated by commas: 2,3,5
>>> average = (nuber1+number2+number3)/3
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    average = (nuber1+number2+number3)/3
NameError: name 'nuber1' is not defined. Did you mean: 'number1'?
>>> average = (number1+number2+number3)/3
>>> print(average)
3.3333333333333335
>>> x=y=z=0
>>> x
0
>>> y
0
>>> z
0
>>> a=1
>>> b=2
>>> a,b = b,a
>>> a
2
>>> b
1
