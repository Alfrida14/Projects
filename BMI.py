weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))

bmi=weight/(height**2)
print("BMI=",bmi)

if bmi<18.5:
    print("You are Underweight.")

elif bmi>=18.5 and bmi<=24.9:
    print("Your weight is Normal.")

elif bmi>=25 and bmi<=29.9:
    print("You are Overweight.")

else:
    print("You are Obese.")
