'''
 Enter 0 for single filers,
 1 for married filing jointly,
 2 for married filing separately,
  and 3 for head of household.
'''

import sys

fillingStatus = eval(input("Enter you salary ( Enter 0 for single filers, 1 for married filing jointly,"
                    " 2 for married filing separately, and 3 for head of household): "))
salary = eval(input("Enter the salary: "))

if fillingStatus == 0:
    if salary < 8350:
        tax = salary*0.10
        netIncome = salary-tax
    elif salary < 33950:
        tax = 8350*0.10 + (salary-8350)*0.15
        netIncome = salary-tax
    elif salary < 82250:
        tax = 8350*0.10+(33950-8350)*0.15 + (salary-33950)*0.25
        netIncome = salary-tax
    elif salary < 171550:
        tax = 8350*0.10+(33950-8350)*0.15 + (82250-33950)*0.25 + (salary-82250)*0.28
        netIncome = salary-tax
    elif salary < 372950:
        tax = 8350*0.10+(33950-8350)*0.15 + (82250-33950)*0.25 + (171550-82250)*0.28 + (salary-372950)*0.33
        netIncome = salary-tax
    elif salary >= 372950:
        tax = 8350*0.10+(33950-8350)*0.15 + (82250-33950)*0.25 + (171550-82250)*0.28 + (372950 - 171550)*0.33 +\
              (salary-372950)*0.35
        netIncome = salary-tax
    else:
        print("Error: invalid status")
        sys.exit()

elif fillingStatus == 1:
    if salary < 16700:
        tax = 16700*0.10
        netIncome = salary-tax
    elif salary < 67900:
        tax = 16700*0.10+(67900-16700)*0.15
        netIncome = salary-tax
    elif salary < 137050:
        tax = 16700*0.10+(67900-16700)*0.15 + (salary-67900)*0.25
        netIncome = salary-tax
    elif salary < 208850:
        tax = 16700*0.10+(67900-16700)*0.15 + (137050-67900)*0.25 + (salary-137050)*0.28
        netIncome = salary-tax
    elif salary < 372950:
        tax = 16700*0.10+(67900-16700)*0.15 + (208850-67900)*0.25 + (208850-137050)*0.28 + (salary - 208850)*0.33
        netIncome = salary-tax
    elif salary >= 372950:
        tax = 16700 * 0.10+(67900-16700)*0.15 + (208850-67900)*0.25 + (208850-137050)*0.28 + (372950 - 208850)*0.33 +\
              (salary-372950)*0.35
        netIncome = salary-tax
    else:
        print("Error: invalid status")
        sys.exit()

elif fillingStatus == 2:
    if salary < 8350:
        tax = 8350 * 0.10
        netIncome = salary-tax
    elif salary < 33950:
        tax = 8350 * 0.10+(salary-8350)*0.15
        netIncome = salary-tax
    elif salary < 68525:
        tax = 8350 * 0.10+(33950-8350)*0.15 + (salary-33950)*0.25
        netIncome = salary-tax
    elif salary < 104425:
        tax = 8350 * 0.10+(33950-8350)*0.15 + (68525-33950)*0.25 + (salary-68525)*0.28
        netIncome = salary-tax
    elif salary < 186475:
        tax = 8350 * 0.10+(33950-8350)*0.15 + (68525-33950)*0.25 + (104425-68525)*0.28 + (salary - 104425)*0.33
        netIncome = salary-tax
    elif salary >= 186475:
        tax = 8350 * 0.10+(33950-8350)*0.15 + (68525-33950)*0.25 + (104425-68525)*0.28 + (186475 - 104425)*0.33 +\
              (salary-186476)*0.35
        netIncome = salary-tax
    else:
        print("Error: invalid status")
        sys.exit()

else:
    if salary < 11950:
        tax = salary*0.10
        netIncome = salary * .9
    elif salary < 45500:
        tax = salary*0.15
        netIncome = salary * .85
    elif salary < 117450:
        tax = salary*0.25
        netIncome = salary * .75
    elif salary < 190200:
        tax = salary*0.28
        netIncome = salary * .72
    elif salary < 372950:
        tax = salary*0.33
        netIncome = salary * .67
    elif salary >= 372950:
        tax = 117450 * 0.10+(117450-11950)*0.15 + (117450-45500)*0.25 + (190200-117450)*0.28 + (372950 - 190200)*0.33 +\
              (salary-372950)*0.35
        netIncome = salary-tax
    else:
        print("Error: invalid status")
        sys.exit()
print("Your tax is ", tax)
print("Your net income is", netIncome)




