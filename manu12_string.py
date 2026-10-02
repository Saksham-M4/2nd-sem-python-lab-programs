from loguru import logger
name = "manish kumar"
# count = 0
# for char in name:
#     print(count,char)

print(name[:4])
print(name.capitalize())
print(name.count("a"))
# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
print(name.endswith("a"))
print(name.lower())
print(name.upper())
print(name.strip())
new_name = name.replace("manish","saksham")
print(new_name)
print(len(name))
print(name.swapcase())
names = "Manu Saksham randy viru"

names_list = names.split(" ")

result = []
for x in names_list:
    if x.endswith("m"):
        result.append(x)
    else:
        print(f"{x} does not end with m")

print(result)
email = "manishkumar@gmail.com"

name,domain = email.split("@")
print(name,domain)
masked_name = name[0] + "*" * (len(name)-2) + name[-1]
masked_email = masked_name +"@" + domain
print(masked_email)
print(masked_name)
s = "hi"
for i in range(len(s)):
    print(i,s[i])
paths = [
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]

unique_ips = set()

for path in paths:
    ip = path.split("/server/")[1].split("/")[0]
    unique_ips.add(ip)

print(list(unique_ips))
s = "Programming Aasan Hai"
result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch   # space or symbol

print(result)









