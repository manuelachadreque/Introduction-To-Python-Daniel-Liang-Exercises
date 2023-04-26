from BMI import  BMI

def main():
    name = input("Input the name: ")
    age = eval(input("Input the age: "))
    weight = eval(input("type your weight: "))
    height = eval(input("Type yout height: "))
    bmi1 = BMI(name, age, weight, height)
    print("The BMI for", bmi1.getName(), " is ", bmi1.getBMI(), bmi1.getStatus())


main()
