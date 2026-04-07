name = input("Enter name: ")
year_of_birth = int(input("Enter year of birth: "))

current_year = 2026
age = current_year - year_of_birth

print("\nName:", name)
print("Age:", age)

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")