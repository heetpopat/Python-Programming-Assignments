import re

with open("details.txt", "r") as file:
    text = file.read()

emails = re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    text
)

phones = re.findall(r"\b\d{10}\b", text)

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)

print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)

print("\nDates:")
for date in dates:
    print(date)