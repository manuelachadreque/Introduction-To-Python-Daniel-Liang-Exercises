from PrintCalendarImplementation import printMonth

def main():
    year = eval(input("enter a full year, e.g 2020: "))
    month = eval(input("Enter a month, e.g. 5 for May: "))

    printMonth(year, month)

main()
