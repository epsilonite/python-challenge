import os
import csv

# get realtive path of csv file
election_csv = os.path.join("Resources","election_data.csv")

# create output and anaylsis variable
text = []

# open csv file and do analysis
with open(election_csv) as csv_file:
    # parse csv file
    csv_reader = csv.reader(csv_file, delimiter=",")
    # remove and store header
    csv_header = next(csv_file)
    # parse csv file into a dictionary: {candidate: total votes}
    results = {}
    for row in csv_reader:
        if row[2] in results.keys():
            results[row[2]] += 1
        else:
            results[row[2]] = 1
    
    # store requested election results as strings
    # title header
    text.append('Election Results')
    text.append('-------------------------')
    # total number of votes cast
    text.append(f'Total Votes: {sum(results.values())}')
    text.append('-------------------------')
    # complete list of candidates an the votes they won formatted as: percentage (totals)
    for k,v in results.items():
        text.append(f'{k}: {round(100*v/sum(results.values()),3)}% ({v})')
    text.append('-------------------------')
    # name of winning candidate
    text.append(f'Winner: {sorted(results.items(), key=lambda item: item[1]).pop()[0]}')
    text.append('-------------------------')

# write text file and print into terminal
with open('Outputs/election_results.txt','w') as f:
    for line in text:
        f.write(line+"\n")
        print(line)