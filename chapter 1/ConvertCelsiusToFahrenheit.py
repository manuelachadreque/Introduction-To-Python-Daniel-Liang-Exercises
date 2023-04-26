'''

(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from
the console and converts it to Fahrenheit and displays the result. The formula for
the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32
Here is a sample run of the program:

'''


# Request the user to input the temperature in celsius degree 

celsius = eval(input("Enter the temperature in celsius degree, e.g. 37: "))

# Calculate the temperature in fahrenheit given by (9 / 5) * celsius + 32


fahrenheit = (9/5)* celsius +32

# Display the temperature in Fahrenheit degree

print( celsius ,"celcius is equivalento to ", fahrenheit, "fahrenheit degree" )
