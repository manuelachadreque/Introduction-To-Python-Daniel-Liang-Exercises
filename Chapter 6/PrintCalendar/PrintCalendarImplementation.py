
def printMonth(year, month):
    # print the headings of the calendar
    printMonthTitle(year, month)
    #print the body of the calendar
    printMonthBody(year, month)

def printMonthTitle(year, month):
    print("        ", getMonthName(month), "          ")
    print("___________________________________________")
    print("Sun Mon Tue Wen Thu Fri Sat")



def getStartDay(year, month):
    START_DAY_OF_YEAR_1800 = 3

    totalNumberOfDays = getTotalNumberOfDays(year, month)

    return (totalNumberOfDays + START_DAY_OF_YEAR_1800) %7


def printMonthBody(year, month):
    startDay= getStartDay(year, month)
    numberOfInDays = getNumberOfDaysInMonth(year, month)

    #Pad space before each day of month
    i=0
    for i in range(0, startDay):
        print("    ", end=" ")

    for i in range(1, numberOfInDays+1):
        print(format(i, "4d"), end=" ")

        if (i+startDay) % 7 == 0:
            print() #Jump to new line

def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName ="April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month ==7:
        monthName = "July"
    elif month == 8:
        monthName = "Augost"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"
    return monthName

def getTotalNumberOfDays(year, month):
    total =0
    for i in range(1800, year):
        if isLeapYear(i):
            total = total +366
        else:
            total = total +365

        #Add days from January to Calendar month
        for i in range(1, month):
            total = total +getNumberOfDaysInMonth(year, i)
    return  total


#get start day of the month
def getNumberOfDaysInMonth(year, month):
    if (month ==1 or month == 3 or month == 5 or month == 7 or month ==8 or month ==10 or month ==12):
        return 31
    if (month == 4 or month ==6 or month ==9 or month ==11):
        return 30
    if month ==2:
        return 29 if isLeapYear(year) else 28

def isLeapYear(year):
    return year % 400 ==0 or (year % 4 == 0 and year %100 != 0)






