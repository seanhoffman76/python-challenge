# PyPoll Homework Assignment - Sean Hoffman

# Load Modules
import os
import csv

# Define Variables
totvote = 0                                                             # Variable to hold the total number of votes submitted
cand_dict = {}                                                          # dictionary to capture the unique key of candidate and the associated value of votes for that candidate
candidates = []                                                         # list to move the candidate names into where they will remain ordered
candvotes = []                                                          # list to move the votes for each candidate into where they will remain ordered
percent = []                                                            # list to move an ordered calculation of % of vote for each candidate
winner = ''                                                             # variable cast as string to land the winning candidate's name into in proper format for reporting

# Set path for file
polling = os.path.join('Resources', 'election_data.csv')

# Open the CSV
with open(polling, newline="") as csvfile:
    polling_list = csv.reader(csvfile, delimiter=",")
    csv_header = next(polling_list)

    # Iterate through polling_list to calculate from polling_list total number of votes cast
    # unique candidates found in the data, and counting the number of votes for each candidate    
    for row in polling_list:
        totvote += 1                                                    # increments the number of total votes by 1 for each record passed
        if row[2] in cand_dict.keys():                                  # If polling_list.Candidate is in cand_dict dictionary, then add 1 vote for that candidate in the dictionary
            cand_dict[row[2]] = cand_dict[row[2]] + 1
        else:
            cand_dict[row[2]] = 1                                       # If polling_list.Candidate is NOT in cand_dict dictionary, then add candidate to the dictionary and give them their first vote

# Split the values from the cand_dict dictionary into candidates and candvotes lists
for key, value in cand_dict.items():
    candidates.append(key)
    candvotes.append(value)

# Iterate through candvotes to generate the percentage of candidate votes from the total number of votes
for vote in candvotes:
    percent.append(round(vote/totvote*100, 3))

# Use zip to combine the data from lists candidates, candvotes, & percent into a list of tuples to keep them combined
pollresult = list(zip(candidates, candvotes, percent))

# Write the name of the winner into a variable if that candidate has the maximum number of votes from pollresult
for name in pollresult:
    if max(candvotes) == name[1]:
        winner = name[0]


# Output the election results to the terminal  
print('')
print('-------------------------------------')
print('Election Results')
print('-------------------------------------')
print(f"Total Votes: {totvote}")
print('-------------------------------------')
for entry in pollresult:
    print(f'{entry[0]}: {entry[2]}% ({entry[1]})')
print('-------------------------------------')
print(f'Winner: {winner}')
print('-------------------------------------')



# Output the election results to a CSV file in the same format as above
    # Set variable for output file
output_file = os.path.join("PyPoll_Analysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(['-------------------------------------'])
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------------------'])
    writer.writerow([f"Total Votes: {totvote}"])
    writer.writerow(['-------------------------------------'])
    for entry in pollresult:
        writer.writerow([f'{entry[0]}: {entry[2]}% ({entry[1]})'])
    writer.writerow(['-------------------------------------'])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(['-------------------------------------'])

# End of homework assignment PyPoll