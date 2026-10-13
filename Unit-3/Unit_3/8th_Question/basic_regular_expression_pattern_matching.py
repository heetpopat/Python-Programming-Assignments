import re

text = "Python programming is easy."

pattern = r"Python"
result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found.")

result = re.match(r"Python", text)

if result:
    print("Match at beginning:", result.group())

text2 = "My age is 20."
result = re.search(r"\d+", text2)

if result:
    print("Number found:", result.group())

result = re.search(r"\bP\w+", text)

if result:
    print("Word starting with P:", result.group())