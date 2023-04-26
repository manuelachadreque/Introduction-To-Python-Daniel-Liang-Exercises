'''
Body mass index (BMI) is a measure of health based on weight. It can be calculated by taking
your weight in kilograms and dividing it by the square of your height in meters. The interpretation of BMI for people 16 years and older is as follows:

BMI Interpretation
----------------------
Below 18.5 Underweight
18.5–24.9 Normal
25.0–29.9 Overweight
Above 30.0 Obese
'''

weight = eval(input("Enter your weigh in pounds: "))

height = eval(input("Enter your height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH

bmi = weightInKilograms / (heightInMeters * heightInMeters)
print("your BMI is: ", bmi)
if bmi < 18.5:
    print("Obese")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
