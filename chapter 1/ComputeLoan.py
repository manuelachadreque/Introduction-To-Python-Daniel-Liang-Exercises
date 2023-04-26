'''

The program must satisfy the following requirements:
■ It must let the user enter the interest rate, the loan amount, and the number of years
for which payments will be made.
■ It must compute and display the monthly payment and total payment amounts.

'''



# Enter annual interest rate as percentage 

annualInterestRate = eval(input("Enter annual interest rate, e.g., 7.5: "))

# Enter loan ammount  

loanAmount = eval(input("Enter the loan amount, e.g., 100000: "))


# Enter loan ammount  

numberOfYears = eval(input("Enter the number of years, e.g., 5: "))



#Convert the annual interest rate into a monthly interest rate`

monthlyInterestRate = annualInterestRate /1200


# Calculate the monthly loan payment

monthlyPayment = loanAmount* monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))


#Calculate the total payment amount
totalPaymentAmout =  monthlyPayment * numberOfYears*12



#Display the montly payment and the total payment

print("the monthly payment is ", int(monthlyPayment*100)/100)

print("the total payment amount is ", int(totalPaymentAmout*100)/100)



