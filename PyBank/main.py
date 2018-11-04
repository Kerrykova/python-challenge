import os
import csv

csvpath = os.path.join("..", "python-challenge", "pybank", "budget_data.csv")

with open(csvpath, "r", newline=" ") as pybank:
    csvreader = csv.reader(pybank, delimiter=",") 

      