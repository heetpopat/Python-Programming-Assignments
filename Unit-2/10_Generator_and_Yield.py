
# Generate a sequence using a generator and yield

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

count = int(input("How many numbers to generate? "))

print("Generated sequence:")
for number in generate_numbers(count):
    print(number)
