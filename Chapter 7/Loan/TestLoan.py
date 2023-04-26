from Loan import Loan

def main():

    annualInterestRate=eval(input("enter the annual interest rate, example, 725: "))

    numberOfYears = eval(input("enter the number of years: "))

    loanAmount = eval(input("Enter the loan amount: "))

    borrower = input("Enter the borrowe name: ")

    #Create a loan object

    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    #Display loan date, monthly payment and total payment

    print("The loan is for ", loan.getBorrower())
    print("Th monthly payment is ", loan.getmonthlyPayment())
    print("The total payento is ", loan.getTotalPayment())

main()