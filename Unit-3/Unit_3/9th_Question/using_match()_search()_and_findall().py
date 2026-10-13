import re

text = "Python is easy. Python is powerful. I like Python."

result1 = re.match(r"Python", text)

if result1:
    print("Match:", result1.group())
else:
    print("No match at the beginning.")

result2 = re.search(r"easy", text)

if result2:
    print("Search:", result2.group())
else:
    print("Word not found.")

result3 = re.findall(r"Python", text)

print("Findall:", result3)
print("Total occurrences:", len(result3))