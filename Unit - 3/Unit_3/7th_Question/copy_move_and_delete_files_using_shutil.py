import os
import shutil

os.makedirs("Demo", exist_ok=True)

with open("Demo/source.txt", "w") as f:
    f.write("This is a sample file.")

shutil.copy("Demo/source.txt", "Demo/copy.txt")
print("File copied successfully.")

os.makedirs("Destination", exist_ok=True)

shutil.move("Demo/copy.txt", "Destination/copy.txt")
print("File moved successfully.")

os.remove("Destination/copy.txt")
print("File deleted successfully.")

os.remove("Demo/source.txt")

os.rmdir("Demo")
os.rmdir("Destination")

print("All operations completed.")