# Program to find maximum number using lambda

numbers = [10, 25, 5, 78, 34]

maximum = max(numbers, key=lambda x: x)

print("List:", numbers)

print("Maximum Number:", maximum)