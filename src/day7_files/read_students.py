import csv
import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "students.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
