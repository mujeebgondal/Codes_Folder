"""
The body mass index (BMI) was created by a Belgian mathematician in the 1850s and 
it's used by health and nutrition professionals to quickly estimate body fat in 
certain populations.
"""
mass=float(input("Enter your mass in kg: ")) 
height=float(input("Enter your height in meters: "))
bmi=round(mass/height**2,2)
print("your BMI is", bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You have a normal weight")
elif bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese")            