import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, "r") as pybank:
    csvreader = csv.reader(pybank, delimiter=",") 

    months = 0
    profit_loss = 0

    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            months = months + 1
            profit_loss = profit_loss + int(row[1])
            
print("Financial Statement")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total ${profit_loss}")