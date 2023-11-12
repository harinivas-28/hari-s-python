print("BMI CALCULATOR")
weight=int(input("Enter your weight in kg's:"))
height=float(input("Enter your height in meters:"))
bmi=weight/(height*height)
print(f"Your BMI is {bmi}")
if bmi<18.5:
    print("You Under Weight")
elif 18.5<bmi<24.9:
    print("You are Healthy")
elif 25<bmi<29.9:
    print("You are Over Weight")
else:
    print("You are Obese")