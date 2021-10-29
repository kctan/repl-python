number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
number1 = float(number1)
number2 = float(number2)

if number1 < number2:
    print("1st number is smaller than 2nd number")
elif number1 > number2:
    print("1st number is greater than 2nd number")
else:
    print("The 2 numbers are equal")
