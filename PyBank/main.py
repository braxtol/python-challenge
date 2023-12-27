import os
import csv
date = input("What day do you want the profit/loss for? ")
csvpath = os.path.join( "Resources", "budget_data.csv")
found = False

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == date:
            print(row[0] + " had " + row[1] + " change ")

            # Set variable to confirm we have found the video
            found = True


    # If the book is never found, alert the user
    if found is False:
        print("Sorry. There is no record for that date requested.")