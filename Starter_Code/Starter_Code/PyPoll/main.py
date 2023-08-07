import csv
import os

# Define local Variables
filePath = "Resources/election_data.csv" # Path to the election data CSV file.
totalVotes = 0 # The sum total of all votes.
votesDictionary = {} # Dictionary to hold candidate name and amount of votes.
winner = '' # The final winning candidate.
winningVotes = -1 # The amount of votes the winning candidate has.
output = '' # The final output string.

# Open and evaluate the contents of the CSV file.
with open(filePath) as csv_file:

    reader = csv.reader(csv_file, delimiter = ',') # Define the CSV reader object.
    index = -1 # Index holds the current row of the election data.

    for row in reader:
        index += 1 # Increment the current row of election data that is being evaluated.

        # Skip the header of the CSV file
        if(index == 0): 
            continue

        # Tally the vote information from the given row.
        totalVotes += 1
        ballot_ID = row[0] # The Ballot ID of the current row
        county = row[1] # The County of the current row.
        candidate = row[2] # The Candidate of the current row.

        # Check if the candidate exists in votesDictionary
        if(candidate in votesDictionary):
            # The candidate already exists, increment their votes by one.
            votesDictionary[candidate] += 1
        else:
            # The candidate does not exist in votesDictionary, add the candidate to votesDictionary, and give them this one vote.
            votesDictionary.update({candidate : 1})
      

# Write the header of our results to output
output += ('Election Results')
output += ('\n___________________\n')
output += ('\nTotal votes: ' + str(totalVotes))
output += ('\n___________________\n')
# Calculate the winning candidate and write the results of each candidate to output
for candidate, votes in votesDictionary.items():
    percentageOfVote = '{:.3%}'.format(votes/totalVotes)
    output += ('\n' + str(candidate) + ': ' + percentageOfVote + ' (' + str(votes) +')\n')
    
    # Determine if this candidate has more votes than the candidate with the leading amount of votes.
    if(votes > winningVotes):
        winningVotes = votes
        winner = candidate

# Write the footer of our results to the output
output += ('___________________\n')
output += ('\nWinner!: ' + winner)
output += ('\n___________________\n')


# Write the results to a text file named "Pypoll Output.txt"
with open('PyPoll Output.txt', 'w') as outputFile:
    outputFile.write(output)
outputFile.close()

# Print the results
print(output)

            


        

    