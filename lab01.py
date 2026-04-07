# Read student details
name = input("Enter student name: ")
dob = input("Enter DOB: ")
reg_no = input("Enter register number: ")
dept = input("Enter department: ")

# Read marks (5 subjects)
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display details
print("\n--- Student Details ---")
print("Name:", name)
print("DOB:", dob)
print("Register No:", reg_no)
print("Department:", dept)
print("Total Marks:", total)
print("Percentage:", percentage)

# Result message
if percentage >= 75:
    print("Result: Distinction")
elif percentage >= 60:
    print("Result: First Class")
elif percentage >= 50:
    print("Result: Second Class")
else:
    print("Result: Fail")