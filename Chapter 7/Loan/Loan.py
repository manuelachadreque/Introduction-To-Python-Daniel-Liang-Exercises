class Loan:
    def __init__(self, annualInterestRate =2.5,
                 numberOfYears =10, loanAmount= 1000, borrower =" " ):
        self.__annualInterestRate__ =annualInterestRate
        self.__numberOfYears__ = numberOfYears
        self.__loanAmount__ =loanAmount
        self.__borrower__ = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate__

    def getNumberOfYeatr(self):
        return self.__numberOfYears__

    def getLoadnAmout(self):
        return self.__loanAmount__

    def getBorrower(self):
        return self.__borrower__

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate__= annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears__ = numberOfYears

    def setLoanAmout(self,loanAmout):
        self.__loanAmount__ =loanAmout
    def setBorrower(self, borrower):
        self.__borrower__ =borrower

    def getmonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate__/1200
        montlyPayment=self.__loanAmount__*monthlyInterestRate/(1-(1/(1+monthlyInterestRate)**(self.__numberOfYears__*12)))
        return montlyPayment
    def getTotalPayment(self):
        totalPayment = self.getmonthlyPayment()*self.__numberOfYears__*12
        return totalPayment
