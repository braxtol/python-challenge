# Bring in libraries
import os
import csv

# Declare variables
VCounter = 0
column_index = 2 
CandidateOne = "Charles Casper Stockham"
SumCandidateOne = 0
PctCandidateOne = 0
CandidateTwo = "Diana DeGette"
SumCandidateTwo = 0
PctCandidateTwo = 0
CandidateThree = "Raymon Anthony Doane"
SumCandidateThree = 0
PctCandidateThree = 0
CWinner = 0

# Define the csv file and path as the variable "csvpath"
csvpath = os.path.join("PyPoll/Resources", "election_data.csv")

# Open csv file then assign it the variable "csvfile"
with open(csvpath, encoding='utf-8') as csvfile:
    # Be able to read the file as the variable "csvreader"
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip first row
    next(csvreader)
    # Loop through rows of csv file
    for row in csvreader:
        # Total of votes
        VCounter += 1
        # Total votes first candidate
        if row[column_index] == CandidateOne:
            SumCandidateOne += 1
        # Total votes second candidate
        if row[column_index] == CandidateTwo:
            SumCandidateTwo += 1
        # Total votes third candidate
        if row[column_index] == CandidateThree:
            SumCandidateThree += 1
# Calculate percentage results
PctCandidateOne = (SumCandidateOne/VCounter)*100
PctCandidateTwo = (SumCandidateTwo/VCounter)*100
PctCandidateThree = (SumCandidateThree/VCounter)*100
# Format percentages
FPctCandidateOne = round(PctCandidateOne, 3)
FPctCandidateTwo = round(PctCandidateTwo, 3)
FPctCandidateThree = round(PctCandidateThree, 3)
# Determine winner
CWinner = max(SumCandidateOne, SumCandidateTwo, SumCandidateThree)
if CWinner == SumCandidateOne:
    Winner = CandidateOne
if CWinner == SumCandidateTwo:
    Winner = CandidateTwo
else:
    Winner = CandidateThree
# Print data}
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {VCounter}")
print("----------------------------------------")
print(f"{CandidateOne}: {FPctCandidateOne}% ({SumCandidateOne})")
print(f"{CandidateTwo}: {FPctCandidateTwo}% ({SumCandidateTwo})")
print(f"{CandidateThree}: {FPctCandidateThree}% ({SumCandidateThree})")
print("----------------------------------------")
print(f"Winner: {Winner} ")
print("----------------------------------------")
# Save the new file
output_file = os.path.join("PyPoll/Analysis", "results.txt")
# Write on output file
with open(output_file, "w") as textfile:
    textfile.write("Election Results")
    textfile.write("\n----------------------------------------")
    textfile.write(f"\nTotal Votes: {VCounter}")
    textfile.write("\n----------------------------------------")
    textfile.write(f"\n{CandidateOne}: {FPctCandidateOne}% ({SumCandidateOne})")
    textfile.write(f"\n{CandidateTwo}: {FPctCandidateTwo}% ({SumCandidateTwo})")
    textfile.write(f"\n{CandidateThree}: {FPctCandidateThree}% ({SumCandidateThree})")
    textfile.write("\n----------------------------------------")
    textfile.write(f"\nWinner: {Winner} ")
    textfile.write("\n----------------------------------------")