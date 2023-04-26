'''

Suppose you
want to develop a program that classifies a given amount of money into smaller monetary
units. The program lets the user enter an amount as a floating-point value representing a total
in dollars and cents, and then outputs a report listing the monetary equivalent in dollars, quarters,
dimes, nickels, and pennies, as shown in the sample run.
Your program should report the maximum number of dollars, then the number of quarters,
dimes, nickels, and pennies, in this order, to result in the minimum number of coins.

'''

moneyAmout = eval(input("Enter a monetary amount: "))

#Convert the amout into cents

remainingAmount = int(moneyAmout*100)


dolars = remainingAmount //100
remainingAmount = remainingAmount % 100

quarters = remainingAmount //25

remainingAmount = remainingAmount % 25

dimes = remainingAmount//10

remainingAmount = remainingAmount % 25

nickels = remainingAmount // 5

remainingAmount = remainingAmount % 5

pennies = remainingAmount


# Display he result

print("Your amount", moneyAmout,  "Consist of \n",
"\t", dolars, "dollars\n",
"\t", quarters, "quarters\n",
"\t", dimes, "dimes\n",
"\t", nickels, "nickels\n",
"\t", pennies, "pennies\n")



s= "Welcome"
s1= s.lower()
s2 =s.upper()

print(1)
print(2)
