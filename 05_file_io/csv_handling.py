# CSV Handling
import csv

with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
