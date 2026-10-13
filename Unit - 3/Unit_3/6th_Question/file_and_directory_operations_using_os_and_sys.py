import os
import sys

print("Current Directory:", os.getcwd())

folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created successfully.")
else:
    print("Directory already exists.")

file_path = os.path.join(folder, "sample.txt")

with open(file_path, "w") as f:
    f.write("Hello, Python!")

print("File created successfully.")
print("Contents:", os.listdir(folder))
print("Python Version:", sys.version)

new_path = os.path.join(folder, "renamed.txt")
os.rename(file_path, new_path)
print("File renamed successfully.")

os.remove(new_path)
print("File deleted successfully.")

os.rmdir(folder)
print("Directory removed successfully.")

print("Command-line Arguments:", sys.argv)