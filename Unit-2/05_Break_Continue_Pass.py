
# Demonstrate break, continue, and pass

print("1. Break statement")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n2. Continue statement")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n3. Pass statement")
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
