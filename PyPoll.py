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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.    
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
    for row in file_reader:
        print(row)


    
