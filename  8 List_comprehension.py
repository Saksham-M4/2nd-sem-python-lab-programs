# 1️⃣ Using for-loop to store even numbers
new_list = []

for i in range(1, 11):
    if i % 2 == 0:
        new_list.append(i)

print(new_list)


# 2️⃣ Using list comprehension to store even numbers
new_list = [i for i in range(1, 11) if i % 2 == 0]
print(new_list)


# 3️⃣ Using for-loop to store "even" or "odd"
new_list = []

for i in range(1, 11):
    if i % 2 == 0:
        new_list.append("even")
    else:
        new_list.append("odd")

print(new_list)


# 4️⃣ Using list comprehension to store "even" or "odd"
new_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(new_list)
