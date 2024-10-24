import csv
import os
# print("current working directory:", os.getcwd())

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..", "Analysis", "election_analysis.txt")  # Output file path

# print("CSV Path:", os.path.abspath(file_to_load))
# print("txt Output Path:", os.path.abspath(file_to_output))

if not os.path.exists(os.path.dirname(file_to_output)):
    os.makedirs(os.path.dirname(file_to_output))

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_to_load) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    for i, row in enumerate(reader):
        total_votes += 1
        candidate = row[2]  
        if candidate in candidate_votes:
            candidate_votes[candidate]["votes"] += 1
        else:
            candidate_votes[candidate] = {"votes": 1, "percentage": 0}

        # Print a loading indicator every 20000 rows
        # if (i + 1) % 20000 == 0:
            # print(f"Processed {i + 1} rows...")

print()  # New line after the loading indicator

# Calculate percentages and determine the winner
winner = None
max_votes = 0

# Print total votes
# print(f"Total Votes: {total_votes}")

for candidate, info in candidate_votes.items():
    votes = info["votes"]
  
    percentage = (votes / total_votes) * 100
    candidate_votes[candidate]["percentage"] = percentage

    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print election results then dashed line as in HW example
# Print individual candidate votes
# Print (f"{candidate} Votes: {votes}")
# Print calculated percentage
# Print(f"{candidate} Percentage: {percentage:.3f}%")
# Print (f"Winner: {winner}") then add dashed line 
print("Election Results")
print("-------------------------")
for candidate, info in candidate_votes.items():
    print(f"{candidate}: {info['percentage']:.3f}% ({info['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a text file in same format as terminal print
with open("election_analysis.txt", 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, info in candidate_votes.items():
        txt_file.write(f"{candidate}: {info['percentage']:.3f}% ({info['votes']})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
