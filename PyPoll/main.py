import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, "r") as pypoll:
    csvreader = csv.reader(pypoll, delimiter=",")
    
    votes = 0

    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            votes = votes + 1
           
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes}")
print("----------------------------")
print(f"Khan:")
print(f"Correy:")
print(f"Li:")
print("----------------------------")
print(f"Winner:")
print("----------------------------")

file = open("PyPoll.txt","w")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {votes}\n")
file.write("----------------------------\n")
file.write(f"Khan:\n")
file.write(f"Correy:\n")
file.write(f"Li:\n")
file.write("----------------------------\n")
file.write(f"Winner:\n")
file.write("----------------------------\n")
file.close()    