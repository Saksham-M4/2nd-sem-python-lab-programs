password = input("Enter a password: ")

has_upper = False
has_digit = False
has_symbol = False

length = len(password)

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isalnum():
        has_symbol = True

if length < 8 or length > 15:
    print("Password is Weak")
else:
    strength = has_upper + has_digit + has_symbol

    if strength == 3:
        print("Password is Strong")
    elif strength == 2:
        print("Password is Moderate")
    else:
        print("Password is Weak")
