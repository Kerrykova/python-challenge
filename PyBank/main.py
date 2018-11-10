# import dependencies
import os
import csv

# path to csv
csvpath = os.path.join("budget_data.csv")

# open and read csv
# first row is the header
with open(csvpath, "r") as pybank:
    csvreader = csv.reader(pybank, delimiter=",") 
    csv_header = next(csvreader)

# create variables and list to capture profit/loss values
    months = 0
    total_profit_loss = 0
    profit_loss = 0
    increase_delta = 0
    decrease_delta = 0
    sum_delta = 0
    prev_value = 0
    ave_pl_change = 0
    first_pl = []

# for loop to add pl to list, count months, total pl, change in pl
    for row in csvreader:
        first_pl.append(row[1])
        prev_value = prev_value
        months = months + 1
        profit_loss = int(row[1])
        total_profit_loss = total_profit_loss + int(row[1])
        # compute each pl change and total of pl changes
        delta = profit_loss - prev_value
        sum_delta = sum_delta + delta
        # assign previous pl value for next for loop
        prev_value = int(row[1])
        # if stmt to check for min and max pl change and the month they occurred 
        if delta > increase_delta:
            increase_delta = delta
            month_name_inc = row[0]
        if delta < decrease_delta:
            decrease_delta = delta
            month_name_dec = row[0] 
    # assign the first list index to variable             
    first_pl_cut = first_pl[0]
    # remove first pl from the total of pl changes and divide by one less the total months to get the average of pl changes
    ave_pl_change = (sum_delta - int(first_pl_cut)) / (months - 1)

# use f strings to print summary of data                  
print("Financial Statement")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total ${total_profit_loss}")
print(f"Average Change: ${round(ave_pl_change,2)}")
print(f"Greatest Increase in Profits: {month_name_inc} (${increase_delta})")
print(f"Greatest Decrease in Profits: {month_name_dec} (${decrease_delta})")

# create a new text file and write the print stmts to that file
file = open("PyBank.txt","w")
file.write("Financial Statement\n")
file.write("----------------------------\n")
file.write(f"Total Months: {months}\n")
file.write(f"Total ${total_profit_loss}\n")
file.write(f"Average Change: ${round(ave_pl_change, 2)}\n")
file.write(f"Greatest Increase in Profits: {month_name_inc} (${increase_delta})\n")
file.write(f"Greatest Decrease in Profits: {month_name_dec} (${decrease_delta})\n")
file.close()    