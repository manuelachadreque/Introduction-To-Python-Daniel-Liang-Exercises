'''
(Convert pounds into kilograms) Write a program that converts pounds into
kilograms. The program prompts the user to enter a value in pounds, converts it to
kilograms, and displays the result. One pound is 0.454 kilograms. Here is a
sample run:
'''

# Request user to insert the pounds

pounds = eval( input( "Enter the pounds: "))

kilograms = 0.454*pounds

print(pounds," pounds correspond to ",kilograms," kilograms")