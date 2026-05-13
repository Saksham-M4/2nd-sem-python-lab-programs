n = 5

# upper part
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))


# lower part
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))
    