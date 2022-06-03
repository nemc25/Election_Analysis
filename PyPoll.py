import csv
import os


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World")

# # Write three counties to the file.
#     txt_file.write("Arapahoe")
#     txt_file.write("Denver")
#     txt_file.write("Jefferson")

# # Write three counties to the file.
#     txt_file.write("Arapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson")
# # Write three counties to the file.
#     txt_file.write("Arapahoe, Denver, Jefferson")
# Write three counties to the file.
    # txt_file.write("Counties in the election\n---------------------\n")  
    
    # txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies.

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []

#1. Declare the empy dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.    
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Read the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
    for row in file_reader:
        print(row)

#2. Add to the total vote count.
total_votes += 1 


#Print the candidate name from each row.

candidate_name = row[2]

# If the candidate does not match any existing candidate...
if candidate_name not in candidate_options:
    # Add it to the list of candidates.
    candidate_options.append(candidate_name)
    #begin tracking that candidate's vote count
    candidate_votes[candidate_name] = 0
#add a vote to that candidate's count.
candidate_votes[candidate_name] += 1

    #print the candidate vote dictionary.
print(candidate_votes)
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#1 Iterate through the candiate list.
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

 #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
# Winning Candidate and Winning Count Tracker

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
 # If true then set winning_count = votes and winning_percent =
# vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage
# And, set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)