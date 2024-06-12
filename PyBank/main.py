import os
import csv

# get realtive path of csv file
budget_csv = os.path.join("Resources","budget_data.csv")

# create output variable
text = []

# open csv file and do analysis
with open(budget_csv) as csv_file:
    # parse csv file
    csv_reader = csv.reader(csv_file, delimiter=",")
    # remove and store header
    csv_header = next(csv_file)
    # parse csv reader into lists: [date] and [profit/losses] columns
    # then create list: [profit/losses changes]
    date = []
    amount = []
    for row in csv_reader:
        date.append(row[0])
        amount.append(int(row[1]))
    # create list for profit/loss changes
    change = list(amount[n+1]-amount[n] for n in range(len(amount)-2))
    
    # store requested financial analysis as strings
    # title header
    text.append("Financial Analysis")
    text.append("----------------------------")
    # total number of months included in the dataset
    text.append(f"Total Months: {len(amount)}")
    # net total amount of profit/losses over the entire period
    text.append(f"Total: ${sum(amount)}")
    # average changes in profit/losses over the entire period
    text.append(f"Average Change: ${round((amount[len(amount)-1]-amount[0])/(len(amount)-1),2)}")
    # greatest increase in profit/losses (date and amount) over the entire period
    text.append(f"Greatest Increase in Profits: {date[change.index(max(change))+1]} (${max(change)})")
    # greatest decrease in profit/losses (date and amount) over the entire period
    text.append(f"Greatest Decrease in Profits: {date[change.index(min(change))+1]} (${min(change)})")

# write text file and print into terminal
with open('Outputs/financial_analysis.txt','w') as f:
    for line in text:
        f.write(line+"\n")
        print(line)