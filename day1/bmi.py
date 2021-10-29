weight = input("Enter your weight (kg):")
height = input("Enter your height (m):")

weight = float(weight)
height = float(height)

bmi = weight/(height * height)

print("bmi: " + str(bmi))

if bmi < 18:
    print ("You are underweight.")
elif bmi <25:
    print("Your weight is ideal.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")