numbers = [1, 2, 3, 4, 5]

def is_even(num):
    return num % 2 == 0

even_numbers = list(
    filter(is_even, numbers)
)

print(f"Even numbers: {even_numbers}")