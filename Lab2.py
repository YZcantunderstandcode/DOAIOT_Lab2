file1 = open("users.txt", "a")
name = input("Enter your name: ")
age = input("Enter your age: ")
weight = input("Enter your weight: ")
height = input("Enter your height: ")
bmi = round(float(weight) / (float(height)) ** 2, 2)

print("BMI: ", bmi)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print("BMI Category: ", category)

file1.write(f"Name: {name}\nage: {age} \nweight: {weight} \nheight: {height} \nBMI: {bmi} \nCategory: {category}\n\n")
file1.close()