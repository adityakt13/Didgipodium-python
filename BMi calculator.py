print("Know your BMI to know your health better")
print("Aditya BMI Calculator service")
height = float(input("Enter your height in c.m.: "))/100 #to convert height into metres
weight = float(input("Enter your weight in kilograms: "))
BMI = weight / (height **2)
if BMI <18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
if BMI >= 18.5 and BMI <25:
    print(f"Your BMI is {BMI}, your weight is normal.")
elif BMI >=25 and BMI <30:
    print(f"Your BMI is {BMI}, you are overweight.")
else:
    print(f"Your BMI is {BMI}, you are obese.")
print("Thanyou for using our services , visit again.")