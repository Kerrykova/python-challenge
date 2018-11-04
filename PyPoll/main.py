import os
import csv

csvpath = os.path.join("..", "python-challenge", "pypoll", "election_data.csv")

with open(csvpath, "r", newline=" ") as pypoll:
    csvreader = csv.reader(pypoll, delimiter=",")
    