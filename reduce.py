# Program to find sum of numbers using reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)

print("List:", numbers)

print("Sum:", sum_result)