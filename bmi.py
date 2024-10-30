def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = round(float(weight) / (float(height)) ** 2, 2)
    print("BMI: ", bmi)
    print("Weight Classification: ", end="")

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif bmi >  25.0:
        print("Overweight")

calculate_bmi(weight=57, height=1.73)