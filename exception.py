# Program using try, except, else and finally

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:

    print("Error: Please enter only numbers")

except ZeroDivisionError:

    print("Error: Division by zero is not possible")

else:

    print("Result of division =", result)

finally:

    print("Program has been executed completely")