def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


print("Welcome to the BMI Calculator")
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi, category = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} which would fall into the {category} category.")
    
except ValueError:
    print("Please enter numeric values for weight and height.")
