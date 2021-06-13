weight = float(input('Enter your weight in kg: \n'))
height = float(input('Enter your height in m: \n'))
# BMI = Weight(kg)/Height**2

BMI = round(weight / height**2, 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are Underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are Normal Weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are Overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are Obese")
else:
    print(f"Your BMI is {BMI}, you are Clinically obese")
