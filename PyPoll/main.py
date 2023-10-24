# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "election_results.txt")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

# Set initial variables to 0
    total_votes = 0
    candidate_votes = {}
    winner_total = 0
    percent_votes = {}

# Iterate through rows
    for row in csvreader:

        # Loop through (sum) total votes
        total_votes += 1

        # Total votes for each candidate
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            candidate_votes[row[2]] = 1

# Calculate percentage of votes for candidates
for x, y in candidate_votes.items():
    percent_votes[x] = round((y/total_votes)*100, 3)

# Define winner
for x in percent_votes:            
    if percent_votes[x] > winner_total:
        winner_total = percent_votes[x]
        winner = x

# Print script in terminal
print(f"Election Results")
print(f"-----------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------")
for x, y in candidate_votes.items():
    print(x,':' , str(percent_votes[x]), '%',' ','(',candidate_votes[x],')')
print(f"-----------------------")
print(f"Winner: {winner}")
print(f"------------------")

# Write to text file
with open(output_file, 'w') as text:
    text.write(f"Election Results\n")
    text.write(f"-----------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write(f"-------------------\n")
    for x, y in candidate_votes.items():
        text.write(f"{x}: {str(percent_votes[x])}%  ({candidate_votes[x]}\n")
    text.write(f"-----------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"------------------\n")