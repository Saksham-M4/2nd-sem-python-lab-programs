#.join() method is used to combine multiple strings into ONE string.
words = [ "python","is","easy"]
result = " ".join(words)
print(result)
items = ["apple", "banana", "mango"]
print(",".join(items))
print("-".join(items))
folders = ["usr", "bin", "python"]
print("/".join(folders))
data = ["101", "Manu", "Bangalore"]
csv_line = ",".join(data)
print(csv_line)
nums = [1, 2, 3]
number = "-".join(map(str, nums))
print(number)
numbers = [1, 2, 3, 4, 5, 6]
result = []
for n in numbers:
    if n % 2 ==0:
        result.append(str(n))
        print(",".join(result))
        










