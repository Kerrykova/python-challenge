import os
import csv

csvpath = os.path.join("election_data.csv")

votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(csvpath, "r") as pypoll:
    csvreader = csv.reader(pypoll, delimiter=",")

    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            votes = votes + 1
            if row[2] == "Khan":
                khan += 1
                kahn_percent = (khan/votes) * 100
            if row[2] == "Correy":
                correy += 1
                correy_percent = (correy/votes) * 100
            if row[2] == "Li":
                li += 1
                li_percent = (li/votes) * 100
            if row[2] == "O'Tooley":
                otooley += 1
                otooley_percent = (otooley/votes) * 100
            if khan > correy and li and otooley:
                winner = "Khan"
            if correy > khan and li and otooley:
                winner = "Correy"
            if li > correy and khan and otooley:
                winner = "Li"
            if otooley > correy and li and khan:
                winner = "O'Tooley"    
            
           
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes}")
print("----------------------------")
print(f"Khan: {round(kahn_percent)}% ({khan})")
print(f"Correy: {round(correy_percent)}% ({correy})")
print(f"Li: {round(li_percent)}% ({li})")
print(f"O'Tooley: {round(otooley_percent)}% ({otooley})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

file = open("PyPoll.txt","w")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {votes}\n")
file.write("----------------------------\n")
file.write(f"Khan: {round(kahn_percent)}% ({khan})\n")
file.write(f"Correy: {round(correy_percent)}% ({correy})\n")
file.write(f"Li: {round(li_percent)}% ({li})\n")
file.write(f"O'Tooley: {round(otooley_percent)}% ({otooley})\n")
file.write("----------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("----------------------------\n")
file.close()    