# Program to check prime number

num = 11

flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")