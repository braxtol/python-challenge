# Bring in libraries
import os
import csv

# Declare variables
MCounter = 0
Total = 0
AvgChg = 0
GrtProfit = 0
GrtLoss = 0
Mchange = []

# Define the csv file and path as the variable "csvpath"
csvpath = os.path.join("PyBank/Resources", "budget_data.csv")

# Open csv file then assign it the variable "csvfile"
with open(csvpath, encoding='utf-8') as csvfile:
    # Be able to read the file as the variable "csvreader"
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    FirstRow = next(csvreader)
    MCounter += 1
    Total += int(FirstRow[1])
    PrevRowProfit = int(FirstRow[1])
    # Loop through rows of csv file
    for row in csvreader:
        # Total of months
        MCounter += 1
        # Total Profits/Losses
        Total += int(row[1])
        # Changes for each month
        CurrentChange = int(row[1]) - PrevRowProfit
        Mchange.append(CurrentChange)
        # Next row
        PrevRowProfit = int(row[1])
        # Greatest increase and its date
        if CurrentChange > GrtProfit:
            GrtProfit = CurrentChange
            GrtProfitM = str(row[0])
        # Greatest decrease and its date
        if CurrentChange < GrtLoss:
            GrtLoss = CurrentChange
            GrtLossM = str(row[0])
# Remove 1st row then find average of monthly change
AvgChg = sum(Mchange)/(len)(Mchange)

# Make data conform to accountant's formatting    
Formatted_Total = "{:,.2f}".format(Total)
Formatted_AvgChg= "{:,.2f}".format(AvgChg)
Formatted_GrtProfit= "{:,.2f}".format(GrtProfit)
Formatted_GrtLoss= "{:,.2f}".format(GrtLoss)
# Print data
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {MCounter}")
print(f"Total Amount: ${Formatted_Total}")
print(f"Total Change: ${Formatted_AvgChg}")
print(f"Greatest Increase in Profits: {GrtProfitM} ${Formatted_GrtProfit}")
print(f"Greatest Decrease in Profits: {GrtLossM} ${Formatted_GrtLoss}") 
print("----------------------------------------")  

# Save the new file
output_file = os.path.join("PyBank/Analysis", "results.txt")
# Write on output file
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n--------------------------------------------")
    textfile.write(f"\nTotal Months: {MCounter}")
    textfile.write(f"\nTotal Amount: ${Formatted_Total}")
    textfile.write(f"\nTotal Change: ${Formatted_AvgChg}")
    textfile.write(f"\nGreatest Increase in Profits: {GrtProfitM} ${Formatted_GrtProfit}")
    textfile.write(f"\nGreatest Decrease in Profits: {GrtLossM} ${Formatted_GrtLoss}")
    textfile.write("\n--------------------------------------------")