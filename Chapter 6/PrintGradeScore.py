def getGrade(score):
    if score >= 90.00:
        return 'A'
    elif score >= 80.00:
        return 'B'
    elif score >= 70.00:
        return 'C'
    elif score >= 60.00:
        return 'D'
    else:
        return 'F'

def main():
    score = eval(input("Enter the score: "))
    print("The grade is: ",getGrade(score) )

main()
