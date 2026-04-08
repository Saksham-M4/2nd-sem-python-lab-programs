# Step 1: Input number of items
n = int(input("Enter number of elements: "))

# Step 2: Create empty list
myList = []

# Step 3: Input elements and find sum
tot = 0
for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    myList.append(num)
    tot += num

# Step 4: Calculate mean
mean = tot / n

# Step 5: Calculate sum of squared differences
tot = 0
for item in myList:
    tot += (item - mean) ** 2

# Step 6: Calculate variance
variance = tot / n

# Step 7: Calculate standard deviation
std_dev = variance ** 0.5

# Step 8: Print results
print("\nResults:")
print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", std_dev)