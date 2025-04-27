# File Read/Write
with open("sample.txt", "w") as f:
    f.write("Hello, File!")

with open("sample.txt", "r") as f:
    print(f.read())
