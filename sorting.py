import csv
import shutil

with open("data/trainLabels/trainLabels.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "image":
            continue
        shutil.move(f"data/train/{row[0]}.jpeg", f"data_sorted/{row[1]}/{row[0]}.jpeg")
