import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, "r") as pybank:
    csvreader = csv.reader(pybank, delimiter=",") 

    months = 0
    profit_loss = int(0)
    ave_pl_change = 0
    increase_delta = 0
    decrease_delta = 0

    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            months = months + 1
            prev_val = profit_loss
            profit_loss = profit_loss + int(row[1])
            delta = profit_loss - prev_val
            ave_pl_change = (ave_pl_change + delta) / months
            if delta > increase_delta:
                increase_delta = delta
                month_name_inc = row[0]
            if delta < decrease_delta:
                decrease_delta = delta
                month_name_dec = row[0]


            
print("Financial Statement")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total ${profit_loss}")
print(f"Average Change: ${round(ave_pl_change)}")
print(f"Greatest Increase in Profits: {month_name_inc} (${increase_delta})")
print(f"Greatest Decrease in Profits: {month_name_dec} (${decrease_delta})")