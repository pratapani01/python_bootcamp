import os

path = "chapter1"

contents = os.listdir(path)

print(f"Contents of '{path}':")
for item in contents:
    print(item)