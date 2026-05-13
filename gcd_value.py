# Program to find GCD using function

def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a

# Function call
result = gcd(12, 18)

print("GCD is:", result)