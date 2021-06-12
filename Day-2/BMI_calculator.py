weight = float(input('Enter your weight in kg: \n'))
height = float(input('Enter your height in m: \n'))
# BMI = Weight(kg)/Height**2

BMI = int(weight / height**2)
print("Your BMI is:")
print(BMI)