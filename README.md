# python-challenge
Simple python scripts to parse csv files to do some data analysis then output results into a text file.

## PyBank
This script looks at monthly profit/losses amounts. The information provided in the sample file has two columns: date, and profit/loss as dollar amount. The script does the following calculations and outputs them into the following text:
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

## PyPoll
This script looks at polling data. The information provided in the sample file has three columns: ballot id, county name, amd camdidate name. The script does the following calculations and outputs them into the following text:
'''
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''