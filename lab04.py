import os.path
import sys

fname = input("Enter the filename to sort: ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
lines = infile.readlines()
infile.close()

lineList = []

for line in lines:
    lineList.append(line.strip())

lineList.sort()

outfile = open("sorted.txt", "w+")

for line in lineList:
    outfile.write(line + "\n")

outfile.seek(0, 0)

fstr = outfile.read()

print("Sorted.txt content:", fstr)
print("Total lines:", len(lineList))

outfile.close()