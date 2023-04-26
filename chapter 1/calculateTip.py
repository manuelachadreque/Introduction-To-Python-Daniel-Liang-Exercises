'''
(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total. Here is a sample run:

'''

# Request the subtotal and the gratuity rate

subtotal, gratuityRate = eval(input("enter the subtotal amout and the gratuity rate separated by commas, eg. 20, 16 for 16%"))

tip = subtotal*gratuityRate/100

print("the tip is ", tip)