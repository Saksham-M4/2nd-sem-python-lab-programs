from loguru import logger

count = 0

# SINGLE-LINE PARAGRAPH — REQUIRED FOR split(" ") TO WORK
paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
thought leader in the data warehouse and business intelligence industry. He has 
educated tens of thousands of IT professionals. The books written by Ralph and 
his colleagues have been the industry's best sellers since 1996. Prior to working 
at Metaphor and founding Red Brick Systems, Ralph co-invented the Star 
workstation, the first commercial product with windows, icons, and a mouse at 
the famous Xerox Palo Alto Research Center."""


count = 0
print(paragraph.lower().split())   # direct split inside print

for word in paragraph.lower().split():
    if word == "the":
        count += 1

logger.info(f"Total count for the article: {count}")


# -------- PART 2: insert x into sorted list --------
lst = [5, 18, 77, 108, 930]
x = 100

index = 0
for num in lst:
    if num > x:
        break
    index += 1

lst.append(None)   # increase list size

for i in range(len(lst) - 1, index, -1):
    lst[i] = lst[i - 1]

lst[index] = x
print(lst)
