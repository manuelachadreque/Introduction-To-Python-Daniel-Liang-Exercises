today=eval(input("Input today's number of the week day: "))

lapseDays = eval(input("Input the number of days from today: "))

weekDay= (today + lapseDays) % 7

print("if today is ", today, " ", lapseDays," days from now will be a ", weekDay)
